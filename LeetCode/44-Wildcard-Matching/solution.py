class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        lenP, lenS = len(p), len(s)
        
        dp = [[False for j in range(lenP + 1)] for i in range(lenS + 1)]
        dp[0][0] = True

        for j in range(1, lenP + 1):
            if p[j - 1] == '*':
                dp[0][j] = True
            else:
                break

        for i in range(1, lenS + 1):
            for j in range(1, lenP + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                else:
                    dp[i][j] = (s[i - 1] == p[j - 1] or p[j - 1] == '?') and dp[i - 1][j - 1]
        
        return dp[lenS][lenP]