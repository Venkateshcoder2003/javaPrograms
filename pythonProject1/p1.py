
print("Enter the name of the Student:")
name = input()

print("Enter the Student USN:")
USN = input()
marks_list=[]
sub_list=[]
print("Enter the number of subjects:")
sub=int(input())
total=0
loop=0
while loop<sub:
    print("Enter the subject name:")
    subject_name = input()
    sub_list.append(subject_name)

    print("Enter the marks scored in", {sub_list[loop]}, "subject:")
    marks = int(input())
    marks_list.append(marks)
    loop += 1
print(name)
print(USN)
print(marks_list)
print(sub_list)

for marks in marks_list:
    total=total+marks
print("Total marks obtained:",total)

print(f"Average marks:{(total)/len(marks_list)}")

final_marks=sub*50
print(f"percentage is :{(total/final_marks)*100}","%")



