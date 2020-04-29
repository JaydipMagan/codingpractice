class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        x = 0 # index
        maxx = 0 # max possible
        for step in nums:
            if x>maxx:
                return False
            maxx = max(maxx,step+x)
            x+=1
        return True
        
        # N = len(nums)
        
        # target = N-1
        # for i in range(N-1, -1, -1):
        #     if i + nums[i] >= target:
        #         target = i

        # return target == 0