
class Node():
	def __init__(self, value):
		self.next = None
		self.prev = None
		self.value = value

class linked_list():
	def __init__(self):
		self.head = None
		self.tail = None

	def get_head(self):
		return(self.head)

	def get_tail(self):
		return(self.tail)

	def insert_node(self, value):
		if self.head is None:
			self.head = Node(value)
			self.head.prev = None 
			self.head.next = None
		else:
			temp = self.head
			new_node = Node(value)
			while temp.next:
				temp = temp.next
			temp.next = new_node
			new_node.prev = temp
			self.tail = new_node

def print_list_with_head(node):
	while node.next:
		print(node.value)
		node = node.next
	print(node.value)

def print_list_with_tail(node):
	while node.prev:
		print(node.value)
		node = node.prev
	print(node.value)

list_1 = linked_list()
arr = [1,2,3,4,5,6,7,8]
for i in arr:
	list_1.insert_node(i)
print_list_with_head(list_1.get_head())
print_list_with_tail(list_1.get_tail())


