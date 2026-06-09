class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]
            
        # nums.sort()
        # i = 0 
        # j = len(nums) -1

        # while i<j:
        #     print(i,j,nums[i], nums[j], target)
        #     if nums[i]+nums[j] == target:
        #         return [i, j]

        #     if nums[i]+nums[j] > target:
        #         j-=1

        #     if nums[i]+nums[j] < target:
        #         i+=1

        