"""
https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/562/week-4-october-22nd-october-28th/3508/

[Solution]
Approach #1: Simulation [Accepted]
Intuition

Instead of keeping track of how much champagne should end up in a glass, keep track of the total amount of champagne that flows through a glass. 
For example, if poured = 10 cups are poured at the top, then the total flow-through of the top glass is 10; the total flow-through of each glass in the second row is 4.5, and so on.

Algorithm
In general, if a glass has flow-through X, then Q = (X - 1.0) / 2.0 quantity of champagne will equally flow left and right. 
We can simulate the entire pour for 100 rows of glasses. 
A glass at (r, c) will have excess champagne flow towards (r+1, c) and (r+1, c+1).

- java
class Solution {
    public double champagneTower(int poured, int query_row, int query_glass) {
        double[][] A = new double[102][102];
        A[0][0] = (double) poured;
        for (int r = 0; r <= query_row; ++r) {
            for (int c = 0; c <= r; ++c) {
                double q = (A[r][c] - 1.0) / 2.0;
                if (q > 0) {
                    A[r+1][c] += q;
                    A[r+1][c+1] += q;
                }
            }
        }

        return Math.min(1, A[query_row][query_glass]);
    }
}

- python
class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        A = [[0] * k for k in xrange(1, 102)]
        A[0][0] = poured
        for r in xrange(query_row + 1):
            for c in xrange(r+1):
                q = (A[r][c] - 1.0) / 2.0
                if q > 0:
                    A[r+1][c] += q
                    A[r+1][c+1] += q

        return min(1, A[query_row][query_glass])

Complexity Analysis
Time Complexity: O(R^2), where R is the number of rows. As this is fixed, we can consider this complexity to be O(1).
Space Complexity: O(R^2), or O(1) by the reasoning above.

[BEST]
class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        if poured==0:
            return 0
        if query_glass==0 and query_row==0:
            return 1 if poured>=1 else 0
        
        dp=[0]*(query_glass+1)
        dp[0]=poured
        
        for i in range(1,query_row+1,1):
            num=query_row-i+1
            start=max(0,(query_glass-num))
            end=min(i,query_glass)
            for j in range(end,start-1,-1):
                if j==0:
                   dp[j]=max((dp[j]-1)/2.0,0)
                else:
                   dp[j]=max((dp[j-1]-1)/2.0,0)+max((dp[j]-1)/2.0,0)
            
        
        return min(dp[query_glass],1)
"""
class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        dp = [[0 for _ in range(x)] for x in range(1, query_row + 2)]
        dp[0][0] = poured

        for r in range(query_row):
            for c in range(r + 1):
                nextglass = (dp[r][c] - 1.0) /  2.0
                if nextglass > 0:
                    dp[r+1][c] += nextglass
                    dp[r+1][c+1] += nextglass

        return min(1, dp[query_row][query_glass])