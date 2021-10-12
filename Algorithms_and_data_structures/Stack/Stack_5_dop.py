class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop(0)
        else:
            return None 

    def push(self, value):
        self.stack.insert(0, value)

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[0]
        else:
            return None 

def Reverse_Polish_notation(polish_string):
    S1 = Stack()
    S2 = Stack()
    polish_list = polish_string.split()
    for k in range(0, len(polish_list)):
        if polish_list[k].isalnum():
            polish_list[k] = int(polish_list[k])
    for i in range(len(polish_list)-1, -1, -1):
        S1.push(polish_list[i])
    while S1.size() > 0:
        if type(S1.peek()) == int:
            S2.push(S1.pop())
        elif S1.peek() == '+':
            S1.pop()
            a = S2.pop()
            b = S2.pop()
            S2.push(a+b)
        elif S1.peek() == '*':
            S1.pop()
            a = S2.pop()
            b = S2.pop()
            S2.push(a*b)
        else:
            S1.pop()
            return S2.pop()
