class Solution:
    def lastStoneWeight(self, stones) -> int:
        def find2Stones(stones):
            copy_stones = stones[:]
            first = max(copy_stones)
            copy_stones.remove(first)
            second = max(copy_stones)
            return second,first
        
        if len(stones)==1:
            return stones[0]

        while not len(stones)<=1:
            print(stones)
            x,y= find2Stones(stones) #O(N)
            print("Combining",x,y,stones)
            if x==y:
                stones.remove(x)
                stones.remove(y)
            else:
                stones.remove(x)
                stones[stones.index(y)] = y-x
            print("ressult",stones)
        if len(stones)==0:
            return 0
        return stones[0]

s = Solution()
print(s.lastStoneWeight([2,7,4,1,8,1]))
