class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        result=0
        while l<r:
            area=min(heights[l],heights[r])*(r-l)
            result=max(res,area)
            if heights[l]<=heights[r]:
                l=l+1
            else:
                r=r-1
        return result
        
