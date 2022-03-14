class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        # print("capacity is: ", capacity)

    def can_add(self, v):
        # print("v is ", v)
        # print("capacity is ", self.capacity)
        return True if self.capacity >= v else False

    def add(self, v):
        self.capacity -= v
        # print("self.capacity is: ", self.capacity)
        # print("v2 is: ", v)
        return self.capacity


x = MoneyBox(10)

x.add(5)

x.add(4)

print(x.can_add(1))
