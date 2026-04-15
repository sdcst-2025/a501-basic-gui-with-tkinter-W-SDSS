import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")
window.geometry("500x200")
window.attributes("-topmost", True)
window.configure(bg="white")

dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)
label2 =tk.Label(window, text="Client Database")
button1=tk.Button(window, text="Serch by Name", height=5, relief=GROOVE)
entry1 = tk.Entry(window, width=20)

label3=tk.Label(window, text="Name")
label4=tk.Label(window, text="Type")
label5=tk.Label(window, text="Breed")
label6=tk.Label(window, text="Owner")
label7=tk.Label(window, text="Birthdate")

entry2=tk.Entry(window, width=13, relief=GROOVE)
entry3=tk.Entry(window, width=13, relief=GROOVE)
entry4=tk.Entry(window, width=13, relief=GROOVE)
entry5=tk.Entry(window, width=13, relief=GROOVE)
entry6=tk.Entry(window, width=13, relief=GROOVE)

button2 = tk.Button(window, text="< Previous", relief=GROOVE)
button3 = tk.Button(window, text="Save Entry", relief=GROOVE)
button4 = tk.Button(window, text="Next >", relief=GROOVE)



label1.place(x=10, y=0)
label2.place(x=200, y=40)
button1.place(x=300, y=0)
entry1.place(x=400, y=5)

label3.place(x=20, y=100)
label4.place(x=120, y=100)
label5.place(x=200, y=100)
label6.place(x=290, y=100)
label7.place(x=400, y=100)

entry2.place(x=5, y=120)
entry3.place(x=95, y=120)
entry4.place(x=185, y=120)
entry5.place(x=275, y=120)
entry6.place(x=390, y=120)

button2.place(x=0, y=150)
button3.place(x=230, y=150)
button4.place(x=450, y=150)


window.mainloop()