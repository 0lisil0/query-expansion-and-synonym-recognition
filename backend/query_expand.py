import requests
import os
import re

import nltk
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
########### TODO: you might need to change the path ###########


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


def remove_duplicates(words: list, synset: set) -> set:
    """Exclude the user input query from the synset.

    Args:
        synset (set): synset

    Returns:
        set: a set of unique synonyms
    """
    words_and_query = words.copy()
    words_and_query.append(' '.join(words_and_query))
    synset.difference_update(words_and_query)


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
            synonyms.add(lemma.name().replace('_', ' '))

    # exclude elements that already in the query or is the query
    remove_duplicates([cleaned_word], synonyms)

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


def expand_query(query: str) -> list:
    """Expand the input query string by finding synonyms.
    Args:
        - query (str): the user input query string
    Returns:
        - list: a list of synonyms
    """
    synonyms = set()

    # preprocess the query string
    cleaned_query = clean_str(query)
    words = split_string(cleaned_query)

    for word in words:
        # get synset of each word
        synsets = wn.synsets(word)
        for syn in synsets:
            lemmas = syn.lemmas()
            for lemma in lemmas:
                synonyms.add(lemma.name().replace('_', ' '))

    # exclude elements that already in the query or is the query
    remove_duplicates(words, synonyms)

    return list(synonyms)


if __name__ == '__main__':
    # test_query = 'software engineer'
    # eq = expand_query(test_query)
    # print(f"Your query is: {test_query}, and synonyms are: ")
    # for i in eq:
    #     print(f"\t- {i}")

    test_word = 'job'
    a = get_word_synonyms(test_word)
    print(f"Your synonyms are: {a}")
