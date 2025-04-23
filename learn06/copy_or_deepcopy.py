import copy

x = [1]

# x.append(x)

y = copy.deepcopy(x)

print(x == y)
print(x is y)