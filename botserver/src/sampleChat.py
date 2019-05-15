import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from src.train import trainSet1, trainSet2, trainSet3
from chatterbot.comparisons import JaccardSimilarity
import time


class SampleChatbot():

    def __init__(self, *args, **kwargs):
        """
        Create & set window variables.
        """

        self.chatbot = ChatBot(
            "Rob.ai",
            storage_adapter="chatterbot.storage.SQLStorageAdapter",
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'default_response': 'I am sorry, but I do not understand.',
                    'maximum_similarity_threshold': 0.90
                },
                {
                    "import_path": "chatterbot.logic.BestMatch",
                    "statement_comparison_function": JaccardSimilarity
                }
            ],
            database_uri="sqlite:///database.db"
        )

        # train
        trainSet1(self.chatbot) #chatterbot greetings
        trainSet2(self.chatbot) #Nijjan HR questions
        trainSet3(self.chatbot) #MSC Software questions

    def get_response(self,user_input):
        """
        Get a response from the chatbot and display it if the user typed something.
        """

        response = self.chatbot.get_response(user_input)

        time.sleep(0.5)

        return response
    
    def train(self, input):
        self.chatbot.train(input)