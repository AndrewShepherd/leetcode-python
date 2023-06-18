BEGINNING = 1
CONVERTING = 2

class Solution:
    def smallestString(self, s: str) -> str:
        as_numbers = [ord(c) for c in s]
        state = BEGINNING
        for i,n in enumerate(as_numbers):
            if n == ord('a'):
                if state == CONVERTING:
                    break
            else:
                if state == BEGINNING:
                    state = CONVERTING
                as_numbers[i] = n-1
        if state == BEGINNING:
            as_numbers[-1] = ord('z')
        return ''.join([chr(n) for n in as_numbers])
            
            
