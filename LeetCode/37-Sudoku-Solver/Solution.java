class Solution {
    public void solveSudoku(char[][] board) {
        int[] solved = new int[1]; // Array to track if the puzzle is solved
        solve(board, 0, 0, solved);
    }

    private void solve(char[][] board, int row, int col, int[] solved) {
        // If we've reached the end of the board, mark as solved
        if (row == board.length - 1 && col == board[0].length) {
            solved[0] = 1;
            return;
        }

        // Move to the next row if we've reached the end of the current row
        if (col == board[0].length) {
            solve(board, row + 1, 0, solved);
            return;
        }

        // If the cell is empty, try placing numbers 1-9
        if (board[row][col] == '.') {
            for (int num = 1; num <= 9; num++) {
                char candidate = (char) (num + '0'); // Convert number to character
                if (isValidPlacement(board, row, col, candidate)) {
                    board[row][col] = candidate; // Place the number
                    solve(board, row, col + 1, solved); // Proceed to the next cell
                    // Backtrack if not solved
                    if (solved[0] != 1) {
                        board[row][col] = '.';
                    }
                }
            }
        } else {
            // Move to the next cell if the current one is not empty
            solve(board, row, col + 1, solved);
        }
    }

    private boolean isValidPlacement(char[][] board, int row, int col, char num) {
        // Check the column
        for (int i = 0; i < 9; i++) {
            if (board[i][col] == num) {
                return false;
            }
        }

        // Check the row
        for (int i = 0; i < 9; i++) {
            if (board[row][i] == num) {
                return false;
            }
        }

        // Check the 3x3 sub-grid
        int subGridRowStart = (row / 3) * 3;
        int subGridColStart = (col / 3) * 3;
        for (int i = subGridRowStart; i < subGridRowStart + 3; i++) {
            for (int j = subGridColStart; j < subGridColStart + 3; j++) {
                if (board[i][j] == num) {
                    return false;
                }
            }
        }

        return true;
    }
}
