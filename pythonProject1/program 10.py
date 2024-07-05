
class students:
    count=0
    def __init__(self,name):
        self.name=name
        self.marks=[]
        students.count+=1

    def enterMarks(self):
        for i in range(3):
            m=int(input(f"Enter marks of{self.name} in {i+1} subject: "))
            self.marks.append(m)
    def display(self):
        print(self.name,"got",self.marks)
name=input("Enter name:")
s1=students(name)
s1.enterMarks()
s1.display()