class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Since set has only unique element we can easily whether the number is repeated or not through comparing size of set and given array
        into_set=set(nums)
        if len(into_set)!=len(nums):
            return True
        else:
            return False
