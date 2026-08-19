class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs: string[]): string[][] {
        /*
        - initialized a map
        - loop through strs
        - get a single str
        - convert it to arraystring
        - create or get the stored array
        - add it map as key:arraystring value:array
        - return loop through the array
        */
        const result = new Map

        for(let i=0;i<strs.length;i++){
            const str = strs[i]
            const arrayString = this.getArrayString(str)
            const temp = result.get(arrayString) || []
            temp.push(str)
            result.set(arrayString,temp)
        }

        return [...result.values()]
    }

    getArrayString(str: string): string{
        const strArr = new Array(26).fill(0)

        for(let i=0;i<str.length;i++){
            strArr[str.charCodeAt(i)-'a'.charCodeAt(0)]++
        }

        return strArr.join(',')
    }
}
