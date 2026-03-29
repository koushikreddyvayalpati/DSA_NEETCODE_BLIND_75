class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_s={}
       # we are using dict to store visited number will be  subtracting next number from target if diff is find in dict we return in the index
        for j in range(0,len(nums)):
            diff=target-nums[j]
            if (diff) in dict_s:
                return [dict_s[diff],j]
            dict_s[nums[j]]=j
        # other way is iterating using two for loops that is o(n^2)
        
