__author__ = 'don'
"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to
 its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
"""
class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
        # first calculate diff
        diff = [0] * len(cost)
        for i in range(len(cost)):
            diff[i] = gas[i]-cost[i]

        sum = 0
        rsum = 0
        startnode = 0
        for i in range(len(diff)):
            rsum += diff[i]
            sum += diff[i]
            if sum < 0:
                # if it is negative, we reset
                # and resume the starting position
                startnode = i + 1
                sum = 0

        if rsum < 0:
            return -1
        else:
            return startnode

