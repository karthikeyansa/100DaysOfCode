class Stack:
	def __init__(self):
		self.stack = []

	def push(self, element):
		self.stack.append(element)

	def pop(self):
		self.stack.pop()

	def get_stack(self):
		return self.stack

stack_obj = Stack()
while True:
	action = input()
	if action == 'push':
		element = input()
		stack_obj.push(element)
	elif action == 'pop':
		stack_obj.pop()
	else:
		break
print(stack_obj.get_stack())
