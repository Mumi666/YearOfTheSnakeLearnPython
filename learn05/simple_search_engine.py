from learn05.search_engine_base import SearchEngineBase


class SimpleSearchEngine(SearchEngineBase):
    def __init__(self):
       super(SimpleSearchEngine, self).__init__()
       self.__id_to_text = {}
    def process_corpus(self, id, text):
        self.__id_to_text[id] = text
    def search(self, query):
        results = []
        for id, text in self.__id_to_text.items():
            if query in text:
                results.append(id)
        return results



# def main(search_engine):
#     for file_path in ['a.txt', 'b.txt', 'c.txt','d.txt','e.txt']:
#         search_engine.add_corpus(file_path)
#     while True:
#         query = input()
#         if query == 'exit':
#             break
#         results = search_engine.search(query)
#         print('find {} result'.format(len(results)))
#         for result in results:
#             print(result)
#
# simple_search_engine = SimpleSearchEngine()
# main(simple_search_engine)