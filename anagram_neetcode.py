class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if strings lengths are not same then it cannot be anagram
        if len(s)!= len(t):
            return False
        # let us use the dict to store key value pair for each char in string, so that we can easily compare both the dicts
        dict_for_s={}
        dict_for_t={}
        for c in s:
            dict_for_s[c]=dict_for_s.get(c,0)+1
        for x in t:
            dict_for_t[x]=dict_for_t.get(x,0)+1
        return dict_for_t==dict_for_s
        # there is one more way we can sort the both string and can compare them
        #but time complexity wille o(nlogn)


        
       

        
