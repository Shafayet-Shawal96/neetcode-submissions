class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero = -1 
        product = 1
        size = len(nums)

        for i in range(size):
            if nums[i] == 0 and zero != -1:
                zero = -2
            elif nums[i] == 0:
                zero = i
            else:
                product *= nums[i]

        if zero == -2:
            return [0] * size
        elif zero != -1:
            result = [0] * size
            result[zero] = product
            return result
        
        result = [-1] * size
        for i in range(size):
            result[i] = round(product/nums[i])
            
        return result
