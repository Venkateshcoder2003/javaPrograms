class Human():
    def eat(self):
        print("i can eat")
    #def work(self):
     #   print("I can work")
class Male():
    def flirt(self):
        print("i can flirt ")
    def work(self):
        print("I can code")

class Boy(Human,Male):
    def sleep(self):
        print("i can sleep")
    #def work(self):
     #   print("i can test")
boy_1=Boy()
boy_1.work()
#boy_1.work()
#Male.work(boy_1)

#Boy.work(boy_1)
#print(Boy.mro())