from functools import cache
from collections import Counter

class Solution:
    
    
    def shortestPalindrome(self, s: str) -> str:
        as_list = [(s[0], 1)]
        for i in range(1, len(s)):
            c = s[i]
            if c == as_list[-1][0]:
                as_list[-1] = (c, as_list[-1][1] + 1)
            else:
                as_list.append((c, 1))
        
        def is_palindrome(iStart, iEndExclusive):
            return iEndExclusive <= iStart or as_list[iStart:iEndExclusive] == as_list[iEndExclusive-1:iStart-1:-1]

        def find_candidate(less_than):
            first_char, first_count = as_list[0]
            while(less_than > 0):
                less_than -= 1
                this_char, this_count = as_list[less_than]
                if this_char == first_char and this_count >= first_count:
                    return less_than
            raise Exception("Should never have got here")
        
        end_index = len(as_list)
        while end_index >= 0:
            end_index = find_candidate(end_index)
            if is_palindrome(1, end_index):
                n = sum([count for c,count in as_list[:end_index]]) + as_list[0][1]
                post_fix = s[n:]
                return post_fix[::-1] + s 
        

        

            

