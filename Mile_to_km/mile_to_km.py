from tkinter import *

window=Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=500)
window.config(padx=50, pady=50)

# Label
label1 = Label(text="is equal to ",font=("Arial",20,"normal"))
label1.grid(row=1, column=0)
label1.config(padx=10)

# Entry
input = Entry(width=7)
input.grid(row=0, column=1)
# mile = float(input.get())

# label_miles
label_miles = Label(text="Miles",font=("Arial",18,"normal"))
label_miles.grid(row=0, column=2)
label_miles.config(padx=20)

# Label answer
label_answer = Label(text=0, font=("Arial",24,"bold"))
label_answer.grid(row=1, column=1)

# Label Km
label_km = Label(text="Km", font=("Arial",18,"normal"))
label_km.grid(row=1, column=2)

# Button calculate

def button_clicked():
    eqvivalent_km = round(float(input.get())*1.609)
    label_answer.config(text=eqvivalent_km)

button = Button(text="Calculate", command = button_clicked)
button.grid(row=2,column=1)
button.config(pady=10)


window.mainloop()
