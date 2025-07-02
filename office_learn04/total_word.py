import pathlib
# with open('./file/e.txt', encoding='utf-8') as f:
#     content = f.read()
#     print(content)
#     characters = content.rstrip()
#     char_count = len(characters)
#     print(char_count)

src_path = './file/'

p = pathlib.Path(src_path)
all_txt_file = [x for x in p.iterdir() if pathlib.PurePath(x).match('*.txt')]

char_count_list = []

for file in all_txt_file:
    with open(file, encoding='utf-8') as f:
        content = f.read()
        characters = content.rstrip()
        char_count = len(characters)
        char_count_list.append(char_count)

print(char_count_list)
print(sum(char_count_list))


