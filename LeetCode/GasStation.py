"""
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3470/

There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.
Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:

If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.

[Example]
Input: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

[Best]
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost): return -1
        
        pos = balance = 0
        for i in range(len(gas)):
            balance += gas[i]-cost[i]
            if balance < 0:
                balance = 0
                pos = i+1
                
        return pos

"""

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        diff = [gas[i] - cost[i] for i in range(len(gas))]
        diff_sum = sum(diff)
        
        if diff_sum < 0:
            return -1
        else:
            start, tank = 0, 0
            for i in range(len(gas)):
                tank = tank + gas[i] - cost[i]
                if tank < 0:
                    start = i + 1
                    tank = 0            
            return start