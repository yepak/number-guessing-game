import tkinter as tk
import random as rd

window = tk.Tk()
window.geometry("600x400")
window.config(bg="black")
window.resizable(width=False,height=False)
window.title('Number Guessing Game')
# ----------------
number = rd.randint(0,1000)
tried = 0

def update_result(text):
    result.configure(text=text)
    
def new_game():
    guess_btn.config(state="normal")
    global number, tried
    number = rd.randint(0,1000) 
    tried = 0
    update_result(text="Guess the number between\n1 and 1000")

def play_game():
    global tried
    choice = int(number_form.get())
    if choice != number:
        tried += 1

        result = "Wrong Guess!! Try Again"
        if number < choice:
            hint = f"The required number lies between 0 and {choice}"
        else:
            hint = f"The required number lies between {choice} and 1000"
        result += "\nHINT:\n" + hint
    else:
        result = f"You guessed the correct number after {tried} retries"
        guess_btn.configure(state='disabled')
        result += "\n"+"Click on Play Game for start a new game"
    
    update_result(result)

# ------------

title = tk.Label(window,text="Number Guessing Game",font=("Arial",24),fg="red",bg="black")
title.place(x=125,y=10)
result = tk.Label(window,text="Click on Play Game for start a new game",font=("Arial",12,"normal","bold"),fg="red",bg="black",justify=tk.LEFT)
result.place(x=150,y=70)

ply_btn = tk.Button(window,text="Play Game",font=("Arial",14,"bold"),fg="red",bg="White", command=new_game)
ply_btn.place(x=250,y=150)

guess_btn = tk.Button(window,text="Guess",font=("Arial",13,"bold"),state="disabled",fg="red",bg="White",command=play_game)
guess_btn.place(x=275,y=220)

ext_btn = tk.Button(window,text="Exit Game",font=("Arial",11,"bold"),fg="Red",bg="White", command=exit)
ext_btn.place(x=505,y=360)

guessed_number = tk.StringVar()
number_form = tk.Entry(window,font=("Arial",11),textvariable=guessed_number)
number_form.place(x=223,y=193)

window.mainloop()