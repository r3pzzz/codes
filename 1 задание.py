class Stack:
    def __init__(self, size=10):
        self.size = size
        self.stack = [None] * size
        self.top_index = -1

    def push(self, value):
        if self.top_index == self.size - 1:
            print("Ошибка: Стек переполнен")
            return
        self.top_index += 1
        self.stack[self.top_index] = value

    def pop(self):
        if self.is_empty():
            print("Ошибка: Стек пуст")
            return None
        value = self.stack[self.top_index]
        self.stack[self.top_index] = None
        self.top_index -= 1
        return value

    def top(self):
        if self.is_empty():
            print("Ошибка: Стек пуст!")
            return None
        return self.stack[self.top_index]

    def is_empty(self):
        return self.top_index == -1

    def __str__(self):
        return str(self.stack[:self.top_index + 1])
stack = Stack(3)

stack.push(1)
stack.push(2)
stack.push(3)
print(stack)  #[1, 2, 3]

stack.push(4)  #ошибка

print(stack.top())  #[3]
print(stack.pop())  #[3]
print(stack.pop())  #[2]
print(stack.pop())  #[1]
print(stack.pop())  #ошибка