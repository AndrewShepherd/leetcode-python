def solveDp(coins, amount):
    counts = [0] + [-1] * amount
    for coin in coins:
        for i, c in enumerate(counts):
            newValue = i + coin
            if newValue >= len(counts):
                break
            if c == -1:
                continue
            newCount = c + 1
            if counts[newValue] == -1 or counts[newValue] > newCount:
                counts[newValue] = newCount
    return counts[amount]


def solveShortestPath(coins, amount):
    visited = [False] * amount
    q = [0]
    ans = 0
    while q:
        ans += 1
        q2, q = q, []
        for n in q2:
            if visited[n]:
                continue
            for c in coins:
                if n + c == amount:
                    return ans
                if n + c > amount:
                    continue
                if visited[n + c]:
                    continue
                q.append(n + c)
            visited[n] = True
    return -1

class Solution(object):
    def coinChange(self, coins, amount):
        return solveShortestPath(coins, amount)
        #return solveDp(coins, amount)