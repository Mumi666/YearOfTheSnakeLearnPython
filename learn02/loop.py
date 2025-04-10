attributes = ['name', 'dob', 'gender']
values = [
            ['jason', '2000-01-01', 'male'],
            ['mike', '1999-01-01', 'male'],
            ['nancy', '2001-02-01', 'female']
        ]

output = []
for i in range(len(values)):
    temp = {}
    for j in range(len(attributes)):
        temp[attributes[j]] = values[i][j]
    output.append(temp)

print(output)

output_in_one_line = [{attributes[j]: values[i][j] for j in range(len(attributes))} for i in range(len(values))]

print(output_in_one_line)
# expected output:
# [{'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'},
# {'name': 'mike', 'dob': '1999-01-01', 'gender': 'male'},
# {'name': 'nancy', 'dob': '2001-02-01', 'gender': 'female'}]
