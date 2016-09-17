from LinkedList import LinkedList

def find_loop_start(circular_list):
  visited_nodes = {}
  current_node = circular_list.head

  while current_node not in visited_nodes or current_node is None:

    visited_nodes[current_node] = True
    current_node = current_node.next_node

  return current_node

# for test
linked_list = LinkedList()

# filling the linked list
data = [4, 3, 2, 9, 5]
for value in data:
  linked_list.append_to_tail(value)

linked_list.tail.next_node = linked_list.head.next_node

# should return 2nd node
print(find_loop_start(linked_list))