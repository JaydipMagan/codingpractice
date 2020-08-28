"""
Given a function rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which generates a uniform random integer in the range 1 to 10.

Do NOT use system's Math.random().

Example 1:

Input: 1
Output: [7]

Example 2:

Input: 2
Output: [8,4]

Example 3:

Input: 3
Output: [8,1,10]

Note:

    rand7 is predefined.
    Each testcase has one argument: n, the number of times that rand10 is called.
"""
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        a = rand7()
        b = rand7()
        rand = a+(b-1)*7
        while rand>40:
            a = rand7()
            b = rand7()
            rand = a+(b-1)*7
        return 1+(rand-1)%10