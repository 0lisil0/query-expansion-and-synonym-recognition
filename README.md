# Query Expansion and Synonym Recognition

## CS 410 Text Information Systems, 2024 Fall

- Lisi Lei (lisilei2@illinois.edu)
- Ivy He (qiuhanh2@illinois.edu)
- Hilda Liu (hildal2@illinois.edu)
- Puyu Yang (pyang33@illinois.edu)
- Meilin Liu (meilinl2@illinois.edu)

## Abstract

This project provides a web-based interface for exploring query expansion techniques through synonym recognition. By leveraging various NLP models and frameworks, users can input a query term, choose an algorithm, and retrieve expanded queries with semantically similar terms. This tool is designed to showcase the practical applications of synonym recognition and query expansion in text-based information retrieval.

## Introduction

Effective information retrieval often hinges on understanding and expanding user queries to include related terms. This project demonstrates how synonym recognition can be integrated with query expansion using state-of-the-art NLP models and frameworks. Users can select between multiple backend algorithms to observe the impact of different approaches, such as statistical and neural-based methods, on synonym retrieval.

The application integrates:

- **NLTK** for traditional synonym matching.
- **ConceptNet** combined with **Sentence BERT** for semantic similarity.
- **Llama-Vision-Free** (via the Together API) for large language model-based synonym generation.

The system is designed to provide a user-friendly interface while demonstrating advanced back-end processing capabilities.

## Backend

### Tech Stack
- **Python**: Version 3.12.2
- **Flask**: Web framework for serving the application
- **NLTK**: For lexical-based synonym retrieval
- **ConceptNet API**: Knowledge graph for semantic relationships
- **Sentence BERT**: Pretrained model for similarity scoring
- **Together API**: Integration for the Llama-Vision-Free LLM

### Core Functionality
1. **Query Processing**: Accepts a user-inputted query and extracts the main term.
2. **Synonym Retrieval**:
   - **NLTK**: Provides synonyms from lexical resources.
   - **ConceptNet + Sentence BERT**: Retrieves related terms and ranks them based on semantic similarity.
   - **Llama-Vision-Free**: Uses an LLM for dynamic synonym generation.
3. **Query Expansion**: Outputs the original query expanded with the retrieved synonyms.

## Frontend

### Features
- A responsive and intuitive web page for user interaction.
- Input fields for the query term and maximum number of synonyms.
- Algorithm selection via radio buttons:
  - BERT-based retrieval
  - LLM-based retrieval
  - NLTK-based retrieval
- Dynamically generated results displayed as a list with options to copy individual or all results.

## Installation Requirements

### Prerequisites
To get started with the Query Expansion Tool, ensure you have the following installed on your machine:

- **Python**: Version 3.12.2 or later
- **pip**: Python package manager

### Backend Installation
1. Clone the repository:
```
   git clone https://github.com/0lisil0/query-expansion-and-synonym-recognition
```
2. Run the following command in the project directory to install dependencies:
```
pip install -r requirements.txt
```

### Environment Setup for LLM Integration
This project supports **Llama-Vision-Free** through the Together API for LLM-based synonym retrieval.

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

## Usage Instructions
### Start the Application
1. Navigate to the project directory.

2. Start the Flask backend server:
    ```
    python app.py
    ```
3. Open your browser and access the application:
- URL: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)


## Tutorial

A video tutorial can be found here: TODO

## Contribution of Team Members
- Backend Implementation (`llm_query_expansion.py`, `nltk_query_expand.py`, `sentence_bert_query_expand.py`) : Lisi Lei, Meilin Liu 
- Frontend Implementation (`index.html`): Ivy He, Hilda Liu
- Flask Implementation (`index.html`, `requirements.txt`, `app.py`) Puyu Yang 
- Testing: Meilin Liu, Lisi Lei
- Tech Review: Lisi Lei , Meilin Liu , Hilda Liu 
- Short Video Presenation: Hilda Liu