class Solution:
# input:["Koushik",Reddy]
    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res+=str(len(s))+"#"+s
        return res
#res ="7#Koushik5#Reddy"
    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j=j+1
            length = int(s[i:j])
            i=j+1
            j=i+length
            res.append(s[i:j])
            i=j
        return res


