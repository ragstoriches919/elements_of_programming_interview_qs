class Stack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def empty(self):
        return len(self.stack) == 0

    def max(self):
        if self.max_stack:
            return self.max_stack[-1]

    def push(self, x):
        self.stack.append(x)
        if len(self.max_stack) == 0:
            self.max_stack.append(x)
        elif x > self.max_stack[-1]:
            self.max_stack.append(x)

    def pop(self):

        if self.empty():
            return

        if self.stack[-1] == self.max_stack[-1]:
            self.max_stack.pop()

        return self.stack_pop()



