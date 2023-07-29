import tkinter


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.maxsize(300, 200)
window.config(padx=70, pady=70)

#converter
def miles_to_km_converter():
    global miles_input
    km_number["text"] = float(miles_input.get()) *1.61

#miles input
miles_input = tkinter.Entry(width=7)
miles_input.grid(column=1, row=0)

#miles label
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

#km row
is_equal_to = tkinter.Label(text="Is equal to")
is_equal_to.grid(column=0, row=1)

km_number = tkinter.Label(text="0")
km_number.grid(column=1, row=1)

km = tkinter.Label(text="Km")
km.grid(column=2, row=1)

#button
btn = tkinter.Button(text="Calculate", command=miles_to_km_converter)
btn.grid(column=1, row=2)

window.mainloop()
