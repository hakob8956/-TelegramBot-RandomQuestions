#!/usr/bin/env python
import random
import pickle
import questions
import telebot
from telebot import types
from telebot.types import Message
from enums.category import Category
from session import Session


TOKEN = 'Paste Your token here'

bot = telebot.TeleBot(TOKEN)
USERS = set()


def generateText(userId,category):
    try:
        print(userId,Category(category).name)
        session =  Session(userId,category)
        id = session.getQuestionId()
        print(id)
        return questions.getRandomQuestionWithId(id,category)
    except Exception as e:
        print(e)



@bot.message_handler(categories=['start', 'help'])
def command_handler(message: Message):
    bot.reply_to(message, """just use inline command '@randquestdiscussbot'""")


@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def echo_digits(message: Message):
    print(message.from_user.id)
    if 'get' == message.text.strip().lower():
        bot.reply_to(message, generateText(message.from_user.id,Category.Discuss.value))
        return
    else:
        bot.reply_to(message, "you can use inline-command '@randquestdiscussbot'  or type 'get'")
        return

@bot.inline_handler(func=lambda query: True)
def query_text(query):
    try:
        print(query)
        if query.query.strip() == 'g':
            category = Category.Girl.value
        else:
            category = Category.Discuss.value
        text = generateText(query.from_user.id, category)
        r_answer =  types.InlineQueryResultArticle(
                id='1',
                title="Click",
                input_message_content=types.InputTextMessageContent(message_text=text)                
        )
        bot.answer_inline_query(query.id, [r_answer], cache_time=1)
    except Exception as e:
        print(e)

bot.polling(timeout=60)
