class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        d = {}
        for i,n in enumerate(nums):
            if n in d:
                return [d[n],i]
            else:
                d[target - n] = i

# enumerate 
# d={}  d.has_key
# Goal is to find the index, so use dictionary type, store the number as key, and index as value
