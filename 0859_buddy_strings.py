'''
Given two strings A and B of lowercase letters, return true if you can swap two letters in A so the result is equal to B, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at A[i] and A[j]. For example, swapping at indices 0 and 2 in "abcd" results in "cbad"
'''

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        m = len(A)
        n = len(B)
        if m != n:
            return False
        elif A == B:
            d1 = defaultdict(int)
            for i in A:
                d1[i] += 1
                
            flag = 0
            for i in d1:
                if d1[i] > 1:
                    flag = 1
                    break
            if flag == 1:
                return True
            else:
                return False
            
        else:
            A = list(A)
            B = list(B)
            for i in range(m):
                if A[i] == B[i]:
                    continue
                else:
                    if A[i] not in B:
                        return False
                    else:
                        ind = B.index(A[i])
                        #print(ind)
                        ch = A[ind]
                        if ch == B[i]:
                            A[i], A[ind] = A[ind], A[i]
                            if A == B:
                                return True
                            else:
                                return False
                        else:
                            return False
            
            
