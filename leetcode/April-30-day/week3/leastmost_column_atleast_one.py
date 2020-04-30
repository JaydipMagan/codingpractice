"""
(This problem is an interactive problem.)

A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

    BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
    BinaryMatrix.dimensions() returns a list of 2 elements [rows, cols], which means the matrix is rows * cols.

Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes you're given the binary matrix mat as input in the following four examples. You will not have access the binary matrix directly.

Example 1:

Input: mat = [[0,0],[1,1]]
Output: 0

Example 2:

Input: mat = [[0,0],[0,1]]
Output: 1

Example 3:

Input: mat = [[0,0],[0,0]]
Output: -1

Example 4:

Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
Output: 1

Constraints:

    rows == mat.length
    cols == mat[i].length
    1 <= rows, cols <= 100
    mat[i][j] is either 0 or 1.
    mat[i] is sorted in a non-decreasing way.
"""

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