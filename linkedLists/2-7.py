from LinkedList import LinkedList

def isPallindrome(linked_list):
  current_node = linked_list.head
  values = ''
  while current_node is not None:
    values += str(current_node.data)
    current_node = current_node.next_node

  return values == values[::-1]


# for test
pallindrome = LinkedList()
not_pallindrome = LinkedList()


# filling the linked list
data = ['r', 'a', 'd', 'i', 'o']
for value in data:
  not_pallindrome.append_to_tail(value)

data = ['r', 'a', 'd', 'a', 'r']
for value in data:
  pallindrome.append_to_tail(value)

print(isPallindrome(not_pallindrome)) # prints false
print(isPallindrome(pallindrome)) # prints true

