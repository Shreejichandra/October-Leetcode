'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 '''
 
 class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        dp1 = [0] * (n-1)
        # from 1 to n-1
        dp1[0] = nums[0]
        for i in range(1, n-1):
            dp1[i] = max(dp1[i-1], (dp1[i-2] + nums[i]))
        #print(dp1)
        
        # from 2 to n 
        dp2 = [0] * (n-1)
        dp2[0] = nums[1]
        for i in range(2, n):
            j = i - 1 
            dp2[j] = max(dp2[j - 1], (dp2[j - 2] + nums[i]))
        #print(dp2)
        
        return max(dp1[-1], dp2[-1])
            
                         
                         
        
        
        
        
        
