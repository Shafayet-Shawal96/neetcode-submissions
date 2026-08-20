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

        let rows = new Array(9).fill(0);
        let cols = new Array(9).fill(0);
        let squares = new Array(9).fill(0);
        
        
        for(let r=0;r<9;r++){
            for(let c=0;c<9;c++){
                const cell = board[r][c]
                if(cell==='.') continue
                const cellNumber = parseInt(cell)-1
                const boxIndex = Math.floor(r/3)*3+Math.floor(c/3)
                const val = 1 << cellNumber
               
                if (
                    rows[r] & (val) ||
                    cols[c] & (val) ||
                    squares[boxIndex] &
                        (val)
                ) {
                    return false;
                }
                rows[r] |= val;
                cols[c] |= val;
                squares[boxIndex] |= val;
            }
        }
        
        return true
    }
}
