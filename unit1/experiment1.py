class Stack:
    def __init__(self):
        self.arr = []

    def push(self, x):
        self.arr.append(x)

    def pop(self):
        if len(self.arr) == 0:
            print("Stack is empty")
            return None
        return self.arr.pop()

    def peek(self):
        if len(self.arr) == 0:
            return None
        return self.arr[-1]

    def isEmpty(self):
        return len(self.arr) == 0


s = Stack()

s.push(10)
s.push(20)
s.push(30)

print("Top element:", s.peek())
print("Popped:", s.pop())
print("Stack now:", s.arr)