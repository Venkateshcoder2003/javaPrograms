class Complex:
    def __init__(self,tempReal,tempImagionary):
        self.real=tempReal
        self.imagionary=tempImagionary
    def addComplex(self,c1,c2):
         temp=Complex(0,0)
         temp.real=c1.real+c2.real
         temp.imagionary=c1.imagionary+c2.imagionary
         return temp


x1=int(input("Enter real part of complex number 1:"))
y1=int(input("Enter imagionary part of complex number 1:"))
c1=Complex(x1,y1)
print("Complex number 1:",c1.real,"+i",str(c1.imagionary))

x2=int(input("Enter real part of complex number 1:"))
y2=int(input("Enter imagionary part of complex number 1:"))
c2=Complex(x2,y2)
print("Complex number 2:",c2.real,'+i',str(c2.imagionary))

c3=Complex(0,0)
c3=c3.addComplex(c1,c2)

print("complex number 3:",c3.real,"+i",str(c3.imagionary))
