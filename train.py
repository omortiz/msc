from Rob import bot
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(bot)

trainer.train([
    "Hi there!",
    "Hello",
])

trainer.train([
    "Greetings!",
    "Hello",
])

trainer.train([
    "Are you a human?",
    "I'm a digital assistant.",
])

trainer.train([
    "What are you",
    "I'm a digital assistant.",
])

trainer.train([
    'How can I help you?',
    'I want to create a chat bot',
    'Have you read the documentation?',
    'No, I have not',
    'This should help get you started: http://chatterbot.rtfd.org/en/latest/quickstart.html'
])
