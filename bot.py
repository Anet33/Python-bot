from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = '6450152847:AAGdfi55urxGS7OnAGSsOvxXR0Pm9MTtteQ'
BOT_USERNAME: Final = '@new_your_small_diary_bot'


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('~Hello~ /n Have you ever forgotten something to do? Forget about someone’s birthday, important meeting, classes or just want to make your life a little bit easier? Than this bot is for you 😊 I am like small diary in phone. You can find out about your schedule, write about your emotions, shoplist and other /n ~Wish all the best~')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('If you need to know the shedule, just write the weekday. PS: please write without any other symbols. /n For example: I want to know shedule for Friday, so I just need to write Friday. /n To know your shoplist, you just need to write word "shoplist" /n Same for birthaday. Write name and you will get date /n To write about your emotions, firstly, you need to write in general "good, awesome, bad" and only than describe why you have this emotion')

def handle_response(text: str) -> str:
    processed = text.lower()

    shedule = {
        'monday': 'Ukrainian language /n Ukrainian literature /n Physics /n Geometry /n Biology /n Physics /n ------- /n Gym',
        'tuesday': 'Maths /n Biology /n Geometry /n Geometry /n Music /n English',
        'wednesday': 'English /n History /n Literature /n History /n PE /n Drama /n Physics /n ------- /n English',
        'thursday': 'Ukrainian language /n PE /n Maths /n Maths /n IT /n Ukrainian literature /n English /n ------- /n Gym',
        'friday': 'Geography /n Drama /n IT /n History /n Maths /n Maths /n PE /n ------- /n English',
        'saturday': 'Chemistry /n Chemistry /n IT /n IT /n IT',
        'sunday': 'Homework /n Meet friends in the cafe /n Read book /n Watch movie /n Homework',
    }

    shoplist = {
        'shoplist': 'Milk /n Bread /n Sweets /n Tea /n Water ',
    }

    birthday = {
        'maria': '27.03',
        'carlos': '01.09',
        'emma': '01.07',
        'ivan': '24.01',
        'anastasia': '28.01',
    }

    emotions = {
        'bad': 'So sorry to hear that. Hope tomorrow will be better',
        'good': "Happy to hear that",
        'awesome': 'YAY',
        }

    if processed in shoplist:
        return shoplist[processed]

    if processed in shedule:
        return shedule[processed]
        
    if processed in  emotions:
        return  emotions[processed]

    if processed in birthday:
        return birthday[processed]


    return "I am so sorry, but I do not have an answer to your request yet :("

    
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text

    print(f'User({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group' and BOT_USERNAME in text:
        new_text = text.replace(BOT_USERNAME, '').strip()
        response = handle_response(new_text)
    else:
        response = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if name == 'main':
    print('Starting bot...')

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))


    app.add_handler(MessageHandler(filters.TEXT, handle_message))


    app.add_error_handler(error)


    print('Loading...')
    app.run_polling(poll_interval = 2 )