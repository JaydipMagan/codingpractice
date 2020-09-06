"""
Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

Example 1:

Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.

Notes: 

    1 <= A.length = A[0].length = B.length = B[0].length <= 30
    0 <= A[i][j], B[i][j] <= 1
"""
class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        n=len(A)
        pts_a=[(i,j) for i in range(n) for j in range(n) if A[i][j]==1]
        pts_b=[(i,j) for i in range(n) for j in range(n) if B[i][j]==1]
        counter = collections.Counter((x1-x2,y1-y2) for x1,y1 in pts_a for x2,y2 in pts_b)
        return max(counter.values() or [0])