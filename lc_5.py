class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        a = [[False]*n for _ in range(n)]
        ans = ""
        for l in range(n):
            for i in range(n):
                j = i + l
                if j >= n:
                    continue
                if l == 0:
                    a[i][j] = True
                elif l == 1:
                    a[i][j] = (s[i]==s[j])
                else:
                    a[i][j] = (a[i+1][j-1] and s[i]==s[j])
                if a[i][j] and l+1 > len(ans):
                    ans = s[i:j+1]
        return ans
