import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from src.train import trainSet1, trainSet2, trainSet3


class SampleChatbot():

    def __init__(self, *args, **kwargs):

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

        # Greeting Questions
        trainSet1(self.chatbot)
        
        # HR Questions from Niijan
        trainSet2(self.chatbot)
        
        # HR Questions 3
        trainSet3(self.chatbot)


    def get_response(self, quest):
        """
        Get a response from the chatbot and display it.
        """

        response = self.chatbot.get_response(quest)

        return response

    def train(self, input):
        """
        Train the chatbot with certain input
        """
        self.chatbot.train(input)

