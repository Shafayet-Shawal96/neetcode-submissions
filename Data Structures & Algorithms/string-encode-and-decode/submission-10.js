class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        /*
        - initialize result string
        - loop through array
        - get the size of the string
        - store in result with # in the middle
        */

        let result = ''
        for(const str of strs){
            const size = str.length
            result += size+'#'+str
        }

        return result
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        // if(str==='') return [""]

        const result = []
        
        let l = 0
        let r = 1 
        while(r<str.length){
            if(str[r]==='#'){
                const len = parseInt(str.slice(l,r))
                result.push(str.slice(r+1,r+len+1))
                l = r+len+1 
                r = r+len+2
            } else {
                r++
            }
        }
        return result
    }
}
