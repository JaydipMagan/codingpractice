class Solution:
    def search(self, nums, target) -> int:
        def binSearch(l,h):
            if h>=l:
                m = l + (h - l) //2
                #normal bin search
                if nums[m]==t:
                    return m
                elif (nums[l]<=t<nums[m] or nums[m]<nums[h]) and (nums[l]<=t<nums[m] or not(nums[m]<t<=nums[h])):
                    return binSearch(l,m-1)
                else:
                    return binSearch(m+1,h)
            else:
                return -1
        t = target
        x = binSearch(0,len(nums)-1)
        return x
s = Solution()
# s.search([4,5,6,7,0,1,2],10)
s.search([4,5,6,7,8,1,2,3],8)
