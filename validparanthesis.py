class Solution:
    def isValid(self, s: str) -> bool:
        #stack
        st=[]
        clos={'}':'{',']':'[',')':'('}
        for c in s:
            if c in clos:
                if st and st[-1]==clos[c]:
                    st.pop()
                else:
                    return False
            else:
                st.append(c)
        return True if not st else False
                


        

                    

        
        
