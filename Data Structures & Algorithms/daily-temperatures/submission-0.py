class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        for i,t in enumerate(temperatures):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > t:
                    res[i] = j - i
                    break
        # print(res)
        return res