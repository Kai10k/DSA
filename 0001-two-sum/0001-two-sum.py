class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dictionary = {}
        for i in range (0,n):
            remaining = target - nums[i]
            if remaining in dictionary:
                return [dictionary[remaining], i]
            else:
                dictionary [nums[i]] = i