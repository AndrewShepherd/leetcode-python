import heapq
from collections import defaultdict

ord_a = ord('a')

def to_index(c):
    return ord(c) - ord_a

class TrieNode:
    def __init__(self):
        self.child_nodes = [None] * 26
        self.can_terminate = False
    def add_substring(self, w):
        if len(w) == 0:
            self.can_terminate = True
        else:
            first_char = w[0]
            first_index = to_index(first_char)
            if self.child_nodes[first_index] == None:
                self.child_nodes[first_index] = w[1:]
            elif type(self.child_nodes[first_index]) == type(''):
                new_node = TrieNode()
                new_node.add_substring(self.child_nodes[first_index])
                new_node.add_substring(w[1:])
                self.child_nodes[first_index] = new_node
            else:
                self.child_nodes[first_index].add_substring(w[1:])

    def get_length(self, w):
        l = 0
        node = self
        for i,c in enumerate(w):
            c_index = to_index(c)
            child_node = node.child_nodes[c_index]

            if child_node == None:
                break
            elif type(child_node) == type(''):
                l += 1
                for child_node_index, word_index in zip(range(0, len(child_node)), range(i+1, len(w))):
                    if child_node[child_node_index] == w[word_index]: 
                        l += 1
                    else:
                        break
                break
            else:
                node = child_node
                l += 1
        return l

class Solution:
    def minValidStrings(self, words: list[str], target: str) -> int:
        root_node = TrieNode()
        for w in words:
            root_node.add_substring(w)

        q = [(0, 0)]
        maxes = defaultdict(lambda: len(target) + 1)
        while(q):
            cost, negative_index = heapq.heappop(q)
            index = 0 - negative_index
            l = root_node.get_length(target[index:])
            if l == len(target) - index:
                return cost + 1
            if cost+1 in maxes:
                start_index = maxes[cost+1] + 1
            else:
                start_index = index + 1
            for j in range(start_index, index+1+l):
                heapq.heappush(q, (cost + 1, 0 - j))
                maxes[cost+1] = j
        return -1
