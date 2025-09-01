import telebot
import openai
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = telebot.TeleBot(BOT_TOKEN)
openai.api_key = OPENAI_API_KEY

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Men AI botman. Menga savol bering.")

@bot.message_handler(func=lambda message: True)
def ai_answer(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": message.text}]
        )
        bot.reply_to(message, response.choices[0].message["content"])
    except Exception as e:
        bot.reply_to(message, f"Xatolik: {e}")

bot.polling()
