



def compressString(string):
  newString = ''
  count = 0

  for i in range(0, len(string)):
    
    if count == 0:
      newString += string[i]
      count += 1
    elif string[i] == string[i-1]:
      count += 1
    else:
      newString += str(count)
      newString += string[i]
      count = 1
    if i == len(string) - 1:
      newString += str(count)

  if len(newString) > len(string):
    return string

  return newString

print(compressString('aaabbbdddjjwk'))
