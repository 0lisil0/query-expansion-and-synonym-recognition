import os
import re

import nltk
from nltk.corpus import wordnet as wn

########### TODO: you might need to change the path ###########
# download wordnet to destination folder
root = os.path.dirname(os.path.dirname(__file__))
venv_nitk_path = os.path.join(root, '.venv', 'nltk_data')
nltk.download('wordnet', download_dir=venv_nitk_path)

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


def expand_query(query: str) -> set:
    """Expand the input query string by finding synonyms.
    Args:
        - query (str): the user input query string
    Returns:
        - set: a set of synonyms
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

    return synonyms


if __name__ == '__main__':
    eq = expand_query('software engineer')
    print(eq)

    # a = {'software engineer', 'applied scientist', 'computer software', 'railroad engineer', 'engine driver', 'engineer', 'locomotive engineer', 'software',
    #      'software package', 'package', 'direct', 'organise', 'orchestrate', 'software program', 'mastermind', 'software system', 'technologist', 'organize'}
    # remove_duplicates(['software', 'engineer'], a)
    # print(a)
