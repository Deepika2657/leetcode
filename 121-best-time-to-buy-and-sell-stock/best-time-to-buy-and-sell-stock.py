class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
       profit=0
       n=len(prices)
       min_p=prices[0]
       if n==0:
        return 0
       for i in range(1,n):
          if prices[i]<min_p:
            min_p=prices[i]
          else:
            currentprofit=prices[i]-min_p
            if currentprofit>profit:
                profit=currentprofit
       return profit

