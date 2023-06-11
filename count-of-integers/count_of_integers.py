MODULO = int(10**9) + 7

class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        num1 = [int(c) for c in num1]
        num2 = [int(c) for c in num2]
        num1 = [0]*(len(num2)-len(num1)) + num1


        def solve_recursive(num1: str, num2: str, min_sum: int, max_sum: int) -> int:
            if len(num1) == 0:
                return 1 if min_sum <= 0 <= max_sum else 0
            if max_sum < 0:
                return 0
            
            max_possible_sum = 9 * len(num1)
            if max_possible_sum < min_sum:
                return 0
            
            if min_sum <= 0 and max_possible_sum < max_sum and num1 == [0]*len(num1) and num2 == [9] * len(num2):
                return pow(10,len(num1), MODULO)


            if num1[0] == num2[0]:
                return solve_recursive(num1[1:], num2[1:], min_sum - num1[0], max_sum - num1[0])


            remaining_as_zeros = [0] * (len(num1) - 1)
            remaining_as_nines = [9] * (len(num1) - 1)

            # First n value
            # Is going to be n 00000-99999
            total = 0
            total += solve_recursive(num1[1:], remaining_as_nines, min_sum - num1[0], max_sum - num1[0])

            # The middle values
            for n2 in range(num1[0]+1, num2[0]):
                total += solve_recursive(remaining_as_zeros, remaining_as_nines, min_sum - n2, max_sum - n2)

            # ths last value
            total += solve_recursive(remaining_as_zeros, num2[1:], min_sum - num2[0], max_sum - num2[0])
            return total % MODULO
        
        return solve_recursive(num1, num2, min_sum, max_sum) % MODULO

    

