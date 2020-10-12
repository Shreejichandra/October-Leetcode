'''Given a string s, remove duplicate letters so that every letter appears once and only once. 
You must make sure your result is the smallest in lexicographical order among all possible results.'''

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d = defaultdict(int)
        for i in s:
            d[i] += 1
            
        stack = []
        ans = ""
        for i in s:
            if i in stack:
                d[i] -= 1
                continue
            if len(stack) == 0:
                stack.append(i)
                d[i] -= 1
            else:
                while (len(stack) != 0 and i < stack[-1]):
                    if d[stack[-1]] > 0:
                        stack.pop()
                    else:
                        break
                     
                stack.append(i)
                d[i] -= 1
                
        return "".join(i for i in stack)
            
                        
                
            
        
     
