class Node:
  def __init__(self, data, next_node=None):
    self.next_node = next_node
    self.data = data

  def __repr__(self):
    return str(self.data) + '=>'

class LinkedList:

  def __init__(self):
    self.head = None
    self.tail = None

  def append_to_tail(self, data):
    new_node = Node(data)
    if self.head == None and self.tail == None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next_node = new_node
      self.tail = new_node

  def remove(self, data):
    current_node = self.head
    previous_node = None
    while current_node is not None:
      if current_node.data is data:
        #deleting list with one item
        if current_node is self.head and current_node is self.tail:
          self.head = None
          self.tail = None
        #deleting head
        elif current_node is self.head:
          self.head = current_node.next_node
        #deleting tail
        elif current_node is self.tail:
          self.tail = previous_node
          self.tail.next_node = None
        #deleting in between
        else:
          previous_node.next_node = current_node.next_node
          current_node.next_node = None
        current_node = None
        break
 
      previous_node = current_node
      current_node = current_node.next_node

    return False

  def __str__(self):
    current_node = self.head
    response = ''

    while current_node is not None:
      response += str(current_node.data) + ' => '
      current_node = current_node.next_node

    return response




