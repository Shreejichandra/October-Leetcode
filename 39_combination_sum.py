'''Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]: 
        output = []
        
        def dfs(index, target, combo):
            if target == 0:
                output.append(combo)
                return
            if target < 0:
                return
            if index == len(candidates):
                return
            
            dfs(index, target - candidates[index], combo + [candidates[index]])
            dfs(index + 1, target, combo)
        
        dfs(0, target, [])
            
                    
        return output
                            
                    
                    
                    
            
