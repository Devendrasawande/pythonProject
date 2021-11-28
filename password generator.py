from tkinter import *
import pyperclip
import random
import math
from tkinter import messagebox

root=Tk()
root.geometry('350x350')
root.title('python Mini project')

passstr = StringVar()
passlen_smallalpha = IntVar()
passlen_bigalpha = IntVar()
passlen_digits = IntVar()
passlen_specialcharc = IntVar()
passstr1 = StringVar()

passlen_smallalpha.set(0)
passlen_bigalpha.set(0)
passlen_digits.set(0)
passlen_specialcharc.set(0)

def generate():

    list1=[]
    small=passlen_smallalpha.get()
    big=passlen_bigalpha.get()
    digits=passlen_digits.get()
    special=passlen_specialcharc.get()

    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
             'w', 'x', 'y', 'z']

    pass2 = ['A', 'B', 'C', 'D', 'E', 'F','G','H','I', 'J', 'K',
             'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V'
             'W', 'X', 'Y','Z']

    pass3 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0' ]

    pass4 = ['!', '@', '#', '$', '%', '&', '*']

    password = ""
    mylist=[pass1,pass2,pass3,pass4]
    k=1

    while(k==1):
        random.shuffle(mylist)
        list1=mylist
        for q in range(4):
            if(list1[q][0]=='A' and big!=0):
                password = password + random.choice(pass2)
                big-=1
            if(list1[q][0]=='a' and small!=0):
                password = password + random.choice(pass1)
                small-=1
            if(list1[q][0]=='1' and digits!=0):
                password = password + random.choice(pass3)
                digits-=1
            if(list1[q][0]=='!' and special!=0):
                password = password + random.choice(pass4)
                special-=1

        if(small==0 and big==0 and digits==0 and special==0):
            break

    passstr.set(password)

def copy_to_clipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)

def module_1():
    f1=Frame()
    f1.place(x=0,y=0,width=350,height=350)
    Label(f1, text="Password Generator", font="calibre 20 bold").pack()

    Label(f1, text="Enter No. of Small Aplhabets").pack(pady=3)
    Entry(f1, textvariable=passlen_smallalpha).pack(pady=3)

    Label(f1, text="Enter No. of Big Alphabets").pack(pady=3)
    Entry(f1, textvariable=passlen_bigalpha).pack(pady=3)

    Label(f1, text="Enter No. of Digits").pack(pady=3)
    Entry(f1, textvariable=passlen_digits).pack(pady=3)

    Label(f1, text="Enter No. of Special Characters").pack(pady=3)
    Entry(f1, textvariable=passlen_specialcharc).pack(pady=3)

    Button(f1, text="Generate Password", command=generate).pack(pady=7)
    Entry(f1, textvariable=passstr).pack(pady=3)
    Button(f1, text="copy to Clipboard", command=copy_to_clipboard).pack()
    Button(f1, text='->', command=home).place(x=0,y=0)

def check_ch():
    f1=Frame()
    f1.place(x=0,y=0, width=350,height=350)
    string = passstr1.get()
    alphabets=digits=special=0

    for i in range (len(string)):
        if(string[i].isalpha()):
            alphabets=alphabets+1
        elif(string[i].isdigit()):
            digits=digits+1
        else:
            special=special+1
    b=Button(f1,text="->", command=module_2)
    b.place(x=0,y=0)
    l1=Label(f1, text={"alpabets", alphabets})
    l1.pack()
    l2=Label(f1, text={"digits", digits})
    l2.pack()
    l3=Label(f1, text={"Special Symbol", special})
    l3.pack()

def module_2():
    f1=Frame()
    f1.place(x=0,y=0, width=350, height=350)
    label=Label(f1, text="Enter Your Password")
    label.pack()
    entry=Entry(f1, textvariable=passstr1)
    entry.pack()
    b=Button(f1, text="Check Character", command=check_ch)
    b.pack()
    b1=Button(f1, text="->", command=home)
    b1.place(x=0,y=0)

def home():
    f1=Frame()
    f1.place(x=0,y=0,width=350,height=350)
    label=Label(f1, text="Click On Button to Select a Module")
    label.pack()
    button_1=Button(f1, text="Random Password Generator", command=module_1)
    button_1.place(x=100,y=50)
    button_2=Button(f1, text="Character Type check", command=module_2)
    button_2.place(x=117,y=150)

home()
root.mainloop()



