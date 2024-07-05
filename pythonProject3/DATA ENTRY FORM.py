
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root=Tk()
root.title("DATA ENTRY FORM")
root.geometry("800x500")
#root.configure(bg="orange")
#creat frame 1
headline=tk.Label(root,text="REGISTRATION FORM",font="bold")
headline.pack()
frame1=tk.Frame(root)
frame1.pack()
def enterdata():
    firstname_info=firstname.get()
    lastname_info=lastname.get()
    title_info=title.get()
    age_info=age_value.get()
    nationality_info=nationality_value.get()
    comp_course_info=comp_course_value.get()
    present_course_info=present_course_value.get()
    semesters_info=semesters_value.get()
    reg_info=reg_variable.get()
    terms_info=terms_var.get()
    if not terms_info:
        messagebox.showwarning("warning","Accepting Terms And Condition Is Neccessary")
    elif not firstname_info or not lastname_info or not title_info or not age_info or not nationality_info or not comp_course_info or not present_course_info or not reg_info:
        messagebox.showerror("ERROR","Please fill all the details")
    else:
        messagebox.showinfo("INFORMATION","You Have Registered Successfully")

    f=open(firstname_info +'.txt' ,'w')
    f.write("*****Information of Name,Age,Nationality****"+'\n')
    f.write("1.Student Name:")
    f.write(firstname_info +'\n')
    f.write(lastname_info+'\n')
    f.write(title_info+'\n')
    f.write("2.Age:")
    f.write(age_info+'\n')
    f.write("3.Nationality:")
    f.write(nationality_info+'\n')
    f.write("*******EDUCATIONAL DETAILS******" +'\n')
    f.write("4.completed Course:")
    f.write(comp_course_info+'\n')
    f.write("5.Present Course:")
    f.write(present_course_info +'\n')
    f.write("6.Semisters(if applicable):")
    f.write(semesters_info+'\n')

    first_name_entry.delete(0,END)
    second_name_entry.delete(0,END)
    age_spinbox.delete(0,END)
    nationality_combobox.delete(0,END)
    title_combobox.delete(0,END)
    comp_course_combobox.delete(0,END)
    present_course_combobox.delete(0,END)
    numsemesters_spinbox.delete(0,END)

#variables of first label frame
firstname=tk.StringVar()
lastname=tk.StringVar()
title=tk.StringVar()
age_value=tk.StringVar()
nationality_value=tk.StringVar()
#variables of second label frame

comp_course_value=tk.StringVar()
present_course_value=tk.StringVar()
semesters_value=tk.StringVar()

reg_variable=tk.StringVar(value='Registration Failed')

#saving user information
user_info_frame=tk.LabelFrame(frame1,text="user Information")
user_info_frame.grid(row=0,column=0,padx=20,pady=20)

#creat widget inside labelframe
first_name_label=tk.Label(user_info_frame,text="First Name:")
first_name_label.grid(row=0,column=1)

last_name=tk.Label(user_info_frame,text="Last Name:")
last_name.grid(row=0,column=2)

title_label=tk.Label(user_info_frame,text="Title")
title_label.grid(row=0,column=0)

first_name_entry=tk.Entry(user_info_frame,textvariable=firstname)
first_name_entry.grid(row=1,column=1)
second_name_entry=tk.Entry(user_info_frame,textvariable=lastname)
second_name_entry.grid(row=1,column=2)

#creat combo box in user_info_frame
title_combobox=ttk.Combobox(user_info_frame,textvariable=title,values=[" ","Mr.","Ms.","Dr."])
title_combobox.grid(row=1,column=0)
#creat user age spin box

age_label=tk.Label(user_info_frame,text="Age")
age_label.grid(row=2 ,column=0 )

age_spinbox=tk.Spinbox(user_info_frame,textvariable=age_value,from_=15,to=100)
age_spinbox.grid(row=3 ,column=0 )

#ask nationality
nationality_label=tk.Label(user_info_frame,text="Nationality")
nationality_label.grid(row=2,column=1)

nationality_combobox=ttk.Combobox(user_info_frame,textvariable=nationality_value,values=[" ",'India','America','China','japan','Russia'])
nationality_combobox.grid(row=3,column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)


#creat frame 2
course_frame=tk.LabelFrame(frame1,text="Academic Details")
course_frame.grid(row=1,column=0,padx=20,pady=20)

registered_label=tk.Label(course_frame,text="Registration Status:")
registered_label.grid(row=2,column=0)
registered_check=tk.Checkbutton(course_frame,text="Currently Registered",variable=reg_variable,onvalue='Registered successfully',offvalue='Registered Failed')
registered_check.grid(row=3,column=0)

comp_course_label=tk.Label(course_frame,text="Completed Course")
comp_course_label.grid(row=2,column=1)
comp_course_combobox=ttk.Combobox(course_frame,textvariable=comp_course_value,values=['SSLC','PUC','ENGINEERING','B.COM','OTHERS'] )
comp_course_combobox.grid(row=3,column=1)

present_course_label=tk.Label(course_frame,text='Present Course')
present_course_label.grid(row=2,column=2)
present_course_combobox=ttk.Combobox(course_frame,textvariable=present_course_value,values=['SSLC','PUC','ENGINEERING','B.COM','OTHERS'] )
present_course_combobox.grid(row=3,column=2)

numsemesters_label=tk.Label(course_frame,text="Semesters")
numsemesters_label.grid(row=2,column=3)
numsemesters_spinbox=tk.Spinbox(course_frame,textvariable=semesters_value,from_=0 ,to=12)
numsemesters_spinbox.grid(row=3,column=3)

for widget in course_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

terms_frame=tk.LabelFrame(frame1,text='Terms and Conditions')
terms_frame.grid(row=2,column=0,sticky='news',padx=10,pady=5)

terms_var=tk.IntVar(value=0)
terms_check=tk.Checkbutton(terms_frame,text="I Accept terms and conditions",variable=terms_var,onvalue=1,offvalue=0)
terms_check.grid(row=0,column=0)

button=tk.Button(frame1,text="EnterData",command=enterdata)
button.grid(row=3,column=0,sticky='news',padx=10,pady=15)




root.mainloop()

