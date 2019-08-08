
class Node:
	def __init__(self):
		self.value = None
		self.next = None

class Linked_list:
	def __init__(self):
		self.head = None

	def get_head(self):
		return self.head

	def insert_node(self, value):
		if self.head is None:
			self.head = Node()
			self.head.value = value
		else:
 			new_node = Node()
 			new_node.value = value
 			new_node.next = None
 			temp_node = self.head
 			while temp_node.next:
 				temp_node = temp_node.next
 			temp_node.next = new_node

def print_list(node):
    while node:
        print(node.value, end = " ")
        node = node.next

arr = [1,2,3,4,5,6,7,8]
list_1 = Linked_list()
for i in arr:
	list_1.insert_node(i)
print_list(list_1.get_head())

 			