n = 5
mmatrix = [[0]*n for i in range(n)]
newMatrix = [[0]*n for i in range(n)]
#print(matrix)
def rotateMatrix(matrix):
  for x, row in enumerate(reversed(matrix)):
    for y in range(0, n):
      newMatrix[y][x] = row[y]
  return newMatrix


test = [
[1, 1, 1, 1, 1], 
[2, 2, 2, 2, 2], 
[0, 0, 0, 0, 3], 
[0, 0, 0, 0, 4], 
[0, 0, 0, 0, 5]
]


rotatedTest = [
[0, 0, 0, 2, 1], 
[0, 0, 0, 2, 1], 
[0, 0, 0, 2, 1], 
[0, 0, 0, 2, 1], 
[5, 4, 3, 2, 1]
]


[
[1, 2, 0, 0, 0], 
[1, 2, 0, 0, 0], 
[1, 2, 0, 0, 0], 
[1, 2, 0, 0, 0], 
[1, 2, 3, 4, 5]
]


print(rotateMatrix(test))

if rotateMatrix(test) == rotatedTest:
  print('success')