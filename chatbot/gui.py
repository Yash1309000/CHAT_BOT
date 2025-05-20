import tkinter as tk

from chatbot import Chatbot

class ChatbotApp:
    def __init__(self, root):
        self.bot = Chatbot()
        self.root = root
        self.root.title("HDFC Bank NLP Chatbot")
        self.root.geometry("600x700")

        # Chat display with scrollbar
        self.chat_frame = tk.Frame(root)
        self.chat_frame.pack(padx=10, pady=(10,5), fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.chat_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.chat_display = tk.Text(self.chat_frame, bd=2, bg="#F9F9F9", fg="#333333",
                                    font=("Arial", 14), wrap=tk.WORD,
                                    yscrollcommand=self.scrollbar.set)
        self.chat_display.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.chat_display.config(state=tk.DISABLED)

        self.scrollbar.config(command=self.chat_display.yview)

        # Input and buttons
        input_frame = tk.Frame(root)
        input_frame.pack(padx=10, pady=10, fill=tk.X)

        self.user_input = tk.Entry(input_frame, bd=2, bg="white", fg="#000000",
                                   font=("Arial", 14))
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0,10))
        self.user_input.bind("<Return>", lambda event: self.send_message())

        self.send_button = tk.Button(input_frame, text="Send", bg="#4CAF50", fg="white",
                                     font=("Arial", 12, "bold"), width=8, command=self.send_message)
        self.send_button.pack(side=tk.LEFT)

        self.clear_button = tk.Button(root, text="Clear Chat", bg="#f44336", fg="white",
                                      font=("Arial", 12, "bold"), width=15, command=self.clear_chat)
        self.clear_button.pack(pady=(0,15))

        self.display_message("Bot", "Welcome! Ask me anything about HDFC Bank.")

    def display_message(self, sender, message):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)

    def send_message(self):
        user_msg = self.user_input.get().strip()
        if not user_msg:
            return
        self.display_message("You", user_msg)
        self.user_input.delete(0, tk.END)

        bot_response = self.bot.get_response(user_msg)
        self.display_message("Bot", bot_response)

    def clear_chat(self):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.delete(1.0, tk.END)
        self.chat_display.config(state=tk.DISABLED)
        self.display_message("Bot", "Chat cleared. Ask me anything about HDFC Bank.")

def run():
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()

if __name__ == "__main__":
    run()
