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


def clean_str(query:str)->str:
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
    
    
def expand_query(query: str) -> set:
    """Expand the input query string by finding synonyms.
    Args:
        - query (str): the user input query string
    Returns:
        - set: a set of synonyms
    """
    synonyms = set()
    words=query.split()
    
    

    return synonyms


if __name__ == '__main__':
    eq = expand_query('software engineer')
    print(eq)
