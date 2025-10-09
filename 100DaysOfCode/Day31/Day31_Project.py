BACKGROUND_COLOR = "#B1DDC6"

import tkinter as tk

# ---------------------------- Function SETUP ------------------------------- #
def right():
    print("Right")

def wrong():
    print("Wrong")

def display_new_word():
    pass

def flip_card():
    pass

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Flash Card Studying")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# ---------------------------- Canvas ------------------------------- #
canvas = tk.Canvas(width=800, height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
lock_img = tk.PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=lock_img)
canvas.grid(column=0, row=0, columnspan=3,rowspan=5)
# ---------------------------- Grid SETUP ------------------------------- #
# Langauge Label
ar_label = tk.Label(text="Arabic",font=("Arial", 30, "bold", "italic"), bg="white")
ar_label.grid(column=1, row=1)
# =================================================================================
# Word to study
ar_word = tk.Label(text="هناك",font=("Arial", 40), bg="white")
ar_word.grid(column=1, row=2)
# =================================================================================
# Correct Button
cor_image = tk.PhotoImage(file="images/right.png")
correct_button = tk.Button(image=cor_image, bd=0,bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, command=right)
correct_button.grid(column=2, row=5)
# =================================================================================
# Incorrect Button
incor_image = tk.PhotoImage(file="images/wrong.png")
incorrect_button = tk.Button(image=incor_image, bd=0, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, command=wrong)
incorrect_button.grid(column=0, row=5)
# =================================================================================
# Flip Button
flip_image = tk.PhotoImage(file="images/repeat.png")
flip_button = tk.Button(image=flip_image, bd=0, bg="white", activebackground="white", command=flip_card)
flip_button.grid(column=1, row=3)
# =================================================================================
window.mainloop()