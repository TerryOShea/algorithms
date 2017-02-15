import random

class Queue:
    def __init__(self):
        self.front = []
        self.back = []

    def enqueue(self, n):
        self.back.append(n)
        return True

    def dequeue(self):
        if not self.front:
            if not self.back: return None
            while self.back:
                self.front.append(self.back.pop())
        return self.front.pop()

    def __str__(self):
        return " <- ".join([str(el) for el in self.front[::-1] + self.back])

if __name__ == "__main__":
    q = Queue()
    for _ in range(15):
        q.enqueue(random.randint(1, 100))
