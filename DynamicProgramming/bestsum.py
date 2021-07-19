class Solution(object):
    def __init__(self) -> None:
        self.memo = {}

    def bestSum(self, targetSum, numbers):

        if targetSum in self.memo:
            return self.memo[targetSum]
        
        if targetSum == 0: return []
        if targetSum < 0: return None
        
        shortestCombination = None

        for num in numbers:
            remainder = targetSum - num 
            remainderCombination = self.bestSum(remainder, numbers)
            if remainderCombination is not None:
                combination = remainderCombination + [num]
                if shortestCombination is None or len(shortestCombination) > len(combination):
                    shortestCombination = combination
            
        self.memo[targetSum] = shortestCombination
        return shortestCombination

if __name__=='__main__':
    obj = Solution()
    numbers = [2,3,5]
    num = 8
    print(obj.bestSum(num,numbers))

    
