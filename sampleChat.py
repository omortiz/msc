from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

import tkinter as tk

try:
    import ttk as ttk
    import ScrolledText
except ImportError:
    import tkinter.ttk as ttk
    import tkinter.scrolledtext as ScrolledText
import time


class TkinterGUIExample(tk.Tk):

    def __init__(self, *args, **kwargs):
        """
        Create & set window variables.
        """
        tk.Tk.__init__(self, *args, **kwargs)

        self.chatbot = ChatBot(
            "Rob.ai",
            storage_adapter="chatterbot.storage.SQLStorageAdapter",
            logic_adapters=[
                "chatterbot.logic.BestMatch"
            ],
            database_uri="sqlite:///database.db"
        )

        # Greetings
        trainer = ChatterBotCorpusTrainer(self.chatbot)
        trainer.train(
            "chatterbot.corpus.english.greetings",
            "chatterbot.corpus.english.conversations"
        )

        # HR Questions
        trainer = ListTrainer(self.chatbot)

        trainer.train([
            "Hi, can I help you?",
            "Yes, I would like information about my 401K?",
            "Here is a link where you can find information about your 401K: https://www.irs.gov/retirement-plans/401k-plans"
            "Thanks Rob!",
            "You're welcome!"
        ])

        trainer.train([
            "Hi there! How can I help you?",
            "I need to know who is the CEO of the company",
            "The current CEO of MSC Software is Paolo Guglielmini."
            "Thanks Rob!",
            "You're welcome!"
        ])

        trainer.train([
            "Hi there! How can I help you?",
            "Who is the current CFO?",
            "The current CFO of MSC Software is Kevin Rubin."
            "Thanks Rob!",
            "You're welcome!"
        ])

        trainer.train([
            "How can I help you?",
            "When was the company founded?",
            "MSC Software was founded in 1963.",
            "Thanks Rob!",
            "You're welcome!"
        ])

        trainer.train([
            "Hi there! How can I help you?",
            "When was MSC Software founded?",
            "MSC Software was founded in 1963.",
            "Thanks Rob!",
            "You're welcome!"
        ])

        trainer.train([
            "Hello! How can I help you?"
            "What's the address of MSC Software?",
            "MSC Software is located at 4675 MacArthur Court Newport Beach, CA 92660.",
            "Okay thanks!",
            "Your're welcome! Is there anything else I can do for you?",
            "No, thanks!"
        ])

        trainer.train([
            "Hi! How can I help you?",
            "What's the company's address?",
            "MSC Software is located at 4675 MacArthur Court Newport Beach, CA 92660.",
            "Do you need anything else?",
            "No, thank you!",
            "Have a good day!",
            "Thanks, you too!"
        ])

        trainer.train([
            "Hi! How can I help you?",
            "What's the phone number of MSC Software?",
            "The phone number for MSC Software (714) 540-8900.",

        ])

        trainer.train([
            "Hi! How can I help you?",
            "What's MSC Software's phone number?",
            "The phone number for MSC Software (714) 540-8900.",

        ])

        self.title("Chatterbot")

        self.initialize()

    def initialize(self):
        """
        Set window layout.
        """
        self.grid()

        self.respond = ttk.Button(self, text='Get Response', command=self.get_response)
        self.respond.grid(column=0, row=0, sticky='nesw', padx=3, pady=3)

        self.usr_input = ttk.Entry(self, state='normal')
        self.usr_input.grid(column=1, row=0, sticky='nesw', padx=3, pady=3)

        self.conversation_lbl = ttk.Label(self, anchor=tk.E, text='Conversation:')
        self.conversation_lbl.grid(column=0, row=1, sticky='nesw', padx=3, pady=3)

        self.conversation = ScrolledText.ScrolledText(self, state='disabled')
        self.conversation.grid(column=0, row=2, columnspan=2, sticky='nesw', padx=3, pady=3)

    def get_response(self):
        """
        Get a response from the chatbot and display it.
        """
        user_input = self.usr_input.get()
        self.usr_input.delete(0, tk.END)

        response = self.chatbot.get_response(user_input)

        self.conversation['state'] = 'normal'
        self.conversation.insert(
            tk.END, "Human: " + user_input + "\n" + "ChatBot: " + str(response.text) + "\n"
        )
        self.conversation['state'] = 'disabled'

        time.sleep(0.5)


gui_example = TkinterGUIExample()
gui_example.mainloop()
