def delete_node(n): 
    next_node = n.next
    if next_node: 
        n.value = next_node.value 
        n.next = next_node.next
    else: 
        raise Exception("can't delete the last node in a linked list this way!")

class Node: 
    def __init__(self, value): 
        self.value = value 
        self.next = None 
    
    def __str__(self): 
        if not self.next: 
            return self.value
        else: 
            return self.value + " -> " + str(self.next)

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
a.next = b 
b.next = c
c.next = d
d.next = e
e.next = f

print(a)
delete_node(f)
print(a)