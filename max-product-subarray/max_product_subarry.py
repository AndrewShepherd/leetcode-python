class Solution:
    def maxProduct(self, nums):
        
        
        min_product_end_at_i = nums[0]
        max_product_end_at_i = nums[0]
        
        max_product_so_far = nums[0]
        
        for i in range(1,len(nums)):
            
            past_min_product_end_at_i, past_max_product_end_at_i =  min_product_end_at_i, max_product_end_at_i
            
            min_product_end_at_i = min(
                nums[i],
                past_min_product_end_at_i * nums[i],
                past_max_product_end_at_i * nums[i]
            )
            
            max_product_end_at_i = max(
                nums[i],
                past_min_product_end_at_i * nums[i],
                past_max_product_end_at_i * nums[i]
            )
            
            max_product_so_far = max(
                max_product_so_far,
                min_product_end_at_i,
                max_product_end_at_i
            )
            
            #print(min_product_end_at_i, max_product_end_at_i)
        
        
        return max_product_so_far