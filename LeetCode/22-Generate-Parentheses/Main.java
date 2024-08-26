import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        backtrack(result, n, 0, 0, "");
        return result;
    }
    
    private void backtrack(List<String> result, int maxPairs, int openCount, int closeCount, String current) {
        // If the current string has reached the maximum length, add it to the result.
        if (current.length() == maxPairs * 2) {
            result.add(current);
            return;
        }

        // Add an open parenthesis if we haven't used all of them yet.
        if (openCount < maxPairs) {
            backtrack(result, maxPairs, openCount + 1, closeCount, current + "(");
        }

        // Add a close parenthesis if it won't create an imbalance.
        if (closeCount < openCount) {
            backtrack(result, maxPairs, openCount, closeCount + 1, current + ")");
        }
    }
}