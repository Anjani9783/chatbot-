pip install chatterbot
pip install chatterbot_corpus

from chatterbot import ChatBot

bot = ChatBot(
'anjani ',
storage_adapter='chatterbot.storage.SQLStorageAdapter',
database_uri='sqlite:///db.sqlite3'
)
from chatterbot.trainers import ListTrainer
trainer = ListTrainer(bot)
trainer.train([
'hii',
'hello'
'good morning',
'How are you?',
'I am good.',
'That is good to hear.',
'Thank you',
'You are welcome.',
])

# Get a response to the input text 'I would like to book a flight.'
response = chatbot.get_response(input())
print(response)
