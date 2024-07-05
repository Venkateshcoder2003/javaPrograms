class AandC:
    def __init__(self,radius):
        self.radius=radius
        self.result=[]
    def circumference(self):
        circum=2*3.14*self.radius
        self.result.append(circum)
    def area(self):
        area=3.14*self.radius**2
        self.result.append(area)
    def display(self):
        print(f"Peimeter is {self.result[0]} and Area is {self.result[1]}")
rad=int(input("Enter radius:"))
operation=AandC(rad)

operation.circumference()
operation.area()
operation.display()








