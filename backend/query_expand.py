import nltk
import os

########### TODO: you might need to change the path ###########
# download wordnet to destination folder
root = os.path.dirname(os.path.dirname(__file__))
venv_nitk_path = os.path.join(root, '.venv', 'nltk_data')
nltk.download('wordnet', download_dir=venv_nitk_path)

# you can also just use `nltk.download('wordnet')` without specifying path
########### TODO: you might need to change the path ###########

