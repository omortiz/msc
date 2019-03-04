'''
Created on Mar 4, 2019

@author: Isaac Li
'''

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

def trainChatbotSample():

    chatbot = ChatBot("Rob")

    trainer = ListTrainer(chatbot)

    trainer.train("chatterbot.corpus.english")
    
    return(chatbot)

if __name__=="__main__":
    #chatbot = trainChatbotSample()
    chatbot = ChatBot("Rob")

    trainer = ListTrainer(chatbot)

    trainer.train("chatterbot.corpus.english")
    
    print("Please type your question or 'quit'\n")
    inp = input("Me: \n")
    
    while (inp != 'quit'):
        
        response = chatbot.get_response(inp)
        print('Rob:')
        print(response)
        print(" ")
        inp = input("Me: \n")
    
    