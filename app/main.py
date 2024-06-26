from flask import Flask, jsonify
from flask_cors import CORS
from opensearch_client import OpenSearchClient
from image_metadata import ImageMetadata
import utils

app = Flask(__name__)
CORS(app)
os_client = OpenSearchClient('localhost', 9200)

@app.route('/images', methods=['GET'])
def get_documents():
    response = os_client.client.search(index="images", body={"query": {"match_all": {}}})
    return jsonify(response['hits']['hits'])

@app.route('/hello', methods=['GET'])
def get_hello():
    s = 'hello world'
    return jsonify(s)
if __name__ == '__main__':
    app.run(debug=True)