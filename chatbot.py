import tkinter as tk
import re
import random

# For speech recognition, you can use libraries like SpeechRecognition

keywords_responses = {
    "hello": ["Hi","hey there", "greetings"],  
    "how are you": ["I'm doing well, thanks for asking! How about you?"],
    " I am fine how was your day": ["It's good but too much hectic. How was yours?"],
    "motivate me for studies": ["How can I help you get motivated?"],
    "I know but how can I be consistent": ["You should have to be consistent towards your studies as studies play a vital role in building your future. What are some specific challenges you face with consistency?"],
    "I get bored and distracted": ["Let's explore some strategies to reduce distractions. Would you like to set up a study schedule or use time management techniques?"],
    "great!!!": ["I'm glad it helped!"],
    "Thanks for helping me :)": ["You're welcome! I'm here to support you in your studies. What else can I help you with today?"],
    "bye": ["Goodbye! Have a great day!"]
}

def process_input(user_input):
    for keyword, responses in keywords_responses.items():
        if keyword in user_input:
            return random.choice(responses)
    return "I didn't understand that. Can you rephrase or try a different question?"

def chatbot():
    root = tk.Tk()
    root.title("Chatbot")

    user_input_text = tk.Text(root, height=5, width=50)
    user_input_text.pack()

    chatbot_output = tk.Text(root, height=5, width=50, state=tk.DISABLED)
    chatbot_output.pack()

    def send_message():
        user_input = user_input_text.get("1.0", tk.END).strip()
        user_input_text.delete("1.0", tk.END)

        response = process_input(user_input)
        chatbot_output.config(state=tk.NORMAL)
        chatbot_output.insert(tk.END, f"YOU: {user_input}\n")
        chatbot_output.insert(tk.END, f"Chatbot: {response}\n")
        chatbot_output.config(state=tk.DISABLED)
        chatbot_output.see(tk.END)  # Scroll to the bottom after each message

    send_button = tk.Button(root, text="Send", command=send_message)
    send_button.pack()

    root.mainloop()

if __name__ == "__main__":
    chatbot()