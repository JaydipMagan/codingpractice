class Solution:
    def countElements(self, arr) -> int:
        counted=[]
        for x in arr:
            if x+1 in arr:
                counted.append(x)
        return len(counted)