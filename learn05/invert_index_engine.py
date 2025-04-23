import re

from learn05.search_engine_base import SearchEngineBase


class InvertIndexEngine(SearchEngineBase):
    def __init__(self):
        super(InvertIndexEngine, self).__init__()
        self.inverted_index = {}

    def process_corpus(self, id, text):
        words = self.parse_text_to_words(text)
        for word in words:
            if word not in self.inverted_index:
                self.inverted_index[word] = []
            self.inverted_index[word].append(id)

    def search(self, query):
        query_words =list(self.parse_text_to_words(query))
        query_words_index = list()

        for query_word in query_words:
            query_words_index.append(0)


        for query_word in query_words:
            if query_word not in self.inverted_index:
                return []

        results = []

        while True:
            current_ids = []
            for idx, query_word in enumerate(query_words):
                current_idx = query_words_index[idx]
                current_inverted_list = self.inverted_index[query_word]
                if current_idx >= len(current_inverted_list):
                    return results
                current_ids.append(current_inverted_list[current_idx])

            if all(x == current_ids[0] for x in current_ids):
                results.append(current_ids[0])
                query_words_index = [x + 1 for x in query_words_index]
                continue

            min_val = min(current_ids)
            min_val_pos = current_ids.index(min_val)
            query_words_index[min_val_pos] += 1


    @staticmethod
    def parse_text_to_words(text):
        text = re.sub(r'[^\w ]', ' ', text)
        text = text.lower()
        ward_list = text.split(' ')
        ward_list = filter(None, ward_list)
        return set(ward_list)


    # wifi 身份证后六位+@+ynby.cn
    # 00257678
    # shihongjin@ynby.cn