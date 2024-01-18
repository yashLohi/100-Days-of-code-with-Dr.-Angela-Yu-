from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WHITE = "#ffffff"
FONT_NAME = "Times"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=WHITE)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=WHITE)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=WHITE)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60) # converted the sec in min
    count_sec = count % 60
    if count_sec == 10: # this give us single digit so to convert
        count_sec == f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)



window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=RED)
canvas = Canvas(width=348, height=303, bg=RED, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(175, 151, image=tomato_img)
timer_text = canvas.create_text(185, 180, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
timer_label = Label(text="Timer", fg=WHITE, bg=RED, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

check_image = PhotoImage(file="right.png")
start_button = Button(image=check_image, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

cross_image = PhotoImage(file="wrong.png")
reset_button = Button(image=cross_image, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=RED, font=(FONT_NAME, 25))
check_marks.grid(column=1, row=3)

window.mainloop()



