from tkinter import *
from tkinter import messagebox, ttk
import random
import string
root = Tk()
root.title("Pembuat Password Simpel")
root.geometry("350x200")
n = StringVar()
password = StringVar()
data = '@$%#!&_*' + string.ascii_letters + string.digits
len = Label(root, text='Setel Kekuatan: ', font=('ariel 15 bold'))
len.place(x=40, y=40)
combo = ttk.Combobox(root, width=8, textvariable=n, font=('ariel 15 bold'))
combo['values'] = [i for i in range(6,13)]
combo.place(x=193, y=40)
paswd = Label(root, textvariable=password, font=('ariel 12 bold'), fg='red')
paswd.place(x=20, y=140)
def generate():
    try:
        if n.get()=='':
            messagebox.showinfo("Pembuat Password", "Please select the Length for your Password")
        passw = random.choices(data, k=int(n.get()))
        password.set("Generated Password is: "+''.join(passw))
    except:
        pass
gen = Button(root, text='Buat', bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=generate)
gen.place(x=125, y=90)
root.mainloop()