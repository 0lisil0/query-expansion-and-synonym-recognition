from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from together import Together
import os
import requests
import json
from dotenv import load_dotenv
import ast


class LlamaQuerySynonymFinder:
    """
    A class to find synonyms for a given query using the LLaMA model.
    """

    def __init__(self, model_name: str = "meta-llama/Llama-Vision-Free"):
        """
        Initialize the synonym finder with the desired LLaMA model.

        Args:
            model_name (str): The name of the LLaMA model to use.
                              Defaults to 'meta-llama/Llama-Vision-Free'.
        """
        load_dotenv()
        self.model_name = model_name
        self.api_key = os.getenv("TOGETHER_API_KEY")
        if not self.api_key:
            raise ValueError(
                "TOGETHER_API_KEY environment variable is not set.")

    def _llama32(self, messages):
        model = self.model_name
        url = "https://api.together.xyz/v1/chat/completions"
        payload = {
            "model": model,
            "max_tokens": 4096,
            "temperature": 0.0,
            "stop": ["<|eot_id|>", "<|eom_id|>"],
            "messages": messages
        }

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        res = json.loads(requests.request(
            "POST", url, headers=headers, data=json.dumps(payload)).content)

        if 'error' in res:
            raise Exception(res['error'])

        return res['choices'][0]['message']['content']

    def get_synonyms(self, query: str, num_synonyms: int = 5) -> list:
        """
        Generate synonyms for the input query.

        Args:
            query (str): The query for which synonyms are needed.
            num_synonyms (int): The number of synonyms to generate.

        Returns:
            list: A list of synonyms generated for the query.
        """
        try:
            messages = [
                {
                    "role": "user",
                    "content": f"You are a helpful AI assistant, you will find the top {num_synonyms} synonyms of {query} and return results as a list, the output format should follow the following example: ['joyful', 'cheerful', 'glad']"
                }
            ]

            response = self._llama32(messages)
            print(f"response from model: {response}")
            # Extract synonyms from the generated text
            synonyms = self._parse_synonyms(response)
            return synonyms
        except Exception as e:
            print(f"Error generating synonyms: {e}")
            return []

    def _parse_synonyms(self, text: str) -> list:
        """
        Parse the synonyms from the generated text.

        Args:
            text (str): The generated text from the model.
            num_synonyms (int): The expected number of synonyms.

        Returns:
            list: A list of parsed synonyms.
        """
        # Attempt to split the text and extract the synonyms
        try:
            start = text.index(":")+1
            end = start+1

            # Loop through the string in reverse to find the last occurrence
            length = len(text)-1
            for i in range(length, start, -1):
                if text[i] == ']':
                    end = i
                    break
            if end-start <= 1:
                return ['No results found']
            sub_text = text[start:end+1].strip()

            if sub_text.count('[') > 1:
                return sub_text.split('\n\n')

            return ast.literal_eval(sub_text)
        except Exception:
            return ["Could not parse synonyms"]
