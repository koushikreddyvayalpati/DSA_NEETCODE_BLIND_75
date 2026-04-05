class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## rather than using two loops we can think like
        ## the resuly we want is the product of all element than corect element
        ## so let us use two arrays one the store product of all elements left of that element
        ## similary suffix array product of all elemnts next to right of th elements
        ## logical then result =product of elemnets left pf[i]* sf[i]product of elemts right

        # pfarray=[1]*len(nums)
        # sfarray=[1]*len(nums)
        # ar=[1]*len(nums)
        # for i in range(1,len(nums)):
        #     pfarray[i]=pfarray[i-1]*nums[i-1]
        # for i in range(len(nums)-2,-1,-1):
        #     sfarray[i]=sfarray[i+1]*nums[i+1]
        # for i in range(len(nums)):
        #     ar[i]=pfarray[i]*sfarray[i]
        # return ar
        ## for optimizing storage we can reduce same approach using one array rather than but same approach
        n=len(nums)
        ar_array=[1]*n
        prefix=1
        for i in range(n):
            ar_array[i]=prefix
            prefix=prefix*nums[i]
        postfix=1
        for i in range(n-1,-1,-1):
            ar_array[i]=ar_array[i]*postfix
            postfix=postfix*nums[i]
        return ar_array

       
        
        
        
