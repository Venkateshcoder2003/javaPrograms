name1=input("enter a name: ")
name2=input("enter another name: ")
x=name1+name2
ls=x.lower()
t=ls.count('t')
r=ls.count('r')
u=ls.count('u')
e=ls.count('e')
true=t+r+u+e

l=ls.count('l')
o=ls.count('o')
v=ls.count('v')
e=ls.count('e')
love=l+o+v+e
love_score=str(true)+str(love)
print(f"your love score is {love_score}"+"%")

#love calculator