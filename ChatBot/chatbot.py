import tkinter as tk
from tkinter import scrolledtext
import spacy

# Load spaCy model for NLP processing
nlp = spacy.load('en_core_web_sm')

# Predefined simple responses
simple_responses = {
    "hi": "Hello! How can I help you today?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "bye": "Goodbye! Have a great day ahead.",
    "what is your name": "I am a simple chatbot created by you.",
    "thank you": "You're welcome!"
}

# Function to get a bot response based on simple logic and spaCy
def get_bot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in simple_responses:
        return simple_responses[user_input]

    doc = nlp(user_input)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return f"Nice to meet you, {ent.text}! How can I assist you today?"
        if ent.label_ == "GPE":
            return f"Oh, {ent.text} is a wonderful place! What would you like to know?"

    for token in doc:
        if token.pos_ == "VERB":
            return f"It sounds like you're talking about {token.text}. Can you tell me more?"

    return "I'm not sure I understand. Can you clarify that?"

# Function to update the chat window with user and bot messages
def send_message():
    user_message = input_box.get()
    if user_message:
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "You: " + user_message + "\n", "user_tag")

        bot_response = get_bot_response(user_message)
        chat_window.insert(tk.END, "Bot: " + bot_response + "\n\n", "bot_tag")

        chat_window.config(state=tk.DISABLED)
        chat_window.yview(tk.END)
        input_box.delete(0, tk.END)

def enter_pressed(event):
    send_message()

# Create the main window
root = tk.Tk()
root.title("Chatbot - Red Theme")

root.geometry("400x475")
root.config(bg='#FF3B30')

chat_window = scrolledtext.ScrolledText(
    root, wrap=tk.WORD, state=tk.DISABLED, height=20, width=50, font=("Helvetica", 12)
)
chat_window.pack(pady=10, padx=10)

# User and bot message styles updated for red theme
chat_window.tag_configure(
    "user_tag", foreground="white", background="#FF6347",  # Tomato Red
    justify="left", font=("Helvetica", 12, "bold"), relief=tk.RAISED, 
    lmargin1=10, lmargin2=10, rmargin=10
)
chat_window.tag_configure(
    "bot_tag", foreground="white", background="#B22222",  # Firebrick Red
    justify="right", font=("Helvetica", 12, "italic"), relief=tk.RAISED, 
    lmargin1=10, lmargin2=10, rmargin=10
)

input_frame = tk.Frame(root, bg='#FF3B30')
input_box = tk.Entry(input_frame, font=("Helvetica", 14), width=28)
input_box.pack(side=tk.LEFT, pady=10, padx=10)

send_button = tk.Button(
    input_frame, text="Send", command=send_message, 
    font=("Helvetica", 12), bg="#C41E3A",  # Crimson Red
    fg="white", width=8
)
send_button.pack(side=tk.RIGHT, pady=10, padx=10)

input_frame.pack(pady=0)

root.bind('<Return>', enter_pressed)
root.mainloop()
