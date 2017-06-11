class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

    def length(self): 
        return len(self.items)

class MaxStack:
    """
    The MaxStack class uses the Stack class above but enables a constant-time get_max method:
    the stack stores each item as a list where the 0th index contains the item value and the 1st
    index the max at the time of the item's insertion (either that item or the existing max,
    whichever is bigger)
    """
    def __init__(self):
        self.stack = Stack()

    def push(self, item):
        if self.stack.length() == 0:
            self.stack.push([item, item])
        else:
            last_max = self.stack.peek()[1]
            self.stack.push([item, max(item, last_max)])

    def pop(self):
        item, _ = self.stack.pop()
        return item

    def get_max(self):
        _, current_max = self.stack.peek()
        return current_max

ms = MaxStack()
ms.push(6)
ms.push(5)
ms.push(13)
ms.push(1)
print(ms.get_max())
ms.pop()
ms.pop()
print(ms.get_max())
