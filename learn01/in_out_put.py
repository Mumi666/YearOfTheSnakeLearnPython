# NPL 统计 word count

import re

def parse(text):
    text = re.sub(r'[^\w ]',' ',text)

    text = text.lower()

    word_list = text.split(' ')

    word_list =  filter(None, word_list)

    word_count = {}
    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    word_count = sorted(word_count.items(),key=lambda x:x[1],reverse=True)

    return word_count

def parse_redline(infile):
    while True:
        text = infile.readline()
        if not text:
            break
        print(parse(text))

        text = re.sub(r'[^\w ]', ' ', text)

        text = text.lower()

        word_list = text.split(' ')
        word_list =  filter(None, word_list)
        word_count = {}
        for word in word_list:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        sort_word_count = sorted(word_count.items(),key=lambda x:x[1],reverse=True)

        return sort_word_count

# with open('test.txt','r') as f:
#     text = f.read()
#
# word_and_freq = parse(text)
#
# with open('result.txt','w') as f:
#     for word,freq in word_and_freq:
#         f.write(word+' '+str(freq)+'\n')

with open('test.txt','r') as f:
    word_and_freq = parse_redline(f)

with open('result_of_readline.txt','w') as f:
    for word,freq in word_and_freq:
        f.write(word+' '+str(freq)+'\n')
