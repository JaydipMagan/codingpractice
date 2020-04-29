import collections

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    
        lcss = collections.defaultdict(lambda: -1)
        
        def lcs(x,y):
            if len(x)==0 or len(y)==0:
                return 0
            
            if x[-1:]==y[-1:]:
                key = (x,y)
                value = 1+lcs(x[:-1],y[:-1]) if lcss[key]==-1 else lcss[key]
                lcss[key]=value
                return value
            else:
                key, key1 = (x[:-1],y), (x,y[:-1])
                value = lcs(x[:-1],y) if lcss[key]==-1 else lcss[key]
                value1 = lcs(x,y[:-1]) if lcss[key1]==-1 else lcss[key1]
                lcss[key]=value
                lcss[key1]=value1
                return max(value,value1)
            
        return lcs(text1,text2)