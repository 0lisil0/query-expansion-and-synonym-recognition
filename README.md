# Query Expansion and Synonym Recognition

UIUC CS410 24FA

## Backend
- Flask

### Tech stack
- Python 3.12.2
- Flask
- NLTK - for a single word
- ConceptNet API and Sentence BERT model for multiple words

### Functionality
- Process user queries
- Identify key terms
- Find synonyms
  - We provide support using both NLP synonyms finder using NLTK
  - and also LLM using LlaMa free model
- Construct an expanded query

### LLM set up instruction 
Currently we only support the free model Llama-Vision-Free

#### Token setup
    First you need to set up your access to LlaMa model from the below link:
    ```
    https://github.com/meta-llama/llama/blob/main/README.md
    ```
    Then download the model you need
    ```
    https://www.llama.com/llama-downloads/
    ```
    Finally, follow this instruction to set up the credential,  the credential is set up using together
    ```
    https://github.com/meta-llama/llama-recipes/blob/main/recipes/quickstart/build_with_Llama_3_2.ipynb
    ```

#### Example usage of LLM synonyms finder
    synonym_finder = LlamaQuerySynonymFinder(model_name="meta-llama/Llama-Vision-Free")
    query = "happy"
    synonyms = synonym_finder.get_synonyms(query, num_synonyms=5)
    print(f"synonyms: {synonyms}")

## Frontend: 
- A simple HTML page with an input field, a submit button, and a synonym list.

## Installation Requirements

To install the required dependencies, run the following command in the project directory:

```bash
pip install -r requirements.txt
```

## Start the Flask Backend

### To start the Flask backend, use the following command:

```bash
python app.py
```

## Access the Frontend

### Open the browser and navigate to:

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)
