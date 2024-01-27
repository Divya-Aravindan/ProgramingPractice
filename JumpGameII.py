class Solution(object):
    def jump(self,nums):
        l=r=0
        while l< len(nums)-1:
            farthest =0
            for i in range (l, r+1):
                fartehst= max(farthest,i)
            l=r
            r=i+1
            res +=1
        return res

