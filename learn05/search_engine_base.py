class SearchEngineBase(object):
    def __init__(self):
        pass
    def add_corpus(self, file_path):
        with open(file_path, 'r') as f:
            text = f.read()
            self.process_corpus(file_path, text)
    def process_corpus(self, id, text):
        raise Exception('process_corpus not implemented')
    def search(self, query):
        raise Exception('search not implemented')

