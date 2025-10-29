import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
checks = ""
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(id=timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, checks

    if reps == 0 or reps == 2 or reps == 4 or reps == 6:
        count_down(WORK_MIN*60)
        reps += 1
        timer_label.config(text="Timer", fg=GREEN)
    elif reps == 1 or reps == 3 or reps == 5:
        count_down(SHORT_BREAK_MIN*60)
        checks += "✔"
        checks_label.config(text= checks)
        reps += 1
        timer_label.config(text="Break", fg=PINK)
    elif reps == 7:
        count_down(LONG_BREAK_MIN*60)
        reps = 0 
        timer_label.config(text="Break",fg=RED)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = math.floor(count / 60)
    if minutes < 10:
        minutes = "0"+ str(minutes)
    seconds = count % 60
    if seconds < 10:
        seconds = "0" + str(seconds)
    canvas.itemconfig(timer_text, text="{}:{}".format(minutes,seconds))
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.minsize(width=400, height=400)
window.config(padx=100, pady=50, bg=YELLOW)
#======================================================================================================================
# timer label
timer_label = tk.Label(text="Timer", bg=YELLOW,fg=GREEN, highlightthickness=0, font=(FONT_NAME, 35,"bold")).pack()
#======================================================================================================================
#======================================================================================================================
canvas = tk.Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img) # play aournd with numbers if image is cut off
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()
#======================================================================================================================
start_button = tk.Button(text="Start",command=start_timer).place(x=-20, y=300)
reset_button = tk.Button(text="Reset", command=reset_timer).place(x=175, y=300)
#======================================================================================================================
checks_label = tk.Label(text=checks, bg=YELLOW, font=(FONT_NAME, 15)).place(y=300, x=60)
#======================================================================================================================
window.mainloop()