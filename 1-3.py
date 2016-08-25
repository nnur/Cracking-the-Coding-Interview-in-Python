word1 = 'nailaa'
word2 = 'alian'
dictionary1 = {}
dictionary2 = {}

def isPermutation(word1, word2):
  if len(word1) != len(word2):
    return 'not permutation'

  for i in range(0, len(word1)):
    if word1[i] not in dictionary1:
      dictionary1[word1[i]] = 0
    else:
      dictionary1[word1[i]] += 1

    if word2[i] not in dictionary2:
      dictionary2[word2[i]] = 0
    else:
      dictionary2[word2[i]] += 1

  if dictionary2 != dictionary1:
    return 'not permutation'
  else:
    return 'permutation'

print(isPermutation(word1, word2))