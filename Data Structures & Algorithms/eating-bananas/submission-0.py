class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        if h == len(piles):
            return MAX_ELEMENT
        1 <= k <= MAX_ELEMENT

        '''
        def find_curr_hr(k):
            hr = 0
            for i,p in enumerate(piles):
                r = p % k
                q = p // k
                hr += q
                if r > 0:
                    hr += 1
            # print('for k=', k, 'hr is' , hr)
            return hr                

        max_k = max(piles)
        min_k = 1
        ans = float('inf')
        while min_k <= max_k:
            k = min_k + ((max_k - min_k) // 2)
            curr_hr = find_curr_hr(k)
            if curr_hr <= h:
                max_k = k - 1
                ans = min(ans, k)
            elif curr_hr > h:
                min_k = k + 1

        return ans