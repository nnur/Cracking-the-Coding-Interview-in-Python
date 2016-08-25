myword = 'meow hap'

dictionary = {}


def hasUniqueChars(word):
  for i in range(0, len(word)):
    char = word[i]
    if char not in dictionary:
      dictionary[char] = 0
    else:
      return 'bad'

  return 'good'

print(hasUniqueChars(myword))