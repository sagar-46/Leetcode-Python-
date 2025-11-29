class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = {}
        n = len(nums)

        for i in range(n):
            diff = target - nums[i]
            if diff in num:
                return [num[diff],i]
            num[nums[i]] = i
        return []
        
