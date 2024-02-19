import copy
a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
b = {}
b = copy.deepcopy(a)
for i, v in b.items():
    if v % 2 == 0:
        b[i] = 2
print(b)
