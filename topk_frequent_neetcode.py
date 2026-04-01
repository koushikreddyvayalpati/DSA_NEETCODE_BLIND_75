class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store={}
        for i in nums:
            store[i]=store.get(i,0)+1
        ## sorting the dictionary based on values 
        # dic_sorted=dict(sorted(store.items(), key=lambda item:item[1],reverse=True))
        ## convert to list all keys before returning top k elemnts
        # return (list(dic_sorted.keys())[:k])


        # here we define array in which we store what numbers occurs at particular frequency 
        # at frequebcy we can have multiple number
        frequency_elements=[[] for i in range(len(nums)+1)]
        #[[],[],[],[]] this is how strucutrre loooks
        for num,count in store.items():
            frequency_elements[count].append(num)
        res=[]
        # lets iterate from backwords since we need the top k elements
        for i in range(len(frequency_elements)-1,0,-1):
            for n in frequency_elements[i]:
                res.append(n)
                # stop when length of array equals to k we need only top k right 
                if len(res)==k:
                    return res

   



        
      

        

        
