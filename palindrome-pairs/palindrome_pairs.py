from collections import defaultdict

class TrieNode:
    def __init__(self): 
        self.children = defaultdict(TrieNode)
        self.endIndex = None
        self.followedByPalindromes = list()

def isPalindrome(word, start, endExclusive):
    section = word[start:endExclusive]
    return section == section[::-1]
    l = start
    r = endExclusive - 1
    while (l <= r):
        if word[l] != word[r]:
            return False
        l += 1
        r -= 1
    return True

class Solution:
    def palindromePairs(self, words):
        rootNode = TrieNode()
        for i, word in enumerate(words):
            node = rootNode
            if isPalindrome(word, 0, len(word)):
                node.followedByPalindromes.append(i)
            for ci, c in reversed(list(enumerate(word))):
                node = node.children[c]
                if isPalindrome(word, 0, ci):
                    node.followedByPalindromes.append(i)
            node.endIndex = i

        result = []
        for i, word in enumerate(words):
            node = rootNode
            if isPalindrome(word, 0, len(word)) and node.endIndex != None:
                result.append((i, node.endIndex))
            for ci, c in enumerate(word):
                if c not in node.children:
                    node = None
                    break
                node = node.children[c]
                if isPalindrome(word, ci+1, len(word)) and node.endIndex != None:
                    result.append((i, node.endIndex))
            if node:
                result.extend((i, pIndex) for pIndex in node.followedByPalindromes)
        return [[l, r] for l,r in set(result) if l != r]
