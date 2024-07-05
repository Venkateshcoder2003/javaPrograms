from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox
import googletrans
from googletrans import Translator
from tkinter import PhotoImage


root=Tk()
root.title("Google Translator")
root.geometry("1080x450")


def label_change():
    c1=combo1.get()
    c2=combo2.get()
    label1.configure(text=c1)
    label2.configure(text=c2)
    root.after(1000,label_change)
def TranslateNow():
    text_=text1.get(1.0,END)
    t1=Translator()
    trans_text=t1.translate(text_,src=combo1.get(),dest=combo2.get())
    trans_text=trans_text.text

    text2.delete(1.0,END)
    text2.insert(END,trans_text)

arrow=PhotoImage(file=r"C:\Users\Venkatesh M\Downloads\python tkinter\arrow.png")
myarrow=tk.Label(root,image=arrow)
myarrow.place(x=478,y=150)

language=googletrans.LANGUAGES
languageV=list(language.values())
lang1=language.keys()

#first combo box
combo1=ttk.Combobox(root,values=languageV,font="NORMAL")
combo1.place(x=160,y=40)
combo1.set("English")

label1=tk.Label(root,text="ENGLISH",width=40,height=2,relief=GROOVE,font="BOLD",bg="orange")
label1.place(x=30,y=80)

#second combo box
combo2=ttk.Combobox(root,values=languageV,font="NORMAL")
combo2.place(x=680,y=40)
combo2.set("Selected language")

label2=tk.Label(root,text="ENGLISH",width=40,height=2,relief=GROOVE,font="bold",bg='orange')
label2.place(x=610,y=80)

#first frame
f=tk.Frame(root,bg="black",bd=5)
f.place(x=30,y=140,width=440,height=200)

text1=Text(f,font="NORMAL",bg="white",relief=GROOVE,wrap=WORD,bd=5)
text1.place(x=0,y=0,width=440,height=200)

scrollbar1=Scrollbar(f)
scrollbar1.pack(side="right",fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#second frame
f1=tk.Frame(root,bg="black",bd=5)
f1.place(x=610,y=140,width=440,height=200)


text2=Text(f1,font="NORMAL",wrap=WORD,bd=5)
text2.place(x=0,y=0,width=440,height=200)

scrollbar2=Scrollbar(f1)
scrollbar2.pack(side="right",fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)


#translate button
translate=tk.Button(root,text="Translate",cursor="hand2",bg="sky blue",fg="dark green",width=18,height=2,relief="solid",command=TranslateNow)
translate.place(x=473,y=300)


label_change()
root.mainloop()
