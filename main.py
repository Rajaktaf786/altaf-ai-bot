import telebot
import google.generativeai as genai
import os

BOT_TOKEN = os.environ['BOT_TOKEN']
GEMINI_KEY = os.environ['GEMINI_KEY']

bot = telebot.TeleBot(BOT_TOKEN)
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot chalu hai bhai ✅")

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    try:
        bot.send_chat_action(message.chat.id, 'typing')
        response = model.generate_content(f"Hindi me short jawab de: {message.text}")
        bot.reply_to(message, response.text)
    except:
        bot.reply_to(message, "Error aa gaya")

print("Bot started...")
bot.infinity_polling()
