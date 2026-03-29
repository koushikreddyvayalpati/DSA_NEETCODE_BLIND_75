class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dict_s={}
      ## we sort each string and storing taking it as key for dictionary
        # for c in strs:
        #     sor="".join(sorted(c))
        #     if sor not in dict_s:
        #         dict_s[sor]=[]
        #     dict_s[sor].append(c)
            
        # return list(dict_s.values())
        result=defaultdict(list)
        for s in strs:
#Instead of sorting each string, we can represent every string by the frequency of its characters.
#Since the problem uses lowercase English letters, a fixed-size array of length 26 can capture how many times each character appears.
#
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            result[tuple(count)].append(s)
        return list(result.values())
            



        
       
        
        
