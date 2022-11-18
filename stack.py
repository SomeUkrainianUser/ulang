class Object:
    def __init__(self, next, data):
        self.data = data
        self.next = next

class Stack:
    top = Object(None, None)
    def push(self, d):
        obj = Object(self.top, d)
        self.top = obj

    def pop(self):
        tmp = self.top
        self.top = self.top.next
        return tmp

    def show(self):
        i = self.top
        while i is not None:
            print(i.data)
            i = i.next