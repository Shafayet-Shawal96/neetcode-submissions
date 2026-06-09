class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = dict()

        for num in nums:
            if num in result.keys():
                result[num] += 1
            else:
                result[num] = 1

        sorted_result = list(dict(sorted(result.items(), key=lambda item: item[1], reverse=True)).keys())

        return sorted_result[:k]