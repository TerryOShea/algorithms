def largest_in_binary_tree(root): 
    curr = root
    while curr: 
        if not curr.right: 
            return curr.value
        curr = curr.right

def second_largest_in_binary_tree(root): 
    curr = root
    while curr: 
        if curr.left and not curr.right: 
            return largest_in_binary_tree(curr)
        if curr.right and not curr.right.left and not curr.right.right: 
            return curr.value
        curr = curr.right

class Node: 
    def __init__(self, value): 
        self.value = value
        self.left = None
        self.right = None

class Tree: 
    def __init__(self): 
        self.root = None

    def getRoot(self): 
        return self.root

    def add(self, value, node): 
        if self.root == None: self.root = Node(value)
        elif value < node.value: 
            if node.left == None: node.left = Node(value)
            else: self.add(value, node.left)
        else: 
            if node.right == None: node.right = Node(value)
            else: self.add(value, node.right)

t = Tree()
node_values = [4, 7, 10, 1, -3, 6, 18, 2, 36, -26]
for item in node_values: 
    t.add(item, t.getRoot())
print(second_largest_in_binary_tree(t.getRoot()))