class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        /**
         * initialize hashmap
         * loop through the array the update the hashmap
         * then loop through the array again check if a element is the start of the seq
         * if start count the max seq
         * else update the result
         */

        const numsHash = {}
        for(let i=0;i<nums.length;i++){
            numsHash[nums[i]]=true
        }

        let result = 0
        for(let i=0;i<nums.length;i++){
            const isStart = this.checkStart(numsHash,nums[i])
            if(isStart){
                const countSeq = this.countTotalSeq(numsHash, nums[i])
                result = result>countSeq?result:countSeq
            }
        }

        return result
    }

    checkStart(numsHash, num){
        if(numsHash[num-1]) return false
        return true
    }

    countTotalSeq(numsHash, num){
        let count = 1
        let countNum = num
        while (numsHash[countNum+1]){
            count++
            countNum++
        }
        return count
    }
}
