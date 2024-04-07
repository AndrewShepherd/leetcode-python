class TrieNode:
    def __init__(self):
        self.sub_nodes = [None] * 26
        self.best_result = None

    def add(self, index, value, value_index):
        if self.best_result == None:
            self.best_result = (index, value)
        else:
            my_best_index, my_best_value = self.best_result
            if len(value) < len(my_best_value):
                self.best_result = (index, value)
        if(value_index < 0):
            return
        c = value[value_index]
        i = ord(c) - ord('a')
        if self.sub_nodes[i] == None:
            self.sub_nodes[i] = TrieNode()
        self.sub_nodes[i].add(index, value, value_index-1)

    def lookup(self, value, value_index):
        if(value_index < 0):
            return self.best_result[0]
        c = value[value_index]
        i = ord(c) - ord('a')
        if self.sub_nodes[i] == None:
            return self.best_result[0]
        else:
            return self.sub_nodes[i].lookup(value, value_index-1)
    

class Solution:
    def stringIndices(self, wordsContainer: list[str], wordsQuery: list[str]) -> list[int]:
        rootNode = TrieNode()
        for i,v in enumerate(wordsContainer):
            rootNode.add(i, v, len(v)-1)
        result = []
        for q in wordsQuery:
            best_result = rootNode.lookup(q, len(q)-1)
            result.append(best_result)
        return result
