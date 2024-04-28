from opensearchpy import OpenSearch

class OpenSearchClient:
    def __init__(self, host='localhost', port=9200):
        self.host = host
        self.port = port
        self.client = OpenSearch(
            hosts=[{'host': self.host, 'port': self.port}],
            http_compress=True,
            use_ssl=False,
            verify_certs=False,
            ssl_assert_hostname=False,
            ssl_show_warn=False
        )

    
    def index_document(self, index, body, doc_id=None):
        response = self.client.index(index=index, body=body, id=doc_id)
        return response

    def get_document(self, index, doc_id):
        response = self.client.get(index=index, id=doc_id)
        return response

    def update_document(self, index, doc_id, body):
        response = self.client.update(index=index, id=doc_id, body=body)
        return response

    def delete_document(self, index, doc_id):
        response = self.client.delete(index=index, id=doc_id)
        return response

    def search(self, index, query):
        response = self.client.search(index=index, body=query)
        return response