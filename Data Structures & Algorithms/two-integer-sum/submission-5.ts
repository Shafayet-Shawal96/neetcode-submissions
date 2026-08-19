class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        const arrayMap = new Map

        for(let i=0;i<nums.length;i++){
            const oppo = target-nums[i]
            if(arrayMap.has(oppo)){
                return [arrayMap.get(oppo),i]
            }
            arrayMap.set(nums[i],i)
        }

        return []
    }
}
