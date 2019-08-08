
class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class Linked_list:
	def __init__(self):
		self.head = None

	def get_head(self):
		return self.head

	def insert_node(self, value):
		new_node = Node(value)
		if self.head is None:
			self.head = new_node
		else:
			temp = self.head
			while temp.next is self.head:
				temp = temp.next
			temp.next = new_node

def print_list(node):
	print(node.value)
	while node.next:
		node = node.next
		print(node.value)

list_1 = Linked_list()
arr = [1,2,3,4,4,6,7,4,2,8]
for i in arr:
	list_1.insert_node(i)
print_list(list_1.get_head())