import operator

d = {'mike': 10, 'lucy': 2, 'ben': 30}

# d_sorted = sorted(d.items(), key=lambda x: -x[1])

d_sorted = sorted(d.items(), key= operator.itemgetter(1), reverse=True)

print(d_sorted)