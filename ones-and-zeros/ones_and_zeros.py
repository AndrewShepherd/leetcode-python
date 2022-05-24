import collections

def countOnesAndZeros(s):
    c = collections.Counter(s)
    return (c['0'], c['1'])

class Solution(object):
    def findMaxForm(self, strs, m, n):
        counts = [(c['0'], c['1']) for c in [collections.Counter(s) for s in strs]]

        grid = [[0]*(n+1) for i in range(m+1)]
        #for i in range(len(grid)):
        #    grid[i] = [0] * (n+1)

        for zeros, ones in counts:
            for r in range(m, zeros - 1, -1):
                for c in range(n, ones - 1, -1):
                    without = grid[r - zeros][c-ones]
                    grid[r][c] = max(grid[r][c], without+1)
        return grid[-1][-1]

        