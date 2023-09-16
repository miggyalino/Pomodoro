import tkinter
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
marks = ""
timer = None


def reset_timer():
    global marks
    global reps
    reps = 0
    marks = ""

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", fg="GREEN")
    repititions.config(text="")


def start_timer():
    global marks
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(5)
        label.config(text="BREAK", fg=RED)
        marks += "✓"
        repititions.config(text=marks)
    elif reps % 2 == 0:
        count_down(1)
        label.config(text="BREAK", fg=PINK)
        marks += "✓"
        repititions.config(text=marks)
    else:
        count_down(3)
        label.config(text="WORK", fg=GREEN)


# COUNTDOWN MECHANISM #
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10 and count_sec > 0:
        count_sec = f"0{count_sec}"
    if count_sec == 0:
        count_sec = "00"
    if count_min == 0 and count_sec == 0:
        count_min = "00"
        count_sec = "00"
    if count_min == 0:
        count_min = "00"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# UI SETUP #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = tkinter.Label(text="Timer", font=(FONT_NAME, 36, "bold"), fg=GREEN, bg=YELLOW)
label.grid(row=0, column=1)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(row=1, column=1)

start_button = tkinter.Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)
reset_button = tkinter.Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

repititions = tkinter.Label(
    text=marks, font=(FONT_NAME, 18, "bold"), fg=GREEN, bg=YELLOW
)
repititions.grid(column=1, row=3)

window.mainloop()
