class GrandParent:
    def money(self):
        print("Grandparent's property")
class Parent(GrandParent):
    def business(self):
        print("Parents business")
class child(Parent):
    def education(self):
        print("child's education")

c=child()
c.money()
c.business()
c.education()