class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

def insert_node(root_node, new_node):
	if new_node.value > root_node.value:
		if root_node.right is None:
			root_node.right = new_node
		else:
			insert_node(root_node.right, new_node)
	else:
		if root_node.left is None:
			root_node.left = new_node
		else:
			insert_node(root_node.left, new_node)

def level_order_traversal(node, level, level_order_list):
	if node:
		if level == 1:
			level_order_list.append(node.value)
		elif level > 1:
			level_order_traversal(node.left, level-1, level_order_list)
			level_order_traversal(node.right, level-1, level_order_list)
	return level_order_list

def height(node):
  if node is None:
    return 0
  else:
    return max(height(node.left), height(node.right)) + 1

tree_nodes = [7, 8, 2, 3, 1, 4, 6, 9]
root_node = Node(tree_nodes[0])
tree_nodes.pop(0)
for tree_node in tree_nodes:
	new_node = Node(tree_node)
	insert_node(root_node, new_node)
tree_height = height(root_node)
level_order_dict = {}
for level in range(1, tree_height+1):
	level_order_list = level_order_traversal(root_node, level, [])
	level_order_dict[level] = level_order_list
print(level_order_dict)