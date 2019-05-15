from chatterbot import ChatBot
from train import trainSet1,trainSet2,trainSet3
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
                {
                    'import_path': 'benefits_adapter.BenefitsAdapter',
                },
                {
                    'import_path': 'travel_adapter.TravelAdapter',
                },
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'default_response': 'I am sorry, but I do not understand.',
                    'maximum_similarity_threshold': 0.90
                }
            ],
            database_uri="sqlite:///database.db"
        )

        # train
        trainSet1(self.chatbot) #chatterbot greetings
        trainSet2(self.chatbot) #Nijjan HR questions
        trainSet3(self.chatbot) #MSC Software questions

        self.title("Rob.ai")

        self.initialize()

    def initialize(self):
        """
        Set window layout.
        """
        self.grid()

        self.respond = ttk.Button(self, text='Send', command=self.get_input)
        self.bind("<Return>", lambda x: self.get_input())
        self.respond.grid(column=1, row=1, sticky='nesw', padx=3, pady=3)

        self.usr_input = ttk.Entry(self, state='normal')
        self.usr_input.grid(column=0, row=1, sticky='nesw', padx=3, pady=3)

        self.conversation = ScrolledText.ScrolledText(self, state='disabled')
        self.conversation.grid(column=0, row=0, columnspan=1, sticky='nesw', padx=3, pady=3)

    def get_input(self):
        if (len(self.usr_input.get()) != 0):
            user_input = self.usr_input.get()
            self.usr_input.delete(0, tk.END)

            self.conversation['state'] = 'normal'
            self.conversation.insert(tk.END, "Me: " + user_input + "\n")
            self.conversation.see(tk.END)
            self.conversation['state'] = 'disabled'
            #self.conversation.after(5000, self.get_response(user_input))
            self.get_response(user_input)

    def get_response(self, user_input):
        """
        Get a response from the chatbot and display it if the user typed something.
        """
        self.conversation['state'] = 'normal'
        response = self.chatbot.get_response(user_input)

        self.conversation.insert(tk.END, "Rob: " + str(response.text) + "\n")
        self.conversation.see(tk.END)
        self.conversation['state'] = 'disabled'
        time.sleep(0.5)


gui_example = TkinterGUIExample()
gui_example.mainloop()
