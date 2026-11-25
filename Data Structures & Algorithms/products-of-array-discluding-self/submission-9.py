class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postfix = [None] * len(nums)
        prefix = []
        output = []
        j = len(nums) - 1

        for i, num in enumerate(nums):
            if i == 0:
                prefix.append(nums[i])
                postfix[j] = nums[j]
                j -= 1
                continue

            prefix.append(prefix[i - 1] * nums[i])
            postfix[j] = postfix[j + 1] * nums[j]
            j -= 1

        for i, num in enumerate(nums):
            if i == 0:
                output.append(postfix[i+1])
            elif i == len(nums) - 1:
                output.append(prefix[len(nums) - 2])
            else:
                output.append(prefix[i - 1] * postfix[i + 1])

        return output