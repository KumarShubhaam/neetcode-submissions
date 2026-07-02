class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i,n in enumerate(nums):
            freq[n] = freq.get(n, 0) + 1
        
        distinct = []
        for key,value in freq.items():
            distinct.append([key, value]) 
        distinct.sort(key=lambda x: x[1], reverse=True)
        # print(distinct)
        res = []
        for i in range(k):
            res.append(distinct[i][0])
        return res