class Node:
  def __init__(self, data=None, next_node=None):
    self.next_node = next_node
    self.data = data

  def __repr__(self):
    return str(self.data) + '=>'

class Stack: 
  def __init__(self):
    self.top = None

  def pop(self):
    if self.top:
      temp = self.top.next_node
      self.top.next_node = None
      self.top = temp
    return temp

  def push(self, item):
    newItem= Node(item)
    
    if self.top:
      newItem.next_node = self.top
    self.top = newItem

  def peek(self):
    return self.top.data

  def __str__(self):
    current_node = self.top
    response = ''

    while current_node is not None:
      response += str(current_node.data) + ' => '
      current_node = current_node.next_node

    return response


