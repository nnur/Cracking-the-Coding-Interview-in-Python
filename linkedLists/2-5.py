from LinkedList import LinkedList


def add_linked_lists(list1, list2):
  list3 = LinkedList()

  p1 = list1.head
  p2 = list2.head
  numbers_to_add = []
  position = 0
  while True:
    if p2 and p1:
      numbers_to_add.append(p1.data*10**position + p2.data*10**position)
      p2 = p2.next_node
      p1 = p1.next_node
    elif p1: # if p2 is the shorter number
      numbers_to_add.append(p1.data*10**position)
      p1 = p1.next_node
    elif p2: 
      numbers_to_add.append(p2.data*10**position)
      p2 = p2.next_node
    else:
      break

    position += 1
  
  return create_sum_list(numbers_to_add)


def create_sum_list(numbers_to_add):
  sum_ = 0
  for number in numbers_to_add:
    sum_ += number
  str_sum = str(sum_)
  backward_number_list = [int(i) for i in str_sum[::-1]]

  result_list = LinkedList()
  for number in backward_number_list:
    result_list.append_to_tail(number)
  return result_list


#testing

list1 = LinkedList()
list2 = LinkedList()

# filling the linked list
data2 = [7, 1]
data1 = [5, 9, 8]

for value in data2:
  list2.append_to_tail(value)
for value in data1:
  list1.append_to_tail(value)

print(add_linked_lists(list1, list2))
