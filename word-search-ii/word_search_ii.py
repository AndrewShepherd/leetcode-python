from collections import defaultdict

def remove_word(root_trie_node, word: str):
    l = [root_trie_node]
    for c in word:
        l.append(l[-1][c])
    end_node = l.pop()
    del end_node[0]
    while(len(l) != 0 and len(end_node) == 0):
        c = word[len(l) - 1]
        end_node = l.pop()
        del end_node[c]


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root_trie_node = dict()
        for w in words:
            node = root_trie_node
            for i,c in enumerate(w):
                if c not in node:
                    node[c] = dict()
                node = node[c]
                if i == len(w) - 1:
                    node[0] = True

        def get_adjacent_coordinates(coordinates):
            r,c = coordinates
            if r > 0:
                yield (r-1, c)
            if r < len(board) - 1:
                yield (r+1, c)
            if c > 0:
                yield (r, c - 1)
            if c < len(board[r]) - 1:
                yield (r, c + 1)


        result = []
        def solve_recursive(coordinates, trie_node, word_so_far, coordinates_taken):
            #print(f"solve_recursive {coordinates}, trie_node = {trie_node}, word_so_far =  '{word_so_far}', coordinates_taken = {coordinates_taken}")
            if 0 in trie_node:
                result.append(word_so_far)
                remove_word(root_trie_node, word_so_far)
            if not len(trie_node):
                return
            adjacent = [c for c in get_adjacent_coordinates(coordinates) if c not in coordinates_taken]

            for r, c in adjacent:
                #print(f"--- solving for {r}, {c}")
                character = board[r][c]
                if character in trie_node:
                    coordinates_taken.add((r, c))
                    solve_recursive((r, c), trie_node[character], word_so_far + character, coordinates_taken)
                    coordinates_taken.remove((r, c))
            
        #print(f"rootTrieNode = {root_trie_node}")
        for r, row in enumerate(board):
            for c in range(len(row)):
                character = board[r][c]
                if character in root_trie_node:
                    #print(f"Calling for {r}, {c}")
                    solve_recursive((r, c), root_trie_node[character], character, {(r,c),})

        return result
