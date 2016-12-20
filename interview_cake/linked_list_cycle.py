def linked_list_cycle(root): 
	if root == None: return False
	slow, fast = root, root.next
	while slow != fast: 
		if fast == None or fast.next == None: return False
		slow, fast = slow.next, fast.next.next
	return True

class Node: 
	def __init__(self, val): 
		self.value = val
		self.next = None

class Linked_List: 
	def __init__(self): 
		self.root = None
		self.last = None
	def add(self, val): 
		if not self.root: 
			self.root = Node(val)
			self.last = self.root
		else: 
			curr = self.root
			while curr.next: 
				curr = curr.next
			curr.next = Node(val)
			self.last = curr.next
	def __str__(self): 
		return self.print_tree(self.root)
	def print_tree(self, node): 
		if not node: return 'None'
		else: return str(node.value) + ' => ' + self.print_tree(node.next)

t = Linked_List()
t.add(5)
t.add(7)
t.add(-1)
print(linked_list_cycle(t.root))
t.last.next = t.root
print(linked_list_cycle(t.root))