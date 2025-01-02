class MinStackNoMemo:

    def __init__(self):
        self.data = []
        self.min = float("inf")

    def push(self, val: int) -> None:
        self.data.append(val)
        if val < self.min:
            self.min = val

    def pop(self) -> None:
        elem = self.data.pop()
        if elem == self.min:
            if self.data:
                self.min = min(self.data)
            else:
                self.min = float("inf")

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min


class MinStack:

    def __init__(self):
        self.data = []

    def push(self, val: int) -> None:
        if not self.data:
            self.data.append((val, val))
        else:
            self.data.append((val, min(val, self.data[-1][0])))

    def pop(self) -> None:
        self.data.pop()

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        return self.data[-1][1]


if __name__ == "__main__":
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())
