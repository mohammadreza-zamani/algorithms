class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        lenP, lenS = len(p), len(s)

        if lenS == 0 and lenP == 0:
            return True
        
        if (lenP == 0 and lenS > 0) or (lenP >= 1 and p[lenP - 1] != '*' and lenS == 0):
            return False

        if lenS == 0 and lenP > 1 and p[lenP - 1] == '*':
            return self.isMatch(s, p[0 : lenP - 2])
        
        if p[lenP - 1] == '.' or s[lenS - 1] == p[lenP - 1]:
            return self.isMatch(s[0 : lenS - 1], p[0 : lenP - 1])
        
        if lenP > 1 and p[lenP - 1] == '*':
            if s[lenS - 1] == p[lenP - 2] or p[lenP - 2] == '.':
                return self.isMatch(s[0 : lenS - 1], p[0 : lenP - 2]) or self.isMatch(s[0 : lenS - 1], p) or self.isMatch(s, p[0 : lenP - 2])
            else:
                return self.isMatch(s, p[0 : lenP - 2])
        
        return False