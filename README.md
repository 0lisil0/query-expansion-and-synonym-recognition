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
- Construct an expanded query

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
