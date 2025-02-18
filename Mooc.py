
# Go
def who_won (game_board:list):
  p1 = 0
  p2 = 0
  for row in game_board:
    for column in row:
      if column == 1:
        p1 += 1
      elif column == 2:
        p2 += 1
    if p1 > p2:
      return 1
    if p2 > p1:
      return 2
    else:
      return 0
      
if __name__ == "__main__":
  who_won (whatever)


# Sudoku: check row

def row_correct (sudoku:list, row_no:int):
  row = sudoku [row_no]
  numbers = [num for num in row if num != 0]
  return len(numbers) == len(set(numbers))

if __name__ == "__main__":
 print(row_correct(sudoku, 0))


# Sudoku: Check column:

def column_correct (sudoku:list,column_no:int):
  column = [row[column_no] for row in sudoku]
  numbers = [num for num in column if num != 0]
  return len(numbers) == len(set(numbers))
    
# Sudoku: check block:

def block_correct (sudoku: list, row_no:int, column_no:int):
  numbers = []
  for i in range(3):
    for j in range (3):
      num = sudoku[row_no+i][column_no+j]
      if num != 0:
        if num in numbers:
          return False
        numberrs.append(num)
  return True

if __name__ == "__main__":
  print(block_correct(sudoku, 0, 0))


#Sudoku: check grid:

def sudoku_grid_correct (sudoku:list):
  if row_correct () == True and column_correct () == True and block_correct () == True:
    return True
  else:
    return False

if __name__ == "__main__":
  sudoku1 = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

print(sudoku_grid_correct(sudoku1))








