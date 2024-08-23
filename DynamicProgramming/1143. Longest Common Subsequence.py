class Solution:
    
    def longestCommonSubsequence(self, text1, text2):
        rows = len(text1)
        cols = len(text2)

        self.D = [[0] * (cols+1) for _ in range(rows+1)]

        for i in range(1,rows+1):
            for j in range(1,cols+1):
                if text1[i-1]==text2[j-1]:
                    self.D[i][j] = 1 + self.D[i-1][j-1] 
                else:
                    self.D[i][j] = max(self.D[i-1][j], self.D[i][j-1])


        return self.D[rows][cols]
 
    # recursion without DP
    def __init__(self, n, m) -> None:
        rows = len(text1)
        cols = len(text2)

        self.D = [[-1] * (cols+1) for _ in range(rows+1)]

    def LCS(self, text1, text2, n, m): # recursion with DP
        rows = len(text1)
        cols = len(text2)

        if n == 0 or m == 0:
            return 0 

        if self.D[n][m] != -1:
            return self.D[n][m]
        
        if text1[-1] == text2[-1]:
            self.D[n][m] = 1 + self.LCS(text1[:n-1], text2[:m-1], n-1, m-1)
            return self.D[n][m]
        else:
            self.D[n][m] = max(self.LCS(text1[:n], text2[:m-1], n, m-1), self.LCS(text1[:n-1], text2[:m], n-1, m))
            return self.D[n][m]

if __name__=="__main__":
    text1 = "abcdef"
    text2 = "acea"
    n = len(text1)
    m = len(text2)

    s = Solution(n,m)

    print(s.LCS(text1,text2,n,m))
    #print(s.longestCommonSubsequence(text1,text2))    
