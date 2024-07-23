class TrieNode:

    def __init__(self):
        self.children = dict()
        self.cost = None
        
    def append(self, s: str, cost:int):
        if not s:
            return
        node = self
        for c in s:
            if c in node.children:
                node = node.children[c]
            else:
                new_node = TrieNode()
                node.children[c] = new_node
                node = new_node
        node.cost = cost if node.cost == None else min(cost, node.cost)

    def get_costs(self, s:str):
        node = self
        for i,c in enumerate(s):
            if c not in node.children:
                break
            node = node.children[c]
            if (node.cost != None):
                yield (i+1, node.cost)

class Solution:
    def minimumCost(self, target: str, words: list[str], costs: list[int]) -> int:
        root = TrieNode()
        for w,c in zip(words,costs):
            root.append(w, c)
        dp = [None] * len(target)
        for length, cost in root.get_costs(target):
            dp[length-1] = cost
        for i in range(1, len(target)):
            if dp[i-1] == None:
                continue
            for length, c in root.get_costs(target[i:]):
               index_to_set = i + length - 1
               if dp[index_to_set] == None:
                   dp[index_to_set] = c + dp[i-1]
               else:
                   dp[index_to_set] = min(dp[index_to_set], c + dp[i-1]) 
        return -1 if dp[-1] == None else dp[-1]
