import telebot
import time

TOKEN = '607394999:AAGQK2jQhiuQghtnBXx8qs8z6rtpFS9TKes'
bot = telebot.TeleBot(TOKEN)
import gspread
from oauth2client.service_account import ServiceAccountCredentials
# import pprint
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
# pp = pprint.PrettyPrinter()
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Hello '+f'{message.chat.first_name}!')
    bot.reply_to(message, 'Here you can type pick up number!')
@bot.message_handler(content_types=['text'])
def reply(message):
    sheet = client.open('TONU').sheet1
    #INHERING DATA TO VARIABLES
    #data = sheet.get_all_records()
    pick_up_numbers = sheet.col_values(1)
    status = sheet.col_values(2)
    num_to_check = message.text
    for i in range(0, len(pick_up_numbers)):
        if num_to_check == pick_up_numbers[i]:
            result = status[i]
            result1 = f"ID: {num_to_check} \nSTATUS: {result}"
            break
        else:
            result1 = "Sorry, you have entered INVALID ID," \
                      "please make sure that you type ID correctly (Note that capital LETTERS are allowed)."
    bot.reply_to(message, result1)

# pp.pprint(data)
while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
