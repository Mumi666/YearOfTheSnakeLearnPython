def fun(d):
    d['a'] = 20
    d['b'] = 30

d = {'a': 1, 'b': 2}
fun(d)
print(d)
# {'a': 20, 'b': 30}

# 因为python是赋值传递
