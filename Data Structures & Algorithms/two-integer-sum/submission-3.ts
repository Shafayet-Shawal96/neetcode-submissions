class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        const indics={}

        for(let i=0; i<nums.length; i++){
            const complementNum = target-nums[i]
            if(indics[complementNum]!==undefined && indics[complementNum]!=i){
                return i>indics[complementNum]? [indics[complementNum],i]:[i,indics[complementNum]]
            }
            indics[nums[i]]=i
        }

        return [0,1]
    }
}
