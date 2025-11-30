class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if(len(set(nums))==len(nums)):
            return False
        else:
            return True

    # return (len(set(nums)) < len(nums))
