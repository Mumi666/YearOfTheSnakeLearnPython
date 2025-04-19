from learn05.bow_engine import BOWEngine
from learn05.invert_index_engine import InvertIndexEngine
from learn05.invert_index_engine_with_cache import InvertIndexEngineWithCache
from learn05.simple_search_engine import SimpleSearchEngine


def main(search_engine):
    for file_path in ['a.txt', 'b.txt', 'c.txt','d.txt','e.txt']:
        search_engine.add_corpus(file_path)
    while True:
        query = input()
        if query == 'exit':
            break
        results = search_engine.search(query)
        print('find {} result'.format(len(results)))
        for result in results:
            print(result)

# simple_search = SimpleSearchEngine()
# main(simple_search)

# bow_engine = BOWEngine()
# main(bow_engine)

# invert_engine = InvertIndexEngine()
# main(invert_engine)

inverse_engine_with_cache = InvertIndexEngineWithCache()
main(inverse_engine_with_cache)