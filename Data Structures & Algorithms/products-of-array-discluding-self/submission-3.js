class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        /**
         * initialize prefix and suffix array
         * loop through and set prefix array and suffix array
         * loop through the result and set by multiplying prefix and suffix of that position
         */
        const result = new Array(nums.length).fill(1)

        let mul = 1
        for(let i=0;i<nums.length-1;i++){
            mul=mul*nums[i]
            result[i+1]=mul
        }
    
        mul = 1
        for(let i=nums.length-1;i>0;i--){
            mul = mul*nums[i]
            result[i-1]*=mul
        }

        return result
    }
}
