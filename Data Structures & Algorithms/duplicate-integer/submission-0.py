class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = dict()
        for num in nums:
            if(num in a.keys()):
                return True

            a[num] = 1

        return False
         