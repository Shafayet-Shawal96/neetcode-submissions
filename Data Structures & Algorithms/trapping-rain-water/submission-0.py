class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]

        while l<r:
            if height[l] < height[r]:
                l = l + 1
                result += max(maxL-height[l],0)

                if height[l] > maxL:
                    maxL = height[l]

            else:
                r = r - 1
                result += max(maxR-height[r],0)

                if height[r] > maxR:
                    maxR = height[r]

        return result