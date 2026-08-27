class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let result = ''

        for(let i=0;i<s.length;i++){
            result+=this.getConvertedCharacter(s[i])
        }
    
        let i = 0
        let j = result.length-1

        while(i<=j){
            if(result[i]!==result[j])return false
            i++
            j--
        }

        return true
    }

    getConvertedCharacter(c){
        const code = c.charCodeAt(0)

        if((code > 47 && code < 58) ||  (code > 96 && code < 123)) return c
        if(code > 64 && code < 91) return c.toLowerCase()
        return ''
    }
}
