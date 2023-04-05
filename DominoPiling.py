def maxNumOfDominos(m, n):
  board_size = m*n
  return (board_size - (board_size % 2)) / 2

print(maxNumOfDominos(3, 3))