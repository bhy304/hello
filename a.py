class TestClass:
    name = "TEST"

    def __init__(self):
        print("TTTTTTTTTTTTTT")

    @staticmethod
    def static_method():
        print("STATIC!!")

    def set_name(self, new_name):
        self.name = new_name
        print("SET NAME>>", self.full_name)

    @property
    def full_name(self):
        return self.name + " FFFF"

    def get_name(self):
        print("QQQQQQQQQQQQQQQQQQQQ")
        return self.name

    def area(self, x, y):
        return x * y

class Child(TestClass):
    def __init__(self):
        super().__init__()
        print("My init!!!")

    def get_name(self):
        t = super().get_name()
        return "Child Name:" + self.name

    def area(self, x, y):
        t = super().area(x, y)
        return t / 2

test = TestClass()
child = Child()

test.static_method()
TestClass.static_method()

print("FFFFFFF>>", test.full_name)
test.set_name("RRRRRRRRRRRRrdd")
print("FFFFFFF>>", test.full_name)

print(test.static_method)
print(TestClass.static_method)

# cmd = input("Input the function name>> ")

# getattr(test, cmd)()
# getattr(TestClass, 'static_method')()

# print("11111>>", child.get_name())

# c = callable(test.get_name)
# print("cccccccc>>", c)
