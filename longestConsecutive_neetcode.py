class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        # let store them in num set retriivng elemnt is O(1)
        #variable lon to store the longest sub sequences
        #for vis [2,20,4,10,3,4,5]
        #[2,3,4,5]
        #[20]
        #[10]
        #this are the three possbe first elements if we clearly break down and visulaise them
        # what are possible seques if element -1 then we cna consider as first elemnt
        lon=0
        for num in num_set:
            if num-1 not in num_set:
                lenth=0
                #if it is first lets try consective sequence and calculate the length
                while num+lenth in num_set:
                    lenth+=1
                lon=max(lon,lenth)
        return lon



        
