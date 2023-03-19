class Solution:
    def beautifulSubsets(self, nums: list[int], k: int) -> int:
        
        def solve_recursively(index, nums_sofar):
            if index >= len(nums):
                return 1 if nums_sofar else 0
            n = nums[index]
            if n in nums_sofar:
                return solve_recursively(index+1, nums_sofar) * 2
            
            without = solve_recursively(index + 1, nums_sofar)
            _with = 0
            if not (n-k in nums_sofar or n+k in nums_sofar):
                c = nums_sofar.copy()
                c.add(n)
                _with = solve_recursively(index + 1, c)
            return without + _with
            
        return solve_recursively(0, set())
