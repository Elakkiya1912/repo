# app.py

from flask import Flask, request, jsonify
import text2emotion as te

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Please provide text input'}), 400

    text = data['text']
    emotions = te.get_emotion(text)
    return jsonify({'emotions': emotions})

if __name__ == '__main__':
    app.run(debug=True)
