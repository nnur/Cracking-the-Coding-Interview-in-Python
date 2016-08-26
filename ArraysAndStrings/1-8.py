def isSubstring(stringPart, stringWhole):
  return stringPart in stringWhole

# test strings
string1 = 'waterbottle'
string2 = 'erbottlewat'

# solution 1
def isRotation(s1, s2):

  if len(s1) != len(s2):
    return False
  if s1 == s2:
    return True

  elif set(s1) != set(s2):
    return False

  for i, char in enumerate(s2):
    if s2[0:i] not in s1:
      part2 = s2[0:i-1]
      part1 = s2[i-1: len(s2)]

      return isSubstring(part1, s1)

# solution 2
def isRotation2(s1, s2):

  if len(s1) != len(s2):
    return False

  elif set(s1) != set(s2):
    return False

  for x, char in enumerate(s2):
    rotatedString = s2[x: len(s2)]
    rotatedString += s2[0: x]
    if rotatedString == s1:
      return True
  return False

# solution 3 :D
def isRotation3(s1, s2):
  doubleString = s1 + s1
  return isSubstring(s2, doubleString)



print(isRotation3(string1, string2))