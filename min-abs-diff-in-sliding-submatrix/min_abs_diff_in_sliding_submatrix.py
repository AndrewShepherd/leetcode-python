def iterateThroughPoints(rows, cols, k):
   for r in range(0, rows + 1 - k, 1):
      for c in range(0, cols + 1 - k, 1):
         yield (r, c)
      
def getDistinctNumbers(grid, start_row, start_col, k):
   s = set()
   for r in range(start_row, start_row + k):
      for c in range(start_col, start_col + k):
         s.add(grid[r][c])
   return sorted(list(s))

def getMinDifference(l):
  if len(l) == 1:
    return 0
  m = 300001
  for i in range(1, len(l)):
    m = min(m, abs(l[i] - l[i-1]))
  return m
  

class Solution:
    def minAbsDiff(self, grid: list[list[int]], k: int) -> list[list[int]]:
      result = [[0] * (len(grid[0])-k+1) for _ in range(len(grid)-k+1)]
      for (r,c) in iterateThroughPoints(len(grid), len(grid[0]), k):
         dn = getDistinctNumbers(grid, r, c, k)
         result[r][c] = getMinDifference(dn)
      return result
