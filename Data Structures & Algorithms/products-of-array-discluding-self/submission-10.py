class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        postfix = [0] * n
        output = []

        # 1. Build prefix and postfix completely first (8 spaces)
        j = n - 1
        for i, num in enumerate(nums):
            if i == 0:
                prefix[i] = num
                postfix[j] = nums[j]
            else:
                prefix[i] = prefix[i - 1] * num
                postfix[j] = postfix[j + 1] * nums[j]
            j -= 1

        # 2. Build output AFTER the first loop finishes (8 spaces)
        for i in range(n):
            if i == 0:
                output.append(postfix[i + 1])
            elif i == n - 1:
                output.append(prefix[i - 1])
            else:
                output.append(prefix[i - 1] * postfix[i + 1])

        return output