class Number:
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        return Number(self.value+other.value)
    def display(self):
        print("Sum:",self.value)
n1=Number(10)
n2=Number(20)
n3=n1+n2
n3.display()