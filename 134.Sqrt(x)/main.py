class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        start, end = 1, x // 2
        while start <= end:
            mid = (start + end) // 2
            if x // mid == mid:
                return mid
            if x // mid < mid:
                end = mid - 1
            else:
                start = mid + 1
        return (start + end) // 2

    def mySqrt_bin(self, x: int) -> int:
        if x < 2:
            return x
        count = 0
        temp = x
        while temp:
            count += 1
            temp >>= 1
        result = 0
        for i in range((count + 1) // 2, -1, -1):
            result |= 1 << i
            if x // result < result:
                result ^= 1 << i
        return result


if __name__ == "__main__":
    f = Solution().mySqrt
    print(f(4))  # 2
    print(f(8))  # 2
    print(f(9))  # 3
    print(f(0))  # 0
