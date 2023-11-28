# using assert in tests
###### from chapter_03.stack import Stack begin ######
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    def __len__(self):
        # in python the `len` function is preferred to `size` methods
        return len(self.items)

    def __bool__(self):
        # lets us use the stack as a conditional
        return bool(self.items)

###### from chapter_03.stack import Stack end ######


class MinStack(Stack):
    def __init__(self):
        super().__init__()
        self.minvals = Stack()

    def push(self, value):
        super().push(value)
        if not self.minvals or value <= self.minimum():
            self.minvals.push(value)

    def pop(self):
        value = super().pop()
        if value == self.minimum():
            self.minvals.pop()
        return value

    def minimum(self):
        return self.minvals.peek()


def test_min_stack():
    newstack = MinStack()
    assert newstack.minimum() is None

    newstack.push(5)
    assert newstack.minimum() == 5

    newstack.push(6)
    assert newstack.minimum() == 5

    newstack.push(3)
    assert newstack.minimum() == 3

    newstack.push(7)
    assert newstack.minimum() == 3

    newstack.push(3)
    assert newstack.minimum() == 3

    newstack.pop()
    assert newstack.minimum() == 3

    newstack.pop()
    assert newstack.minimum() == 3

    newstack.pop()
    assert newstack.minimum() == 5

    newstack.push(1)
    assert newstack.minimum() == 1


if __name__ == "__main__":
    test_min_stack()
