import os

import nltk
from nltk.corpus import wordnet as wn

########### TODO: you might need to change the path ###########
# download wordnet to destination folder
root = os.path.dirname(os.path.dirname(__file__))
venv_nitk_path = os.path.join(root, '.venv', 'nltk_data')
nltk.download('wordnet', download_dir=venv_nitk_path)

# you can also just use `nltk.download('wordnet')` without specifying path
########### TODO: you might need to change the path ###########


def expand_query(query: str) -> list:
    """Expand the input query string by finding synonyms.
    Args:
        - query (str): the user input query string
    Returns:
        - list: a list of synonyms
    """
    synonyms = []

    return synonyms


if __name__ == '__main__':
    eq = expand_query('software engineer')
