import os
import re

import nltk
import requests
from nltk.corpus import wordnet as wn
from sentence_transformers import SentenceTransformer, util

########### TODO: you might need to change the path ###########
# download wordnet to destination folder
root = os.path.dirname(os.path.dirname(__file__))
venv_nitk_path = os.path.join(root, '.venv', 'nltk_data')
nltk.download('wordnet', download_dir=venv_nitk_path)

# add to path
nltk.data.path.append(venv_nitk_path)

# you can also just use `nltk.download('wordnet')` without specifying path
# nltk.download('wordnet')
########### TODO: you might need to change the path ###########

# Load Sentence-BERT model
# Lightweight semantic similarity model
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


def split_string(query: str) -> list:
    """Split the cleaned string into a list of words

    Args:
        query (str): the cleaned string

    Returns:
        list: a list of words in the cleaned string
    """
    return query.split()


def get_word_synonyms(word: str) -> list:
    """Get synonyms for a single word using WordNet.

    Args:
        word (str): the input word.

    Returns:
        list: a list of synonyms.
    """
    synonyms = set()

    # preprocess the word string
    cleaned_word = clean_str(word)

    # get synset of each word
    synsets = wn.synsets(cleaned_word)
    for syn in synsets:
        lemmas = syn.lemmas()
        for lemma in lemmas:
            syn = lemma.name().replace('_', ' ').lower()
            if word != syn:
                synonyms.add(syn)

    return list(synonyms)


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

    # generate embeddings for the input sentence and candidate terms
    phrase_embedding = sbert_model.encode(
        cleaned_phrase, convert_to_tensor=True)
    term_embeddings = sbert_model.encode(
        corpus, convert_to_tensor=True)

    # compute cosine similarities
    similarities = util.cos_sim(phrase_embedding, term_embeddings)[0]
    top_indices = similarities.argsort(descending=True)

    return [corpus[idx] for idx in top_indices]


def expand_query(query: str, top_k: int = 10) -> list:
    """Expand the input query string by finding synonyms.
    Args:
        - query (str): the user input query string
    Returns:
        - list: a list of synonyms
    """
    # check if the input is a single word or a sentence
    if " " not in query.strip():
        res = get_word_synonyms(query)[:top_k]
        if not res:
            print('--------- not found ------------')
            return get_phrase_synonym(query)[:top_k]
        return res
    else:
        return get_phrase_synonym(query)[:top_k]


if __name__ == '__main__':
    test_query = ['software engineer', 'job', 'heart attack',
                  'mayday', 'examples', 'text information']
    for i in test_query:
        eq = expand_query(i)
        print(f"Your query is: {i}, and synonyms are: ")
        for i in eq:
            print(f"\t- {i}")
