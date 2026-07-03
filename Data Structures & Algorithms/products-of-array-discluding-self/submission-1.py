class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = []
        s = 1
        for n in nums:
            s *= n
            forward.append(s)
        # print('forward', forward)
        backward = [1 for i in range(len(nums))]
        s = 1
        for i in range(len(backward)-1, -1, -1):
            s *= nums[i]
            backward[i] = s
        # print('backward', backward)

        output = []
        for i in range(len(nums)):
            if i == 0:
                output.append(backward[i+1])
            elif i == len(nums)-1:
                output.append(forward[i-1])
            else:
                s = forward[i-1] * backward[i+1]
                output.append(s)

        return output
        
