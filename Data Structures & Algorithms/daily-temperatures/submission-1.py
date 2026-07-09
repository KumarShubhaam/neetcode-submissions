class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i,t in enumerate(temperatures):
            if stack and t > temperatures[stack[-1]]:
                while stack and t > temperatures[stack[-1]]:
                    j = stack.pop()
                    res[j] = i - j
                stack.append(i)
            else:
                stack.append(i)
            # print(stack, i)
        
        # print(res)
        return res
