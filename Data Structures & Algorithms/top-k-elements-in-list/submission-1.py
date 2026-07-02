class Solution:
    def fillStack(self, n, freq, stack):
        if len(stack) == 0:
            stack.append(n)
            return
        
        if freq[n] >= freq[stack[-1]]:
            top = stack.pop()
            self.fillStack(n, freq, stack)
            if top != n:
                stack.append(top)
        else:
            stack.append(n)
        return


    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        stack = []
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
            self.fillStack(n, freq, stack)
            # print(stack)
            
        
        return stack[:k]
        