class Solution(object):
    def __init__(self) -> None:
        self.memo = {}

    def canSum(self, targetSum, numbers):

        if targetSum in self.memo:
            return self.memo[targetSum]
        
        if targetSum == 0: return True
        if targetSum < 0: return False

        for n in numbers:
            remainder = targetSum - n 
            if self.canSum(remainder, numbers)==True:
                self.memo[targetSum] = True
                return True
        
        self.memo[targetSum] = False
        return False

if __name__=='__main__':
    obj = Solution()
    numbers = [2,3,5]
    num = 19
    print(obj.canSum(num,numbers))

    
