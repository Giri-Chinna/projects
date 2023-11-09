class Solution:

    def __init__(self, nums,target):
        self.nums = nums
        self.target = target
    
    def two_sum(self):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(self.nums)-1):
            for j in range(i+1,len(self.nums)):
                if self.nums[i]+self.nums[j] == self.target:
                    return [i,j]

res1 = Solution([2,7,11,15],9)
res2 = Solution([3,2,4],6)
res3 = Solution([3,3],6)
res4 = Solution([3,2,4,5,1,8,7],13)

print(res1.two_sum())
print(res2.two_sum())
print(res3.two_sum())
print(res4.two_sum())
