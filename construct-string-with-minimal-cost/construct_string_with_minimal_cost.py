class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.cost = None
        
    def append(self, s: str, cost:int):
        if not s:
            return
        node = self
        index = 0
        while True:
            if (index == len(s)):
                if node.cost == None:
                    node.cost = cost
                else:
                    node.cost = min(node.cost, cost)
                break
            c = s[index]
            lookup_index = ord(c) - ord('a')
            if node.children[lookup_index] == None:
                new_node = TrieNode()
                new_node.cost = cost
                node.children[lookup_index] = (s[index:], new_node)
                break
            else:
                unsplit_string, child_node = node.children[lookup_index]
                matching_length = 0
                while(matching_length < min(len(s) - index, len(unsplit_string))):
                    if s[index + matching_length] != unsplit_string[matching_length]:
                        break  
                    matching_length += 1
                if (matching_length == len(unsplit_string)):
                    node = child_node
                    index += matching_length
                else:   
                    node_extension = TrieNode()
                    string_right = unsplit_string[matching_length:]
                    c_right = string_right[0]
                    c_index = ord(c_right) - ord('a')
                    node_extension.children[c_index] = (string_right, child_node)
                    node.children[lookup_index] = (unsplit_string[:matching_length], node_extension)
                    node = node_extension
                    index += matching_length


    def get_costs(self, s:str, start_index:int):
        index = start_index
        node = self
        while(index < len(s)):
            child_index = ord(s[index]) - ord('a')
            child_value = node.children[child_index]
            if child_value == None:
                break
            child_string, child_node = child_value
            if child_string == s[index:index + len(child_string)]:
                node = child_node
                index += len(child_string)
                if (node.cost != None):
                    yield (index - start_index, node.cost) 
            else:
                break

def calculate_cost(target: str, root: TrieNode) -> int:
    dp = [None] * len(target)
    for length, cost in root.get_costs(target, 0):
        dp[length-1] = cost
    for i in range(1, len(target)):
        if dp[i-1] == None:
            continue
        if dp[-1] != None and dp[-1] <= dp[i-1]:
            continue
        for length, c in root.get_costs(target, i):
            index_to_set = i + length - 1
            if dp[index_to_set] == None:
                dp[index_to_set] = c + dp[i-1]
            else:
                dp[index_to_set] = min(dp[index_to_set], c + dp[i-1]) 
    return -1 if dp[-1] == None else dp[-1]



class Solution:
    def minimumCost(self, target: str, words: list[str], costs: list[int]) -> int:
        root = TrieNode()
        for w,c in sorted(zip(words,costs), key=lambda t:len(t[0])):
            existing_cost = calculate_cost(w, root)
            if (existing_cost == -1 or existing_cost > c):
                root.append(w, c)
            else:
                None
        return calculate_cost(target, root)
