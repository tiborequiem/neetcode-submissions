class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashS = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashS:
                return [hashS[complement], i]
            else:
                hashS[num] = i    

     