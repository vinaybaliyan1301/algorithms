class Solution(object):
    def __init__(self) -> None:
        self.memo = {}

    def howSum(self, targetSum, numbers):

        if targetSum in self.memo:
            return self.memo[targetSum]
        
        if targetSum == 0: return []
        
        for num in numbers:
            remainder = targetSum - num 
            if remainder >=0:
                result = self.howSum(remainder, numbers)
                if result is not None:
                    self.memo[targetSum] = result + [num]
                    return self.memo[targetSum]
        
        self.memo[targetSum] = None
        return None

if __name__=='__main__':
    obj = Solution()
    numbers = [2,3,5]
    num = 5
    print(obj.howSum(num,numbers))

    
