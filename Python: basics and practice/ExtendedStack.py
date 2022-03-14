class ExtendedStack(list):
    def sum(self):
        self.append(self.pop(-1) + self.pop(-1))

    def sub(self):
        self.append(self.pop(-1) - self.pop(-1))

    def mul(self):
        self.append(self.pop(-1) * self.pop(-1))

    def div(self):
        self.append(self.pop(-1) // self.pop(-1))


def test():
    ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
    ex_stack.div()
    assert ex_stack.pop() == 2
    ex_stack.sub()
    assert ex_stack.pop() == 6
    ex_stack.sum()
    assert ex_stack.pop() == 7
    ex_stack.mul()
    assert ex_stack.pop() == 2
    assert len(ex_stack) == 0


print(test())
