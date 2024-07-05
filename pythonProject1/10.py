class students:
    count=0
    def __init__(self,name):
        self.name=name
        self.marks=[]

        students.count+=1
    def entermarks(self):
        for i in range(3):
            marks=int(input(f"Enter the marks of {self.name}  in {i+1} subject: "))
            self.marks.append(marks)
    def display(self):
        list_of_marks=self.marks
        print(list_of_marks)
        marks=0
        for i in list_of_marks:
            obt_marks=marks+ i
            marks=obt_marks
        print(marks)
        print(f"{self.name} has got:",(marks/300)*100,"%")


name=input("Enter the name of the students:")
s1=students(name)
s1.entermarks()
s1.display()
