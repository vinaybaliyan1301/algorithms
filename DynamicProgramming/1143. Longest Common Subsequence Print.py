#https://www.youtube.com/watch?v=x5hQvnUcjiM
class Solution:
    
    def longestCommonSubsequencePrint(self, text1, text2):
        rows = len(text1)
        cols = len(text2)

        self.D = [[0] * (cols+1) for _ in range(rows+1)]

        for i in range(1,rows+1):
            for j in range(1,cols+1):
                if text1[i-1]==text2[j-1]:
                    self.D[i][j] = 1 + self.D[i-1][j-1] 
                else:
                    self.D[i][j] = max(self.D[i-1][j], self.D[i][j-1])


        i = rows
        j = cols

        ans = ""
        
        while i != 0 or j !=0:
            if text2[j-1] == text1[i-1]:
                ans += text2[j-1]
                i-=1
                j-=1
                continue 
                
            if self.D[i-1][j] > self.D[i][j-1]:
                i-=1
            else:
                j-=1
        
        return ans[::-1]

if __name__=="__main__":
    text1 = "acbcf"
    text2 = "abcdaf"
    n = len(text1)
    m = len(text2)

    s = Solution()

    print(s.longestCommonSubsequencePrint(text1,text2))    
