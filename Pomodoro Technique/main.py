from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer  = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_canvas, text="00:00")
    timer_label.config(text="Timer")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    if reps%2 == 0:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)
        work_complete=True
    elif reps%7==0:
        timer_label.config(text="Long Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps%2!=0:
        timer_label.config(text="Short Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    reps+=1

    # count_down(1*60)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    min_time = int(count / 60)
    sec_time = int(count % 60)
    if sec_time == 0:
        sec_time="00"
    elif sec_time<10:
        sec_time = "0"+str(sec_time)
    if min_time == 0:
        min_time = "00"
    canvas.itemconfig(timer_canvas, text=str(min_time)+":"+str(sec_time))
    if count>0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer Label
timer_label = Label(text="Timer", font=(FONT_NAME,50,"bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0,column=1)


# Image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  #highlightthickness is for removing border around canvas
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(100,112, image = tomato_img)
timer_canvas = canvas.create_text(100,150,text="00:00", fill="white", font=(FONT_NAME,20,"bold"))
canvas.grid(row=1,column=1)

# Start Button
button_start = Button(text="Start", highlightthickness=0 , bd=0, font=(FONT_NAME,18,"bold"), bg=GREEN, command=start_timer)
button_start.grid(row=2,column=0)

# Reset Button
button_reset = Button(text="Reset", highlightthickness=0, bd=0, font=(FONT_NAME,18,"bold"), bg=GREEN, command=reset_timer)
button_reset.grid(row=2,column=2)


window.mainloop()
