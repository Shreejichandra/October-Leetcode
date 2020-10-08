'''Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. 
If target exists, then return its index, otherwise return -1.'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        while(l <= r):
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return -1
