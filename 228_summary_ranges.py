''''

You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
'''

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == []:
            return []
        ans = [[nums[0]]]
        if len(nums) == 1:
            return [str(nums[0])]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                continue
            else:
                ans[-1].append(nums[i-1])
                ans.append([nums[i]])
        if nums[-1] == nums[-2]+1:
            ans[-1].append(nums[-1])
        
        output = []
        for i in ans:
            if i[0] == i[-1]:
                output.append(str(i[0]))
            else:
                output.append(str(i[0]) + "->" + str(i[1]))
        return output
        
        
      
