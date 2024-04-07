import random
from tkinter import *
import pyperclip 

root = Tk()
root.geometry("375x350")
root.title('Password Generator')
root.configure(bg='#ffdb4d')
password = ""



def generate(small,caps,spc,num,sym):
    global password
    
    len = int(e.get())
    
    alpha_small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alpha_caps = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    space = [' ']
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    symbols = ["~","!","@","#","$","%","^","&","*","(",")","_","+","-","=","{","}","|","[","]","/","?","<",">"]

    pwdList = []
    copy = ''
    
    #print(length.get())

    while(len>0):
        if len == 0:
            break
        if (small):
            char = random.choice(alpha_small)
            pwdList.append(char)
            len = len - 1
        
        if (caps):
            char = random.choice(alpha_caps)
            pwdList.append(char)
            len = len - 1

        if (spc):
            char = random.choice(space)
            pwdList.append(char)
            len = len - 1
        
        if (num):
            char = random.choice(numbers)
            pwdList.append(char)
            len = len - 1

        if (sym):
            char = random.choice(symbols)
            pwdList.append(char)
            len = len - 1

    
    random.shuffle(pwdList)
    
    for i in pwdList:
        copy = copy + i
    
    pwdList = []
    password = copy
    copy = ''
    #output.insert(0,password)
    #print("Generated Password: ", password)
    
    return password

def display():
    pwd = generate(sml.get(),cpl.get(),spc.get(),n.get(),symb.get())
    print(pwd) 
    output.delete("0","end")
    output.insert(0,password)


def copyClipboard():
    pyperclip.copy(password)  

label=Label(root, text="Password Generator", font="TimesNewRoman 20 bold", pady=10, bg='#ffdb4d')
label.pack()
label = Label(root,text="Enter Length", bg='#ffdb4d')
label.pack()

e = Entry(root,width=30)
e.focus_set()
e.pack()

sml = IntVar()
cpl = IntVar()
spc = IntVar()
n = IntVar()
symb = IntVar()

letter_small = Checkbutton(root, text='Include Small Letters', variable=sml,bg='#ffdb4d').pack()
letter_caps = Checkbutton(root, text='Include Capital Letters', variable=cpl,bg='#ffdb4d').pack()
letter_space = Checkbutton(root, text='Include Blank Space', variable=spc,bg='#ffdb4d').pack()
letter_symbols = Checkbutton(root, text='Include Symbols', variable=symb,bg='#ffdb4d').pack()
letter_numbers = Checkbutton(root, text='Include Numbers', variable=n,bg='#ffdb4d').pack()

b = Button(root,text="Generate", command=display, bg='#66c2ff', padx=5)
b.pack(pady=10)

#b1 = Button(root,text='print',command=display)
#b1.pack()

output = Entry(root, width=30)
output.pack()


b2 = Button(root,text="Copy to Clipboard",command=copyClipboard, padx=8, pady=5, bg='#66c2ff')
b2.pack(pady=10)

root.mainloop()