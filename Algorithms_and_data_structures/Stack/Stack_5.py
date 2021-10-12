class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None 

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None 

def proverka_skobok(skobki):
    sk_stack = Stack()
    if (len(skobki) % 2 == 0) and (skobki[0] == "("):
        for i in range(0, len(skobki)):
            if skobki[i] == "(":
                sk_stack.push(1)
            else:
                sk_stack.pop()
        if sk_stack.size() == 0:
            return True
        else:
            return False
    else:
        return False
