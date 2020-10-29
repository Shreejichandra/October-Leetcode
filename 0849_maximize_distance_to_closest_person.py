'''
You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to the closest person.
'''

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        start = False
        n = len(seats)
        ans = []
        count = 0
        begin_index = -1
        for i in range(n):
            if seats[i] == 1 and start == False:
                ans.append(count)
                count = 0
                start = True
                begin_index = i
                
            elif seats[i] == 1 and start == True:
                x = (count + 1)//2
                ans.append(x)
                count = 0
                begin_index = i
                
            elif seats[i] == 0 and i == n-1:
                count += 1
                
            elif seats[i] == 0:
                count += 1
        if count:
            ans.append(count)
        return (max(ans))
                
        
