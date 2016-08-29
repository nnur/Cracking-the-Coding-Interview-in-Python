from LinkedList import LinkedList

linked_list = LinkedList()

data = [4, 3, 2, 4 ]

# filling the linked list
for value in data:
  linked_list.append_to_tail(value)

def remove_duplicates(linked_list):
  current_node = linked_list.head
  temp_buffer = []

  while current_node is not None: 
    temp_buffer.append(current_node.data)
    current_node = current_node.next_node

  temp_set = set(temp_buffer)

  unique_list = LinkedList()

  for value in temp_set:
    unique_list.append_to_tail(value)

  linked_list.head = unique_list.head
  linked_list.tail = unique_list.tail

print(linked_list)
remove_duplicates(linked_list)
print(linked_list)


# remove duplicates without a buffer

def remove_duplicates_no_buffer(linked_list):
  current_node = linked_list.head
  another_node = current_node.next_node

  while current_node.next_node is not None:
    if current_node.data == another_node.data:
      linked_list.remove(current_node.data)
      current_node = linked_list.head
      another_node = current_node.next_node
    elif another_node.next_node == None:
      current_node = current_node.next_node
      another_node = current_node.next_node
    else:
      another_node = another_node.next_node

# print(linked_list)
# remove_duplicates_no_buffer(linked_list)
# print(linked_list)