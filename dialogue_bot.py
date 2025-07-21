import telebot as t
import os
from mistralai import Mistral

key = "axH9Wi5GKJa5LEQktOVYITTXJBd4XvSi"
TOKEN = "7838573587:AAGKAYiy3IYyecRRuBiPwJI7-8Uqenu2NP4"
api_key = "axH9Wi5GKJa5LEQktOVYITTXJBd4XvSi"
model = "magistral-small-2506"

client = Mistral(api_key=api_key)
bot = t.TeleBot(TOKEN)

a = ""
b = ""
n = 1

@bot.message_handler(commands=["start"])
def hello(message):
    bot.send_message(message.chat.id, "Привет, я бот для помощи школьникам в социализации!\n"
                                      "Насколько социализированным ты себя чувствуешь?")


@bot.message_handler(content_types = ['text'])
def chating(message):
    global a
    global b
    global n
    chat_history_user = a
    chat_history_bot = b
    chat_response = client.chat.complete(
        model=model,
        messages=[
            {
                "role": "system",
            "content": "Тебя зовут СоциоБот, но можно называть БаблГамБот"
                       "Ты — бот для помощи школьникам в социализации и борьбе с социофобией.\n"
                       "Сначала спроси школьника как ему удобнов формате диалога или полный маршрут действий\n"
                       "Если формат диалога твоя задача — создавать постепенно усложняющиеся задания, помогая интегрироваться школьнику в общество\n"
                       "Если маршрут то создай ему конкретный полный план действий как ему постепенно интегрироваться в общество\n"
                       "Говори ему что хоть это может быть и сложно, но ему понравится как только у него всё получиться\n" 
                       "Всегда поддерживай школьника, напоминая, что не все контакты будут успешными, но найти друзей реально.\n"},
        {
            "role": "system",
            "content": f"Сообщения написанные  ранее, если тебя спросят ты можешь брать их отсюда они пронумерованы и занесены в скобочки:{chat_history_user}"},
        {
            "role": "system",
            "content": f"Сообщения написанные тобой ранее, помни нельзя задавать вопросы которые спрашивают одно и тоже, никогда не пиши скобочки и цифры в одном сообщении:{chat_history_bot}"},
        {
            "role": "user",
            "content": f"{message.text}",}
                  ]
                                         )
    a = a +str(n)+"("+ message.text+")"
    b = b +str(n)+"("+ chat_response.choices[0].message.content+")"
    n += 1
    bot.send_message(message.chat.id, f"{chat_response.choices[0].message.content}")
bot.polling(none_stop = True )