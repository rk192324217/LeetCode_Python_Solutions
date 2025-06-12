class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        f1,f2=-prices[0],0
        f3,f4=-prices[0],0
        for price in prices:
            f1=max(f1,-price)
            f2=max(f2,f1+price)
            f3=max(f3,f2-price)
            f4=max(f4,f3+price)
        return f4

prices=[7,1,5,3,6,4]  
sol=Solution()  
print(f"Maximum Profit: {sol.maxProfit(prices)}")