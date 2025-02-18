
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
  one = 0
  two = 0
  three = 0
  four = 0
  five = 0
  six = 0
  seven = 0
  eight = 0
  nine = 0
  zero = 0
  for row in sudoku:
    for item in row:
      if item == 1:
        one += 1
      if item == 2:
        two += 1
      if item == 3:
        three += 1
      if item == 4:
        four += 1
      if item == 5:
        five +=1
      if item == 6:
        six += 1
      if item == 7:
        seven += 1
      if item == 8:
        eight += 1
      if item == 9:
        nine +=1
      if item == 0:
        zero +=1
  if one == 1 and two == 1 and three == 1 and four == 1 and five == 1 and six == 1 and seven == 1 and eight == 1 and nine == 1 and zero ==1:
    return True
  else:
    return False

if __name__ == "__main__":
 print(row_correct(sudoku, 0))


# Sudoku: Check column:

def column_correct (sudoku:list,column_no:int):
  one = 0
  two = 0
  three = 0
  four = 0
  five = 0
  six = 0
  seven = 0
  eight = 0
  nine = 0
  zero = 0
  for row in sudoku:
    if row[0] == 0:
      zero += 1
    if row[1] == 1:
      zero += 1
    if row[0] == 2:
      zero += 1
    if row[0] == 3:
      zero += 1
    if row[0] == 0:
      zero += 1
    
      






