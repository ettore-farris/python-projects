from tkinter import *
from tkinter import messagebox
from pandas import *
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
DELAY = 5000

#----------------------------------DATA PROCESSING----------------------------------#

try:
    data = read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    initial_data = read_csv("./data\sardinian_words.csv.csv")
    to_learn = initial_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

current_card = {"./data/words_to_learn.csv"}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    sardinian_word = current_card.get("Sardinian")
    
    canvas.itemconfig(card_title,text="Sàrdu", fill="black")
    canvas.itemconfig(card_word,text=sardinian_word, fill="black")
    canvas.itemconfig(card_image, image=card_front_img)
    flip_timer = window.after(DELAY, func=flip_card)

def flip_card():
    english_word = current_card.get("English")
    canvas.itemconfig(card_title,text="English", fill="white")
    canvas.itemconfig(card_word,text=english_word, fill="white")
    canvas.itemconfig(card_image, image=card_back_img)
    
def is_known():
    to_learn.remove(current_card)
    data = DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", sep=',')
    next_card()

def reset():
    global to_learn
    is_ok = messagebox.askyesno(title="Are you sure?", message="Are you sure you want to reset your progresses?")
    if is_ok:
        to_learn = initial_data.to_dict(orient="records")


#----------------------------------GUI----------------------------------#

window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(DELAY, func=flip_card)

#canvas
canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="./images\card_front.png")
card_back_img = PhotoImage(file="./images\card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

#text
card_title = canvas.create_text(400, 150, font=LANG_FONT, text="")
card_word = canvas.create_text(400, 263, font=LANG_FONT, text="")

#buttons
right_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, borderwidth=0, highlightthickness=0, command=is_known)
right_btn.grid(column=0, row=1)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, borderwidth=0, highlightthickness=0, command=next_card)
wrong_btn.grid(column=1, row=1)

reset_btn = Button(text="Reset", command=reset)
reset_btn.grid(column=1, row=3, pady=50)


next_card()
window.mainloop()

