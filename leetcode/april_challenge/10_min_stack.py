class Item:

    def __init__(self, val):
        self.val = val
        self.min = None

    def __repr__(self):
        return "Item({}, min_so_far={})".format(self.val, self.min)


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []

    def push(self, x: int) -> None:
        new_item = Item(x)
        if not self.s or new_item.val < self.s[-1].min:
            new_item.min = new_item.val
        else:
            new_item.min = self.s[-1].min

        self.s.append(new_item)

    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        return self.s[-1].val

    def getMin(self) -> int:
        return self.s[-1].min


def test():
    ms = MinStack()
    print(ms.push(2))
    print(ms.push(0))
    print(ms.push(3))
    print(ms.push(0))
    print(ms.getMin())
    print(ms.pop())
    print(ms.getMin())
    print(ms.pop())
    print(ms.getMin())
    print(ms.pop())
    print(ms.getMin())

def test2():
    ms = MinStack()
    print(ms.push(46))
    print(ms.push(46))
    print(ms.push(47))
    print(ms.top())
    print(ms.pop())
    print(ms.getMin())
    print(ms.pop())
    print(ms.getMin())
    print(ms.pop())
    print(ms.push(47))
    print(ms.top())
    print(ms.getMin())
    print(ms.push(-48))

test2()