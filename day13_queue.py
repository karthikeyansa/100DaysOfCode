class Queue:
	def __init__(self):
		self.queue = []

	def push(self, value):
		self.queue.append(value)
		self.display_queue()

	def pop(self):
		self.queue.pop(0)
		self.display_queue()

	def display_queue(self):
		print(self.queue)

queue = Queue()
queue.push(1)
queue.push(3)
queue.push(4)
queue.pop()