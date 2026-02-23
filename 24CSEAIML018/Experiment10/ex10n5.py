class Parent:
    def __init__(self):
        print("Parent Constructor")
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child Constructor")
c=Child()