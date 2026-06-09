class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        buckets = [None]*(len(nums)+1)

        for n in nums:
            counts[n] = counts.get(n,0)+1

        for key in counts.keys():
            count = counts[key]
            if buckets[count] is None:
                buckets[count] = [key]
            else:
                buckets[count].append(key)

        result = []
        for c in buckets[::-1]:
            if len(result) >= k:
                    break
            if c is None:
                continue
            else:
                for num in c:
                    if len(result) >= k:
                        break
                    else:
                        result.append(num)

        return result
