from tkinter import *
import requests

FONT = ("Ariel", 20, "bold")


def change_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(canvas_text, text=quote)


windows = Tk()
windows.title("Kanye says...")
windows.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(151.5, 207, image=background_img)
canvas_text = canvas.create_text(150, 207, text="   To know what Kanye says, press on the picture of Kanye 👇", width=250, font=FONT, fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(height=131, width=100, image=kanye_img, highlightthickness=0, command=change_quote)
kanye_button.grid(row=1, column=0)
windows.mainloop()
