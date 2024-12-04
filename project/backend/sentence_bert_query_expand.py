import re

import requests
from sentence_transformers import SentenceTransformer, util


# load Sentence-BERT model
sbert_model = SentenceTransformer("all-MiniLM-L6-v2")


def clean_str(query: str) -> str:
    """Clean the input string by removing whitespace and any
    non-alphanumeric characters.

    Args:
        query (str): the user input string

    Returns:
        str: cleaned string
    """
    # replace non-alphanumeric characters with space
    cleaned_str = re.sub(r'[^a-zA-Z0-9]', ' ', query)

    # remove leading and trailing whitespace
    cleaned_str = cleaned_str.strip()

    return cleaned_str


def get_conceptnet_corpus(query: str, language: str = "en") -> list:
    """Fetch related terms dynamically from ConceptNet's API.

    Args:
        query (str): Input word or phrase.
        language (str): Language code (default: "en").

    Returns:
        list: A list of related terms.
    """
    lang_params = f'/c/{language}/'
    filter_params = f'?filter=/c/{language}'
    url = f"https://api.conceptnet.io/related{
        lang_params}{query}{filter_params}"
    response = requests.get(url).json()

    # extract related terms
    related_terms = []
    for resp in response.get("related", []):
        term = resp["@id"]
        term = term[len(lang_params):]
        term = term.replace('_', ' ')
        if term.lower() != query.lower():  # exclude the original query term
            related_terms.append(term)

    return related_terms


def get_phrase_synonym(phrase: str) -> list:
    """Get synonyms for a phrase using WordNet.

    Args:
        phrase (str): the input phrase.

    Returns:
        list: a list of synonyms.
    """
    # preprocess the query string
    cleaned_phrase = clean_str(phrase)

    corpus = get_conceptnet_corpus(cleaned_phrase)

    # if empty, return
    if not corpus:
        return []

    # generate embeddings for the input sentence and candidate terms
    phrase_embedding = sbert_model.encode(
        cleaned_phrase, convert_to_tensor=True)
    term_embeddings = sbert_model.encode(
        corpus, convert_to_tensor=True)

    # compute cosine similarities
    similarities = util.cos_sim(phrase_embedding, term_embeddings)[0]
    top_indices = similarities.argsort(descending=True)

    return [corpus[idx] for idx in top_indices]


def bert_expand_query(query: str, top_k: int = 10) -> list:
    """Expand the input query string by finding synonyms.
    Args:
        - query (str): the user input query string
    Returns:
        - list: a list of synonyms
    """
    try:
        return get_phrase_synonym(query)[:top_k]
    except Exception as e:
        return [f"Error: {e}"]


if __name__ == '__main__':
    test_query = ['software engineer', 'job', 'heart attack',
                  'mayday', 'examples', 'text information',
                  'text retrieval', 'Chase bank']
    for i in test_query:
        eq = bert_expand_query(i, 5)
        print(f"Your query is: {i}, and synonyms are: ")
        for i in eq:
            print(f"\t- {i}")
