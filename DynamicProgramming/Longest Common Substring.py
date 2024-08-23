class Solution:
    def longestCommonSubstring(self, text1, text2):
        rows = len(text1)
        cols = len(text2)

        self.D = [[0] * (cols+1) for _ in range(rows+1)]
        result = 0 

        for i in range(1,rows+1):
            for j in range(1,cols+1):
                if text1[i-1]==text2[j-1]:
                    self.D[i][j] = 1 + self.D[i-1][j-1] 
                    result = max(result, self.D[i][j])
                else:
                    self.D[i][j] = 0

        return result

text1 = "abcdefg"
text2 = "abcjdefg"

s = Solution()

print(s.longestCommonSubstring(text1,text2))    