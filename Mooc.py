
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






