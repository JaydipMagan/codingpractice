class Solution:
    def singleNumber(self, nums) -> int:
        seen = dict([ (p,0) for p in nums ])
        to_return = nums[0]
        for x in nums:
            if seen[x]==0 or seen[x]==1:
                seen[x] = seen[x]+1
        for x in seen:
            if seen[x] == 1:
                return x


s = Solution()
a = s.singleNumber([4,1,2,1,2])
print(a)