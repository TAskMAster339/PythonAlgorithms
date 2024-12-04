from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # way = [0] * len(gas)
        # start = 0
        # for i in range(len(gas) + 1):
        #     if gas[i % len(gas)] - cost[i % len(gas)] > 0:
        #         start = i % len(gas)
        #         break
        #
        # for i in range(len(gas) + 2):
        #     way[i % len(gas)] = way[(i - 1) % len(gas)] + gas[i % len(gas)] - cost[i % len(gas)]
        #
        # print(way)
        # if all(x >= 0 for x in way):
        #     return start
        # return -1

        fuel = 0
        count = 0
        result = 0
        for i in range(len(gas) * 2):
            fuel += gas[i % len(gas)] - cost[i % len(gas)]
            if count == len(gas):
                return result
            if fuel < 0:
                fuel = 0
                result = (i + 1) % len(gas)
                count = 0
                continue
            count += 1
        return -1

if __name__ == "__main__":
    s = Solution()
    print(s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
    print(s.canCompleteCircuit([1, 2, 3, 4, 2, 12], [3, 4, 5, 1, 6, 1]))
    print(s.canCompleteCircuit([2, 3, 4], [3, 4, 3]))
