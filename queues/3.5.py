from Stack import Stack

class MyQueue:

  def __init__(self):
    self.stack1 = Stack()
    self.stack2 = Stack()

  def enqueue(self, item):
     self.stack1.push(item)

  def dequeue(self):
   
    while self.stack1.top != None:
      self.stack2.push(self.stack1.pop())

    self.stack2.pop()
    print(self.stack2)

    while self.stack2.top != None:
      self.stack1.push(self.stack2.pop())


poop = MyQueue()

poop.enqueue(3)
poop.enqueue(4)
poop.enqueue(5)

print(poop.stack1)

poop.dequeue()
print(poop.stack1)
