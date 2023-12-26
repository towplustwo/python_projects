from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#3D0000" #"#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
   window.after_cancel(timer)
   canvas.itemconfig(timer_text, text = "00:00")
   timer_lb.config(text = "Timer")
   tick_lb.config( text = "")
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
       timer_lb.config(text = "Break", fg= RED)
       count_down(long_break_sec)
       
    elif reps % 2 == 0:
       timer_lb.config(text = "Break", fg = PINK)
       count_down(short_break_sec)
       
    else:
       count_down(work_sec)
       timer_lb.config(text = "Work", fg = GREEN)
       
       

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor( count / 60 )
    count_sec = count % 60
    if count_sec < 0:
       count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")

    if count > 0:  
      global timer     
      timer = window.after(2, count_down, count-1)
    else:
       start_timer()
       mark = ""
       work_sessions = math.floor(reps/2)
       for _ in range(work_sessions):
          mark += "✔"
       tick_lb.config(text = mark)
       if reps > 8:
          reset_timer()
          
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg= YELLOW)


canvas = Canvas(width = 200, height = 224, bg= YELLOW, highlightthickness= 0)
tamato_img = PhotoImage(file= "C:/Users/hk339/OneDrive/Documents/Web-Dev/Python_projects/pomodoro-start/tomato.png")
canvas.create_image( 100, 112, image = tamato_img)
timer_text = canvas.create_text( 100, 138, text = "00:00", fill= "white", font=(FONT_NAME, 26, "bold"))
canvas.grid(column= 1, row = 1)


timer_lb = Label(text = "Timer", fg= GREEN, font= (FONT_NAME, 40, "bold"), bg= YELLOW, highlightthickness= 0)
timer_lb.grid(column = 1, row = 0)

start_bt = Button(text ="Start",command = start_timer, highlightthickness= 0, border= 0)
start_bt.grid(column = 0, row = 2)

reset_bt = Button(text = "Reset",command= reset_timer, highlightthickness= 0, border= 0)
reset_bt.grid(column = 2, row = 2)

tick_lb = Label( fg= GREEN, bg= YELLOW, font=(FONT_NAME, 15))
tick_lb.grid(column = 1, row = 3)

window.mainloop()