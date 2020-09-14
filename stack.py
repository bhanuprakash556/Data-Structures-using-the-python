class stack():
    def __init__(self):
        self.stack = list()

    def push(self,item):
           self.stack.append(item)

    def pop(self):
        if len(self.stack)>0:
          self.stack.pop()
        else:
            print("No elements to pop from the stack")


    def __str__(self):
        return str(self.stack)








line = stack()

line.push(13)
line.push(14)
line.push(15)
line.pop()
line.pop()
line.pop()
line.pop()

