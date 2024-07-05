no_of_ele=int(input("Enter the number of elements:"))
original_list=[]
new_list=[]
i=0
while i<no_of_ele:
    num=int(input("Enter the element to original list:"))
    original_list.append(num)
    i+=1
print(original_list)
for number in original_list:
    digit=str(number)
    for ele in digit:
        new_list.append(ele)
print(new_list)