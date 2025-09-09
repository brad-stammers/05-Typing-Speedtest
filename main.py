###################################################################################################
#   100 Days of Code: The Complete Python Pro Bootcamp
#   Portfolio Assignment 05 - Typing Speedtest
###################################################################################################

import tkinter as tk
from dotenv import load_dotenv
import os

# initialise
load_dotenv()
BACKGROUND = os.environ["BACKGROUND_COLOUR"]
WORD_LIST = os.environ["WORDS"]
timer = None
print(WORD_LIST)

#set up timer mechanism
def start_timer():
    typing.config(state="normal")
    typing.focus_set()
    count_down(15)

def count_down(count):
    timer_text.config(text=f"{count}")
    global timer
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        typing.config(state="disabled")
        check_correct_words()

def check_correct_words():
    base_words = WORD_LIST.split(" ")
    typed_words = typing.get("1.0", "end-1c").split(" ")
    correct_count = 0
    for ctr in range(len(typed_words)):
        if typed_words[ctr] == base_words[ctr]:
            correct_count += 1

    #output result
    result_label.config(text=f"Result: {correct_count} WPM")



# UI setup
window = tk.Tk()
window.title("Typing Speedtest")
window.config(padx=50, pady=20, width=800, height=400, bg=BACKGROUND)

result_label = tk.Label(text="", fg="red", bg=BACKGROUND, font=("Arial", 24))
result_label.config(pady=10)
result_label.grid(column=0, row=0, columnspan=2)

timer_label = tk.Label(text="Timer: ", fg="black", bg=BACKGROUND, font=("Arial", 24))
timer_label.config(pady=10)
timer_label.grid(column=0, row=1)
timer_text = tk.Label(text="60", fg="darkblue", bg=BACKGROUND, font=("Arial", 20))
timer_text.grid(column=1, row=1)

word_list = tk.Text(width=50, height=10, bg="lightgrey", fg="darkblue", wrap="word", font=("Arial", 12))
word_list.insert("1.0", WORD_LIST)
word_list.config(state="disabled")
word_list.grid(column=0, row=2, columnspan=2)

spacer = tk.Label(text=" ",bg=BACKGROUND)
spacer.grid(column=0, row=3, columnspan=2)

typing = tk.Text(width=50, height=10, bg="white", fg="darkgreen", font=("Arial", 12))
typing.config(pady=20,state="disabled")
typing.grid(column=0, row=4, columnspan=2)

start_button = tk.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=5, columnspan=2)


window.mainloop()