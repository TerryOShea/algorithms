class Node: 
	def __init__(self, value): 
		self.value = value
		self.next = None

class LinkedList: 
	def __init__(self, root=None): 
		self.root = root

	def add(self, value): 
		if self.root == None: 
			self.root = Node(value)
		else: 
			curr = self.root
			while curr.next: 
				curr = curr.next
			curr.next = Node(value)

	def __repr__(self): 
		return self.node_str(self.root)

	def node_str(self, n): 
		if n == None: 
			return "None"
		else: 
			return str(n.value) + " => " + self.node_str(n.next)

def reverse_linked_list(head): 
	if head is None: return
	prev = None
	while head: 
		head.next, head, prev = prev, head.next, head
	return prev

l = LinkedList()
a = [3, 15, -2, 8, 10, 0, 17]
for item in a: 
	l.add(item)
print(l)
l.root = reverse_linked_list(l.root)
print(l)