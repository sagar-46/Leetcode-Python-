class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        maxsum = nums[0]
        for num in nums:
            curr += num
            maxsum = max(maxsum,curr)
            if curr < 0:
                curr = 0
        return maxsum
