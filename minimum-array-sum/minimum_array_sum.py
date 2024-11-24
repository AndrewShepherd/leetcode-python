class Solution:
    def minArraySum(self, nums: list[int], k: int, op1: int, op2: int) -> int:
        nums_plus_records = [(n, True, True) for n in nums]
        nums_plus_records.sort(reverse=True)

        # for every item that is >= k*2, use up op1

        for i,(n, can_apply_op1, can_apply_op2) in enumerate(nums_plus_records):
            if op1 == 0:
                break
            if (n+1) < k*2:
                break
            nums_plus_records[i] = ((n+1)//2, False, can_apply_op2)
            op1 -= 1

        nums_plus_records.sort()

        # for every item that is >= k and will be even after subtracting k, us up op2
        for i,(n, can_apply_op1, can_apply_op2) in enumerate(nums_plus_records):
            if op2 == 0:
                break   
            if (n < k):
                continue
            if (n-k) % 2 == 1:
                continue
            if not can_apply_op2:
                continue
            nums_plus_records[i] = (n-k, can_apply_op1, False)
            op2 -= 1
        
        nums_plus_records.sort()
        # for every item that is >= k, us up op2
        for i,(n, can_apply_op1, can_apply_op2) in enumerate(nums_plus_records):
            if op2 == 0:
                break   
            if not can_apply_op2:
                continue
            if (n < k):
                continue
            if not can_apply_op2:
                continue
            nums_plus_records[i] = (n-k, can_apply_op1, False)
            op2 -= 1

        nums_plus_records.sort(reverse = True)
        # for every item that has not used up op1, use up op1
    
        for i,(n, can_apply_op1, can_apply_op2) in enumerate(nums_plus_records):
            if op1 == 0:
                break
            if not can_apply_op1:
                continue
            nums_plus_records[i] = ((n+1)//2, False, can_apply_op2)
            op1 -= 1




   
        return sum([n for n,b1,b2 in nums_plus_records])
        
