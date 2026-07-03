class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        forward = [1] * length
        backward = [1] * length

        for i in range(1, length):
            forward[i] = nums[i-1] * forward[i-1]
                      
        # print('forward', forward)

        for i in range(length-2, -1, -1):
            backward[i] = nums[i+1] * backward[i+1]

        # print('backward', backward)

        output = [0] * length
        for i in range(length):
            output[i] = forward[i] * backward[i]

        return output