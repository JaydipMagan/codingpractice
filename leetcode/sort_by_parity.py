"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Note:

    1 <= A.length <= 5000
    0 <= A[i] <= 5000

"""
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        n = len(A)
        result = [0]*n
        l , h =  0 , n - 1
        for i in range(n):
            if A[i]%2==0:
                result[l] = A[i]
                l+=1
            else:
                result[h] = (A[i])
                h-=1
        return result