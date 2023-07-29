# ---------------------------- CONSTANTS ------------------------------- #
from tkinter import *
import math
import winsound

duration = 1000  # milliseconds
freq = 440  # Hz


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 20
reps = 0
stop = True

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    global reps
    global stop
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")
    reps = 0
    stop = True
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def countdown_starter():
    global reps
    global stop
    stop = False
    reps += 1
    work_min = WORK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    
    if reps % 8 == 0:    #if reps 8
        countdown(long_break)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:   #if reps 2, 4 or 6    
        countdown(short_break)
        timer_label.config(text="Short Break", fg=PINK)
    else:    #if reps 1, 3, 5, or 7 // add sound every completed working session
        countdown(work_min)
        timer_label.config(text="Work!", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(n):
    global stop
    count_minutes = math.floor(n/60)
    count_seconds = n%60
    if count_seconds <10:
        count_seconds = f"0{count_seconds}"
    
    if stop == False:
        canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
        if n > 0:
            window.after(1000, countdown, n-1)
        else:
            countdown_starter()
            #add checkmarks
            marks = ""
            work_sessions = math.floor(reps/2)
            for i in range(work_sessions):
                marks += "✓"
                checkmark.config(text=f"{marks}")


# ---------------------------- UI SETUP ------------------------------- #

#window
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=100, bg=YELLOW)


#label
timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
timer_label.grid(column=1, row=0)

#canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=r"Tkinter\Pomodoro Timer\tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 112, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)

#buttons
start_btn = Button(text="Start", command=countdown_starter)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", command=reset)
reset_btn.grid(column=2, row=2)

#checkmark
checkmark = Label(fg=GREEN, bg=YELLOW, font=("Arial", 10, "bold"))
checkmark.grid(column=1, row=3)


window.mainloop()