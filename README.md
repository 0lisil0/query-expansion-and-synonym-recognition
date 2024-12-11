# Query Expansion and Synonym Recognition

UIUC CS410 24FA

## Backend
### Tech stack
- Python 3.12.2
- Flask
- NLTK
- ConceptNet API and Sentence BERT model
- Together API

### Functionality
- Process user queries.
- Identify key terms.
- Find synonyms (choose one of the following):
  - Leverage an NLP-based synonym finder powered by NLTK.
  - Use the ConceptNet API to retrieve related terms, followed by the Sentence BERT model to calculate similarity.
  - Utilize the LlaMa free model for synonym identification.
- Construct an expanded query.

## Frontend: 
- A simple HTML page with a text input field, a number input field, a group of radio buttons for algorithm options, a submit button, and a synonym list.

## Installation Requirements

To install the required dependencies, run the following command in the project directory:

```
pip install -r requirements.txt
```

### LLM set up instruction 
Currently we only support the free model Llama-Vision-Free

#### Token setup
1. Create an account (or log in if you already have one) on [Together AI](https://www.together.ai/).
2. To temporarily set the environment variable, use the following command in PowerShell:
    ```
    $env:TOGETHER_API_KEY="your_actual_api_key_here"
    ```
    Alternatively, you can save the key in a .env file and load it from there.

#### Example usage of LLM synonyms finder
    synonym_finder = LlamaQuerySynonymFinder(model_name="meta-llama/Llama-Vision-Free")
    query = "happy"
    synonyms = synonym_finder.get_synonyms(query, num_synonyms=5)
    print(f"synonyms: {synonyms}")

## Start the project

### To start the project, use the following command:
```
python app.py
```

### Open the browser and navigate to:
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)
