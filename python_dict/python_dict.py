dict = {'a': ['ape', 'ant', 'aardvark'], 'b': ['bat', 'bison'], 'c': []}

total = 0
for val in dict.values():
	total += len(val)
print(f'total = {total}')

total = sum([len(val) for val in dict.values()])
print(f'total = {total}')