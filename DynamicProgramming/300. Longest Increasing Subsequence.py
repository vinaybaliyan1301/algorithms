class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        
        self.D = [1] * len(nums)

        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    self.D[i] = max(self.D[i], self.D[j]+1)
        
        print(self.D)

        return max(self.D)
    
if __name__=="__main__":
    s= Solution()
    nums = [10,9,2,5,3,7,101,18]
    print(s.lengthOfLIS(nums))
