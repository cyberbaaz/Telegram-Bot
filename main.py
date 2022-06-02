import os,time
import telebot
import sitescrap
API_Key=os.getenv('API_KEY')
bot=telebot.TeleBot(API_Key)
print(API_Key)
try:


    for _ in range(100):
        def get_roll(msg):
            for text in msg:
                if '@' in text:
                    return text


        @bot.message_handler(commands=['Greet'])


        def greet(message):
            bot.reply_to(message,"Hello noob")

        @bot.message_handler(commands=['Do'])
        def demand(message):
            bot.send_message(message.chat.id,"What should i do?")

        @bot.message_handler(commands=['Result'])
        def result_msg(message):
            bot.send_message(message.chat.id,"@ Roll_no Sem as told")

        @bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
        def semresult(message):
            params = message.text.split()
            if len(params)>2:
                sitescrap.send_data(params[1:])
                photo = open("img/{}.png".format(params[1]), 'rb')
                bot.send_message(message.chat.id, ' '.join(params[1:]))
                bot.send_photo(message.chat.id, photo)
                photo.close()
                os.remove("img/{}.png".format(str(params[1])))
            else:
                bot.send_message(message.chat.id, "Please Type as stated")





except:
    print("error " + str(IOError))
    pass

bot.polling()