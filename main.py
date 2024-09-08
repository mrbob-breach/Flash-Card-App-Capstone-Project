from tkinter import *
import pandas as pd
import random

words = {}

try:
    words = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    words = pd.read_csv("data/french_words.csv")
finally:
    words = words.to_dict(orient="records")
    random_word = {}


def next_card_correct():
    next_card()
    words.remove(random_word)
    words_df = pd.DataFrame(words)
    words_df.to_csv("data/words_to_learn.csv", index=False)


def next_card():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(words)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(canvas_title, text="French", fill="black")
    canvas.itemconfig(canvas_text, text=random_word['French'], fill="black")
    flip_timer = window.after(1000, func=card_flip)


def card_flip():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(canvas_title, text="English", fill="white")
    canvas.itemconfig(canvas_text, text=random_word['English'], fill="white")


# ---------------------------- UI SETUP ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(1000, func=card_flip)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas_title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
canvas_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=next_card_correct)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()
