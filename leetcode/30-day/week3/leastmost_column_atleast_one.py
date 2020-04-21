

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        # Beast mode version
        #  x, y = binaryMatrix.dimensions()
        # def seems_legit(column):
        #     return any(binaryMatrix.get(i, column) for i in range(x))
        
        # lo = 0
        # hi = y
        
        # while lo < hi:
        #     mid = (lo + hi) // 2
        #     if seems_legit(mid):
        #         hi = mid
        #     else:
        #         lo = mid + 1
        # return lo if lo < y else -1

        # return first occurence of element in list
        def binSearch(i,j):
            l = 0
            h = j
            index = -1
            while(l<=h):
                m = l + (h-l)//2
                if binaryMatrix.get(i,m)==1:
                    index = m
                    h = m - 1
                else:
                    l = m + 1
            return index    
                    
        x,y = binaryMatrix.dimensions()[0]-1,  binaryMatrix.dimensions()[1]-1
        min_index = None
        while x>=0:
            index_found = binSearch(x,y)
            x-=1
            if index_found == -1:
                continue 
            min_index = index_found if min_index==None else min(min_index,index_found)
        return -1 if min_index==None else min_index