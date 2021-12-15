def valid_row(row, grid):
  temp = grid[row]
  temp = list(filter(lambda a: a != 0, temp))
  if any(i < 0 and i > 9 for i in temp):
    print("Invalid value")
    return -1
  elif len(temp) != len(set(temp)):
    return 0
  else:
    return 1
  
def valid_col(col, grid):
  temp = [row[col] for row in grid]
  temp = list(filter(lambda a: a != 0, temp))
  if any(i < 0 and i > 9 for i in temp):
    print("Invalid value")
    return -1
  elif len(temp) != len(set(temp)):
    return 0
  else:
    return 1

def valid_subsquares(grid):
  for row in range(0, 9, 3):
      for col in range(0,9,3):
         temp = []
         for r in range(row,row+3):
            for c in range(col, col+3):
              if grid[r][c] != 0:
                temp.append(grid[r][c])
         if any(i < 0 and i > 9 for i in temp):
             print("Invalid value")
             return -1
         elif len(temp) != len(set(temp)):
             return 0
  return 1

def valid_board(grid):
    for i in range(9):
        res1 = valid_row(i, grid)
        res2 = valid_col(i, grid)
        if (res1 < 1 or res2 < 1):
            return False
    res3 = valid_subsquares(grid)
    if (res3 < 1):
        return False
    else:
        return True
      
