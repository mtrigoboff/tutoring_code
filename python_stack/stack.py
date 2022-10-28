stack = []

def push(item):
	stack.insert(0, item)
	print(f'pushed {item}')

def pop():
	global stack
	item = stack[0]
	stack = stack[1:]
	print(f'popped {item}')
	return item

print(f'stack {stack}')
push('a')
print(f'stack {stack}')
push('b')
print(f'stack {stack}')
push('c')
print(f'stack {stack}')
push('d')
print(f'stack {stack}')

pop()
print(f'stack {stack}')
pop()
print(f'stack {stack}')
pop()
print(f'stack {stack}')
pop()
print(f'stack {stack}')