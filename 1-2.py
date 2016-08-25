word = 'hello'

def recursiveReverse(testword):
  if testword == '':
    return ''
  else:
    return testword[-1] + recursiveReverse(testword[0:-1])


print(recursiveReverse(word))


