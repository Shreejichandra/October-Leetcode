'''
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.
'''

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        # All elements of A should be same as 1st element of A
        start = A[0]
        swaps1 = 0
        for i in range(1, len(A)):
            if A[i] == start:
                continue
            elif B[i] == start:
                swaps1 += 1
            else:
                swaps1 = float('inf')
        # All elements of B should be same as 1st element of B
        start = B[0]
        swaps2 = 0
        for i in range(1, len(B)):
            if B[i] == start:
                continue
            elif A[i] == start:
                swaps2 += 1
            else:
                swaps2 = float('inf')
        # All elements of A should be same as 1st element of B
        start = B[0]
        swaps3 = 1
        for i in range(1, len(A)):
            if A[i] == start:
                continue
            elif B[i] == start:
                swaps3 += 1
            else:
                swaps3 = float('inf')
        # All elements of B should be same as 1st element of A
        start = A[0]
        swaps4 = 1
        for i in range(1, len(B)):
            if B[i] == start:
                continue
            elif A[i] == start:
                swaps4 += 1
            else:
                swaps4 = float('inf')
        ans = min(swaps1, swaps2, swaps3, swaps4)
        if ans == float('inf'):
            return -1
        else:
            return ans
    
