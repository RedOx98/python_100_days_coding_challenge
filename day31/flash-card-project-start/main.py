from tkinter import Tk, Canvas, PhotoImage, Button
import pandas
import random

# ----------------------------- CONSTANTS ----------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FLIP_TIME = 3000  # milliseconds (3 seconds)

# ----------------------------- LOAD DATA ----------------------------- #
# Load words from CSV (we’ll add logic later for progress tracking)
try:
    data = pandas.read_csv("data/words_to_learn.csv")  # if user has prior progress
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

to_learn = data.to_dict(orient="records")  # [{"French": "partie", "English": "part"}, ...]
current_card = {}

# ----------------------------- NEXT CARD FUNCTION ----------------------------- #
def next_card():
    """Pick a random card and display the French word."""
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # cancel previous flip timer if user clicks early

    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)

    # set a timer to flip the card after 3 seconds
    flip_timer = window.after(FLIP_TIME, flip_card)

# ----------------------------- FLIP CARD FUNCTION ----------------------------- #
def flip_card():
    """Flip the card to show the English translation."""
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# ----------------------------- IS KNOWN FUNCTION ----------------------------- #
def is_known():
    """Remove known word and save remaining ones to CSV."""
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ----------------------------- UI SETUP ----------------------------- #
window = Tk()
window.title("Flashy Flashcards 💡")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(FLIP_TIME, flip_card)  # start initial timer

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)
known_button = Button(image=right_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

# Show first card
next_card()

# ----------------------------- START APP ----------------------------- #
window.mainloop()