class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
        /**
         * initialize row,col and block array
         * go through the sudoku and assign them into the array
         * if already found then return false
         */

        const rowArr =  Array.from({length: 9}, ()=>new Array(9).fill(false))
        const colArr =  Array.from({length: 9}, ()=>new Array(9).fill(false))
        const blockArr =  Array.from({length: 9}, ()=>new Array(9).fill(false))
        
        
        for(let r=0;r<9;r++){
            for(let c=0;c<9;c++){
                const cell = board[r][c]
                if(cell==='.') continue
                const cellNumber = parseInt(cell)-1
                const boxIndex = Math.floor(r/3)*3+Math.floor(c/3)
                if(rowArr[r][cellNumber]||colArr[c][cellNumber]||blockArr[boxIndex][cellNumber]){
                    return false
                }
                rowArr[r][cellNumber]=true
                colArr[c][cellNumber]=true
                blockArr[boxIndex][cellNumber]=true
            }
        }
        
        return true
    }
}
