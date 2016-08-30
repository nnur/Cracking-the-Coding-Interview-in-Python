from LinkedList import LinkedList

def sort_by_value(x, linked_list):
  current_node = linked_list.head
  while current_node is not None:
    if current_node.data >= x:
      linked_list.append_to_tail(current_node.data)
      linked_list.remove(current_node.data) #removes only the first occurance
    current_node = current_node.next_node


linked_list = LinkedList()
# filling the linked list
data = [5, 9, 2, 6, 4]
for value in data:
  linked_list.append_to_tail(value)

sort_by_value(5, linked_list)
print(linked_list)