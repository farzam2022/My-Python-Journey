from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_text, text=current_card["French"])
    canvas.itemconfig(card_background, image=front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=current_card["English"])
    canvas.itemconfig(card_background, image=back_img)



def is_known():
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)



window = Tk()
window.title("Flash Card Program")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)


flip_timer = window.after(3000, func=flip_card)

front_img = PhotoImage(file="./images/card_front.png")
canvas = Canvas(bg=BACKGROUND_COLOR, width=800, height=526, highlightthickness=0)
back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


cross_img = PhotoImage(file="./images/wrong.png")
cross_button = Button(image=cross_img, highlightthickness=0, command=next_card)
cross_button.grid(row=1, column=0)

check_img = PhotoImage(file="./images/right.png")
tick_button = Button(image=check_img, highlightthickness=0, command=is_known)
tick_button.grid(row=1, column=1)


next_card()

window.mainloop()