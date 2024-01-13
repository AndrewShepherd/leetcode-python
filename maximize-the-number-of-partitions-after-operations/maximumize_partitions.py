from functools import cache

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        if k == 26:
            return 1
        


        s = [ord(c) - ord('a') for c in s]


        @cache
        def calculate_score(start_index):
            distinct = set()
            partitions = 0
            for c in s[start_index:]:
                if not distinct:
                    partitions += 1
                if (c not in distinct):
                    if len(distinct) == k:
                        partitions += 1
                        distinct = { c }
                    else:
                        distinct.add(c)
            return partitions
        
        @cache
        def calculate_score_with_substitution(start_index):
            distinct = set()
            first_appearances = [None] * 26
            first_duplicated_item_index = [None]
            for i in range(start_index, len(s)):
                c = s[i]
                if c in distinct:
                    if first_duplicated_item_index == None:
                        first_duplicated_item_index = first_appearances[c]
                        if len(distinct) == k:
                            return 1 + calculate_score(start_index)
                else:
                    if len(distinct) == k - 1 and first_duplicated_item_index != None:
                        first_appearances[c] = i
                    if len(distinct) == k - 1 and first_duplicated_item_index != None:
                        return 1 + calculate_score(start_index)
                    if len(distinct) == k:
                        return 1 + calculate_score_with_substitution(start_index)
                    distinct.add(c)
            return 1
                


        return calculate_score_with_substitution(0)
        
