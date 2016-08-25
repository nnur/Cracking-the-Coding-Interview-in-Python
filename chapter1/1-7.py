m = 4
n = 3

testMatrix = [[2]*n for i in range(0, m)]
testMatrix[2][2] = 0

# the expected result from testMatrix
expectedMatrix = [
  [2, 2, 0], 
  [2, 2, 0], 
  [0, 0, 0], 
  [2, 2, 0]
]

def findZeroLocations(matrix):
  zeroLocations = []
  for y, row in enumerate(matrix):
    for x in range(len(row)):
      if row[x] == 0:
        zeroLocations.append([x, y])
  return zeroLocations


def setToZeroes(matrix):
  zeroLocations = findZeroLocations(matrix)
  for coordinate in zeroLocations:
    for x in range(0, n):
      matrix[coordinate[1]][x] = 0
    for y in range(0, m):
      matrix[y][coordinate[0]] = 0
  return matrix



result = setToZeroes(testMatrix)
print(result)
print(expectedMatrix)

if result == expectedMatrix:
  print('success!')



