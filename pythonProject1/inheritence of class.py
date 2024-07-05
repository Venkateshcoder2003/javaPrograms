class Human():
    def __init__(self,name):
        self.name=name
        self.num_eyes=2
        self.num_nose=1
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")

class Male(Human):
    def __init__(self,name):
        super().__init__(name)
        self.name=name
    def flirt(self):
        print("i can flirt")
    def work(self):
        super().work()
        print("i can code")

        print("Hi i am ",male_1.name)

male_1=Male("venkatesh")
male_1.eat()
male_1.flirt()
male_1.work()
print(male_1.name)
print(male_1.num_eyes)
print(male_1.num_nose)

