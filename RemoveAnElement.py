
class RemoveElement(object):
    def RemoveElement(self,nums,val):
        i=0
        for x in nums:
            if x !=val:
                nums[i]=x
            i+=1
        return i


    