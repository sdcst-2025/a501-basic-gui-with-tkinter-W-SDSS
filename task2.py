import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")
window.geometry("500x200")
window.attributes("-topmost", True)

dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)
label2 =tk.Label(window, text="Client Database")
button1=tk.Button(window, text="Serch by Name", relief=GROOVE)
entry1 = tk.Entry(window, width=10)

label3=tk.Label(window, text="Name")
label4=tk.Label(window, text="Type")
label5=tk.Label(window, text="Breed")
label6=tk.Label(window, text="Owner")
label7=tk.Label(window, text="Birthdate")

entry2=tk.Entry(window, width=80, relief=GROOVE)
entry3=tk.Entry(window, width=80, relief=GROOVE)
entry4=tk.Entry(window, width=80, relief=GROOVE)
entry5=tk.Entry(window, width=80, relief=GROOVE)
entry6=tk.Entry(window, width=80, relief=GROOVE)



label1.place(x=10, y=0)
label2.place(x=200, y=50)
button1.place(x=400, y=0)
entry1.place(x=450, y=0)

label3.place(x=20, y=100)
label4.place(x=110, y=100)
label5.place(x=200, y=100)
label6.place(x=290, y=100)
label7.place(x=380, y=100)

entry2.place(x=0, y=110)
entry3.place(x=90, y=110)
entry4.place(x=180, y=110)
entry5.place(x=270, y=110)
entry6.place(x=360, y=110)


window.mainloop()