# Query Expansion and Synonym Recognition
UIUC CS410 24FA

## Backend
### Tech stack
- Python 3.12.2
- Flask
- NLTK

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

### TODO
- Use Flask to get user queries from frontend
- Use Flask to return expanded queries

# Frontend: Pending
