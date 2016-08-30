from LinkedList import LinkedList

def delete_middle_node(node):
  while node.next_node is not None:
    
    node.data = node.next_node.data
    #delete the resulting duplicate tail
    if node.next_node.next_node is None:
      node.next_node = None
    else:
      node = node.next_node


linked_list = LinkedList()
# filling the linked list
data = [4, 3, 2, 9, 5]
for value in data:
  linked_list.append_to_tail(value)

delete_middle_node(linked_list.head)
print(linked_list)