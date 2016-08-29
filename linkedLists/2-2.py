from LinkedList import LinkedList


def find_from_last(k, linked_list):
  current_node = linked_list.head
  data_buffer = []

  while current_node is not None:
    data_buffer.append(current_node)
    current_node = current_node.next_node

  position = len(data_buffer) - k
  return data_buffer[position]


# for test
linked_list = LinkedList()

# filling the linked list
data = [4, 3, 2, 9, 5]
for value in data:
  linked_list.append_to_tail(value)

# prints 9
print(find_from_last(2, linked_list))