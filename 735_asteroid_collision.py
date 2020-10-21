'''
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
'''

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        n = len(asteroids)
        for i in range(1, n):
            if asteroids[i] > 0:
                stack.append(asteroids[i])
            else:
                append_new_rock = True
                while stack and stack[-1] > 0:
                    if stack[-1] == abs(asteroids[i]):
                        stack.pop()
                        append_new_rock = False
                        break
                    elif stack[-1] > abs(asteroids[i]):
                        append_new_rock = False
                        break
                    else:
                        stack.pop()
                if append_new_rock:
                    stack.append(asteroids[i])          

        return stack
            
                
            
            
        
