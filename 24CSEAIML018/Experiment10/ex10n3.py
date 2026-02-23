class Father:
    def skill(self):
        print("Father has leadership quality.")
class Mother:
    def skill2(self):
        print("Mother has multitasking ability.")
class Child(Father,Mother ):
    def skill3(self):
        print("Child is learning skills from parents.")
c=Child()
c.skill()
c.skill2()
c.skill3()