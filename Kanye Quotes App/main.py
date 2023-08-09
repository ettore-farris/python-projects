from tkinter import *
import requests

FONT = "Arial", 20, "bold"

quote = "Start here"
API_URL = "https://api.kanye.rest"

def get_quote():
    global quote
    data = requests.get(url=API_URL)
    quote = data.json()["quote"]
    canvas.itemconfig(quote_text, text=quote)

    print(quote)   
 
    
window = Tk()
window.title("Kanye Sais...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img )
quote_text = canvas.create_text(150, 207, text=f"{quote}", width=250, font=(FONT), fill="white")
canvas.grid(row=0, column=0)

kanye_face = PhotoImage(file="kanye.png")
btn = Button(image=kanye_face, highlightthickness=0, command=get_quote)
btn.grid(column=0, row=1)


window.mainloop()