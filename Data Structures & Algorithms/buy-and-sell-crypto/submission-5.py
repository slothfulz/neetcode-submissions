class Solution:
    '''
    understand
    input: integer array ==> element represent prices, element position represent day
    output: integer 
    
    '''
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        for i in range(len(prices)):
            for j in range(i + 1):
                if (prices[i] - prices[j]) > output:
                    output = prices[i] - prices[j]
        return output
        