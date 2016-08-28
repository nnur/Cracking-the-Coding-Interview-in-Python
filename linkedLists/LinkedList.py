class Node:
  def __init__(self, data, next_node=None):
    self.next_node = next_node
    self.data = data

  def __repr__(self):
    return str(self.data) + '=>'

class LinkedList:

  def __init__(self):
    self.first_node = None
    self.last_node = None

  def append_to_tail(self, data):
    new_node = Node(data)
    if self.first_node == None and self.last_node == None:
      self.first_node = new_node
      self.last_node = new_node
    else:
      self.last_node.next_node = new_node
      self.last_node = new_node

  def remove(self, data):
    current_node = self.first_node
    previous_node = None
    while current_node is not None:
      if current_node.data is data:
        #deleting list with one item
        if current_node is self.first_node and current_node is self.last_node:
          self.first_node = None
          self.last_node = None
        #deleting head
        elif current_node is self.first_node:
          self.first_node = current_node.next_node
        #deleting tail
        elif current_node is self.last_node:
          self.last_node = previous_node
          self.last_node.next_node = None
        #deleting in between
        else:
          previous_node.next_node = current_node.next_node
          current_node.next_node = None
        current_node = None
        break
 
      previous_node = current_node
      current_node = current_node.next_node

    return False



my_list = LinkedList()
my_list.append_to_tail('lip')
print(vars(my_list))
my_list.remove('lip')
print(vars(my_list))





