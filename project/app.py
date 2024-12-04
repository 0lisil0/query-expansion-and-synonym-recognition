import os

import nltk
from backend.llm_query_expansion import LlamaQuerySynonymFinder
from backend.nltk_query_expand import nltk_expand_query
from backend.sentence_bert_query_expand import bert_expand_query
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from nltk.corpus import wordnet as wn

########### TODO: you might need to change the path ###########
# download wordnet to destination folder
# root = os.path.dirname(os.path.dirname(__file__))
# venv_nitk_path = os.path.join(root, '.venv', 'nltk_data')
# nltk.download('wordnet', download_dir=venv_nitk_path)

# add to path
# nltk.data.path.append(venv_nitk_path)
# you can also just use `nltk.download('wordnet')` without specifying path
########### TODO: you might need to change the path ###########
nltk.download('wordnet')

app = Flask(__name__)
CORS(app)  # enable Cross-Origin Resource Sharing, looks like it is not useful tho

# Serve the HTML js: http://127.0.0.1:5000


class Option1Handler:
    def process(self, word, topk):
        print(f"Processed '{word}' with Option 1")
        return bert_expand_query(word, topk)


class Option2Handler:
    def process(self, word, topk):
        print(f"Processed '{word}' with Option 2")
        synonym_finder = LlamaQuerySynonymFinder(
            model_name="meta-llama/Llama-Vision-Free")
        return synonym_finder.get_synonyms(word, topk)


class Option3Handler:
    def process(self, word, topk):
        print(f"Processed '{word}' with Option 3")
        return nltk_expand_query(word, topk)


option_map = {
    "Option1": Option1Handler(),
    "Option2": Option2Handler(),
    "Option3": Option3Handler(),
}


@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

# Add the `/expand` endpoint to call the def expand_query() function under backend and in query_expand


@app.route('/expand', methods=['POST'])
def expand():
    try:
        # Parse JSON data
        data = request.get_json()
        word = data.get('word')
        option = data.get('option')
        topk = int(data.get('topk'))

        if not word:
            return jsonify({'error': 'No word provided'}), 400

        # Call the `expand_query` function, which is currently a build-in function now
        # TODO: probably implement our own expand_query function here, but it might be time-consuming

        handler = option_map.get(option)
        if not handler:
            return jsonify({"error": "Invalid option selected"}), 400

        synonyms = handler.process(word, topk)
        return jsonify({"synonyms": synonyms}), 200

    except Exception as e:
        # internal fault return 500
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
