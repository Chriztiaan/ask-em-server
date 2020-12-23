# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import json
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# http://127.0.0.1:5000/questionnaire/question1
@app.route('/questionnaire/<questionnaire>', methods=['GET'])
def test(questionnaire):
    with open(questionnaire + '.json') as json_file:
        data = json.load(json_file)
        return jsonify(data)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)