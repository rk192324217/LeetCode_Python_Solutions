class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        profits_sorted=sorted(zip(difficulty,profit))
        worker.sort()
        total=0
        max_profit=0
        i=0

        for w in worker:
            
            while i<len(profits_sorted) and profits_sorted[i][0]<=w:
                max_profit=max(max_profit,profits_sorted[i][1]) 
                i+=1
            total+=max_profit
        return total