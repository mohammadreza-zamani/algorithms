class Solution:
    def longestPalindrome(self, s: str) -> str:
        lenS = len(s)
        dp = [[j <= i for j in range(lenS)] for i in range(lenS)]

        maxPalndromLen = bestI = bestJ = 0

        for gap in range(1, lenS):
            for i in range(lenS - 1):
                j = i + gap
                if j >= lenS:
                    break

                if s[i] == s[j] and (dp[i + 1][j - 1] or gap == 1):
                    dp[i][j] = True
                    if gap > maxPalndromLen:
                        maxPalndromLen = gap
                        bestI = i
                        bestJ = j
        
        return s[bestI : bestJ + 1]
