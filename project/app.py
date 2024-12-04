from backend.llm_query_expansion import LlamaQuerySynonymFinder
from backend.nltk_query_expand import nltk_expand_query
from backend.sentence_bert_query_expand import bert_expand_query
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # enable Cross-Origin Resource Sharing, looks like it is not useful tho

# Serve the HTML js: http://127.0.0.1:5000


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

        if not word:
            return jsonify({'error': 'No word provided'}), 400

        # Call the `expand_query` function, which is currently a build-in function now
        # TODO: probably implement our own expand_query function here, but it might be time-consuming
        synonyms = bert_expand_query(word)
        return jsonify({'synonyms': synonyms})
    except Exception as e:
        # internal fault return 500
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
