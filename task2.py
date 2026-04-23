import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")
window.geometry("500x200")
window.attributes("-topmost", True)
window.configure(bg="white")

dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto, relief=FLAT)
label2 =tk.Label(window, text="Client Database", bg="white")
button1=tk.Button(window, text="Serch by Name", height=1, relief=GROOVE, bg="white")
entry1 = tk.Entry(window, width=15, relief=SOLID)

label3=tk.Label(window, text="Name", bg="white")
label4=tk.Label(window, text="Type", bg="white")
label5=tk.Label(window, text="Breed", bg="white")
label6=tk.Label(window, text="Owner", bg="white")
label7=tk.Label(window, text="Birthdate", bg="white")

entry2=tk.Entry(window, width=13, relief=SOLID, highlightbackground="lightgray")
entry3=tk.Entry(window, width=13, relief=SOLID, highlightbackground="lightgray")
entry4=tk.Entry(window, width=13, relief=SOLID, highlightbackground="lightgray")
entry5=tk.Entry(window, width=13, relief=SOLID, highlightbackground="lightgray")
entry6=tk.Entry(window, width=13, relief=SOLID, highlightbackground="lightgray")

button2 = tk.Button(window, text="< Previous", relief=GROOVE, bg="white")
button3 = tk.Button(window, text="Save Entry", relief=GROOVE, height=2)
button4 = tk.Button(window, text="Next >", relief=GROOVE, bg="white")



label1.place(x=10, y=0)
label2.place(x=200, y=40)
button1.place(x=300, y=0)
entry1.place(x=400, y=5)

label3.place(x=20, y=100)
label4.place(x=120, y=100)
label5.place(x=210, y=100)
label6.place(x=295, y=100)
label7.place(x=400, y=100)

entry2.place(x=5, y=120)
entry3.place(x=95, y=120)
entry4.place(x=185, y=120)
entry5.place(x=275, y=120)
entry6.place(x=390, y=120)

button2.place(x=2, y=160)
button3.place(x=190, y=150)
button4.place(x=450, y=160)


window.mainloop()

#frame no color ga black...gray ni sitai
#image no frame ga still gray...white or clear ni sitai
# 'search by my name' no kado nakusu