import tkinter as tk
from tkinter import scrolledtext
import re

def initial_state():
    display_message("Hi there! I hope you're doing okay? I'm here to assist you in all the ways I can. So please tell me, how can I help you?")
    entry.focus()

def handle_input(event=None):
    user_input = entry.get().strip()
    if user_input:
        display_message(user_input, is_user=True)
    entry.delete(0, tk.END)
    user_input_lower = user_input.lower()

    if re.search(r'real person|human|911|emergency', user_input_lower):
        emergency_contact()
    elif re.search(r'lost|help', user_input_lower):
        lost_help()
    elif re.search(r'scared|afraid|fear', user_input_lower):
        scared_help()
    else:
        default_response()

def emergency_contact():
    display_message("It seems like you need to talk to a real person. Please contact emergency services at 911.")
    final_state()

def lost_help():
    display_message("I understand you're feeling lost and need help. Let's talk about it. How can I make you feel less anxious?")
    entry.bind('<Return>', lambda event: lost_help_follow_up())
    submit_button.config(command=lost_help_follow_up)

def lost_help_follow_up():
    user_input = entry.get().strip()
    if user_input:
        display_message(user_input, is_user=True)
    entry.delete(0, tk.END)
    display_message("Distress signal online. Rescue team on its way.")
    final_state()

def scared_help():
    display_message("I understand you're feeling scared. Everything is going to be alright. Let's talk more about what's scaring you.")
    entry.bind('<Return>', lambda event: scared_help_follow_up())
    submit_button.config(command=scared_help_follow_up)

def scared_help_follow_up():
    user_input = entry.get().strip()
    if user_input:
        display_message(user_input, is_user=True)
    entry.delete(0, tk.END)
    display_message("It's okay to feel scared. You're not alone. We'll get through this together.")
    entry.bind('<Return>', lambda event: scared_help_follow_up_2())
    submit_button.config(command=scared_help_follow_up_2)

def scared_help_follow_up_2():
    user_input = entry.get().strip()
    if user_input:
        display_message(user_input, is_user=True)
    entry.delete(0, tk.END)
    display_message("Remember, you're safe and help is on the way if needed.")
    final_state()

def default_response():
    display_message("Distress signal online. Rescue team on its way.")
    final_state()

def final_state():
    display_message("Don't worry, everything will be fine. Someone will soon arrive and help you!")
    entry.config(state=tk.DISABLED)
    submit_button.config(state=tk.DISABLED)

def display_message(message, is_user=False):
    chat_log.config(state=tk.NORMAL)
    if is_user:
        chat_log.insert(tk.END, f"You: {message}\n")
    else:
        chat_log.insert(tk.END, f"RoverAi: {message}\n")
    chat_log.yview(tk.END)
    chat_log.config(state=tk.DISABLED)

# Initialize the main window
root = tk.Tk()
root.title("Assistance Bot")

# Create the chat log
chat_log = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create the entry widget for user input
entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=(0, 10), fill=tk.X)
entry.bind('<Return>', handle_input)

# Create the submit button
submit_button = tk.Button(root, text="Submit", command=handle_input)
submit_button.pack(padx=10, pady=(0, 10))

# Start the initial state
initial_state()

# Run the main loop
root.mainloop()
