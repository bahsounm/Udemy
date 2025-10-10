import tkinter as tk
from word_extract import EngToArabic

BACKGROUND_COLOR = "#B1DDC6"
front = True
with open("score.txt", "r") as f:
        index = int(f.read())
dict_of_words = EngToArabic().get_dict()
# ---------------------------- Function SETUP ------------------------------- #
def handle_answer(is_right):
    global index
    index += 1
    with open("score.txt", "w") as f:
        f.write(str(index))

    filename = "words_right.txt" if is_right else "words_wrong.txt"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{en_word.cget('text')},{ar_word.cget('text')}\n")

    en_word.config(text=dict_of_words[index]["English"])
    ar_word.config(text=dict_of_words[index]["Arabic"])

def right():
    handle_answer(True)

def wrong():
    handle_answer(False)
    
def flip_card():
    global front, card_front_img, card_back_img

    if front:
        flip_button.config(bg="#91c2af",activebackground="#91c2af")
        canvas.itemconfig(image_on_canvas, image=card_back_img)
        
        ar_word.grid_forget()
        
        lang_label.config(text="English",bg="#91c2af")
        
        en_word.grid(column=1, row=2)
        en_word.config(bg="#91c2af")
        
        front = False
    else:
        flip_button.config(bg="white",activebackground="white")
        canvas.itemconfig(image_on_canvas, image=card_front_img)
        
        en_word.grid_forget()

        lang_label.config(text="Arabic", bg="white")
        
        ar_word.grid(column=1, row=2)
        ar_word.config(bg="white")

        front = True
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Flash Card Studying")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# ---------------------------- Canvas ------------------------------- #
canvas = tk.Canvas(width=800, height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tk.PhotoImage(file="images/card_front.png")
card_back_img = tk.PhotoImage(file="images/card_back.png")
image_on_canvas = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=3,rowspan=5)
# ---------------------------- Grid SETUP ------------------------------- #
# Langauge Label
lang_label = tk.Label(text="Arabic",font=("Arial", 30, "bold", "italic"), bg="white")
lang_label.grid(column=1, row=1)
# =================================================================================
# Word to study
ar_word = tk.Label(text=dict_of_words[index]["Arabic"],font=("Arial", 40), bg="white")
ar_word.grid(column=1, row=2)

en_word = tk.Label(text=dict_of_words[index]["English"],font=("Arial", 40), bg="white")
en_word.grid_forget()
# =================================================================================
# Correct Button
cor_image = tk.PhotoImage(file="images/right.png")
correct_button = tk.Button(image=cor_image, bd=0,bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, command=right)
correct_button.grid(column=2, row=5, sticky="EW")
# =================================================================================
# Incorrect Button
incor_image = tk.PhotoImage(file="images/wrong.png")
incorrect_button = tk.Button(image=incor_image, bd=0, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, command=wrong)
incorrect_button.grid(column=0, row=5, sticky="EW")
# =================================================================================
# Flip Button
flip_image = tk.PhotoImage(file="images/flip.png")
flip_button = tk.Button(image=flip_image, bd=0, bg="white", activebackground="white", command=flip_card)
flip_button.grid(column=1, row=3)
# =================================================================================
window.mainloop()