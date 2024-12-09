from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        total_fuel = 0
        for i in range(len(gas)):
            total_fuel += gas[i] - cost[i]

        if total_fuel < 0:
            return -1

        fuel = 0
        result = 0
        for i in range(len(gas)):
            fuel += gas[i] - cost[i]
            if fuel < 0:
                fuel = 0
                result = i + 1

        return result

        # fuel = 0
        # count = 0
        # result = 0
        # for i in range(len(gas) * 2):
        #     fuel += gas[i % len(gas)] - cost[i % len(gas)]
        #     if count == len(gas):
        #         return result
        #     if fuel < 0:
        #         fuel = 0
        #         result = (i + 1) % len(gas)
        #         count = 0
        #         continue
        #     count += 1
        # return -1


if __name__ == "__main__":
    s = Solution()
    print(s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
    print(s.canCompleteCircuit([1, 2, 3, 4, 2, 12], [3, 4, 5, 1, 6, 1]))
    print(s.canCompleteCircuit([2, 3, 4], [3, 4, 3]))
