class Stack():

   def __init__(self):
       self.items=[]
   def push(self,data):
       self.items.append(data)
   def get(self):
       return self.items
   def pop(self):
       self.items.pop()
   def isempt(self):
       return sel.items==[]
stack= Stack()
stack.push('A')
stack.push('B')
stack.push('C')
stack.push('D')
print(stack.get())
print('\n')
stack.pop()
print(stack.get())
