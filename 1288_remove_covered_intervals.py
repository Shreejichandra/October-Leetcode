'''Given a list of intervals, remove all intervals that are covered by another interval in the list.

Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

After doing so, return the number of remaining intervals.'''


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key = lambda x: x[0])
        count = 0
        end = 0
        for i in range(n):
            for j in range(i+1, n):
                if intervals[i][0] != intervals[j][0]:
                    break
                if intervals[i][1] < intervals[j][1]:
                    intervals[i], intervals[j] = intervals[j], intervals[i]
        #print(intervals)
        for i in range(n):
            if intervals[i][1] > end:
                end = intervals[i][1]
                count += 1
 
        return count
