import os
from dotenv import load_dotenv

import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    ContextTypes, ConversationHandler, MessageHandler, filters
)

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("Токен не найден! Убедитесь, что он указан в файле .env")

Q1A, Q1P, Q2A, Q2P, Q3A, Q3P, Q4A, Q4P, Q4S, Q5A, Q5P, Q6A = range(12) 

def get_start_key_board():
    keyboard = [
        [
            InlineKeyboardButton("Готов!", callback_data="ready"),
            InlineKeyboardButton("Я пупсик...", callback_data="not_ready"),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(photo=open("images/first", "rb"), caption="""Привет, Славик! Кукуруза на связи🤙🏻
Сегодня тебя ждет небольшое путешествие, в конце которого ты найдешь сокровище🤑🤑🤑
Готов?""", reply_markup=get_start_key_board())
    

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):    
    query = update.callback_query
    await query.answer()  # Подтверждаем нажатие (убирает "часики")

    if query.data == "not_ready":
        await query.edit_message_caption(caption="🎉Ну ты шутник)", reply_markup=get_start_key_board())

    elif query.data == "ready":
        await query.edit_message_caption(caption="Поехали! 🚀 \n Я дом для путешественников, уютен и светел,\n  В сердце города жду, когда ты ко мне приедешь.\n Что это за место, где отдых и тепло?")
        return Q1A

async def question1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q1 = update.message.text.strip().lower()
    if q1 == "гостиница калининград":
        await update.message.reply_text("Молодец! Пришли фотку, как доберешься до места🫵🏻")
        return Q1P
    else:
        await update.message.reply_text("Попробуй... еще... раз...")
        return Q1A

async def question1_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.photo:
        # Фото получено — переходим к следующему вопросу
        await update.message.reply_photo(photo=open("images/photo1", "rb"),
            caption="Фото получено! 👍\n Следующий вопрос: \n Кто критикует чистый разум?"
        )
        return Q2A
    else:
        # Если прислали не фото — просим повторить
        await update.message.reply_text("Пожалуйста, отправь фото. Не текст!")
        return Q1P  # Остаёмся в состоянии ожидания фото

async def question2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q2 = update.message.text.strip().lower()
    if q2 == "кант":
        await update.message.reply_text("Молодец! Фоточку памятника в чат)")
        return Q2P
    else:
        await update.message.reply_text("Мда... А казалось все так просто...")
        return Q2A

async def question2_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.photo:
        # Фото получено — переходим к следующему вопросу
        await update.message.reply_photo(photo=open("images/photo2", "rb"),
            caption="Фото получено! 👍\n Время мини викторины: \n Посмотри на памятник и составь новое слово..."
        )
        return Q3A
    else:
        # Если прислали не фото — просим повторить
        await update.message.reply_text("Пожалуйста, отправь фото. Не текст!")
        return Q2P  # Остаёмся в состоянии ожидания фото


    
async def question3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q2 = update.message.text.strip().lower()
    if q2 == "танк":
        await update.message.reply_text("Молодец! Как и раньше, нужна фотка, но теперь танка")
        return Q3P
    else:
        await update.message.reply_text("Я уже красный!")
        return Q3A
    

async def question3_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.photo:
        # Фото получено — переходим к следующему вопросу
        await update.message.reply_photo(photo=open("images/photo3", "rb"),
            caption="Фото получено! 👍\n На вниматочность: \n Посмотри на пятник и найти буквы: \n 1: 5 (x2) \n 3: 5, 7, 10 \n 4: 5 \n 6: 3 "
        )
        return Q4A
    else:
        # Если прислали не фото — просим повторить
        await update.message.reply_text("Пожалуйста, отправь фото. Не текст!")
        return Q3P  # Остаёмся в состоянии ожидания фото



async def question4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q2 = update.message.text.strip().lower()
    if q2 == "иимрнтс":
        await update.message.reply_text("Молодец! А теперь составь из этих букв слово")
        return Q4S
    else:
        await update.message.reply_text("Попробуй... еще... раз...")
        return Q4A

async def question4s(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q2 = update.message.text.strip().lower()
    if q2 == "министр":
        await update.message.reply_text("Молодец! Скинь фотку!!!!")
        return Q4P
    else:
        await update.message.reply_text("Попробуй... еще... раз...")
        return Q4S
    

async def question4_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.photo:
        # Фото получено — переходим к следующему вопросу
        await update.message.reply_photo(photo=open("images/photo4", "rb"),
            caption="Фото получено! 👍\n Следующий вопрос: \n Ее называют Старым Светом, \n Там Эйфелева башня, Колизей есть где-то.  \n Здесь много стран, но одно – общий дом, \n От Балтики до Средиземноморья, все в нём."
        )
        return Q5A
    else:
        # Если прислали не фото — просим повторить
        await update.message.reply_text("Пожалуйста, отправь фото. Не текст!")
        return Q4P  # Остаёмся в состоянии ожидания фото


async def question5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q2 = update.message.text.strip().lower()
    if q2 == "европа":
        await update.message.reply_text("Красавчик, путник!🔥 Следующее фото в студию. Осталось немного :3")
        return Q5P
    else:
        await update.message.reply_text("Ого")
        return Q5A
    

async def question5_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.photo:
        # Фото получено — переходим к следующему вопросу
        await update.message.reply_photo(photo=open("images/photo5", "rb"),
            caption="Фото получено! 👍\n Следующий вопрос: \n Я магазин большой, где техника живет, \n Задрот гулять внутри готов - днями напролет. \n Телевизоры, смартфоны — все, что любишь ты! \n Что ж за место это такое — для шопинга мечты?"
        )
        return Q6A
    else:
        # Если прислали не фото — просим повторить
        await update.message.reply_text("Пожалуйста, отправь фото. Не текст!")
        return Q5P  # Остаёмся в состоянии ожидания фото


async def question6(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q2 = update.message.text.strip().lower()
    if q2[1] == "-" or q2[1] == ".":
        q2 = q2[0] + q2[2:]
    if q2 == "мвидео":
        await update.message.reply_photo(photo=open("images/last", "rb"), caption="Ты проделал длинный путь, а в конце всегда положена награда🎁 \n Забери её: \n № 1 597 782 563")
        return ConversationHandler.END
    else:
        await update.message.reply_text("Попробуй... еще... раз...")
        return Q6A
    

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Квест прерван. Напиши /start, чтобы начать заново.")
    return ConversationHandler.END


async def photo_fallback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Пожалуйста, отправь фото. Не текст!")
    # Возвращаем текущее состояние (оно и так не меняется)
    # Но чтобы быть точным, можно определить по context, но проще — просто не менять состояние
    return None  # ConversationHandler остаётся в том же состоянии


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points = [
        CommandHandler("start", start),
        CallbackQueryHandler(button_handler, pattern="^(ready|not_ready)$")
        ],
        states = {
            Q1A: [MessageHandler(filters.TEXT & ~filters.COMMAND, question1)],
            Q1P: [MessageHandler(filters.PHOTO, question1_photo),
                  MessageHandler(filters.TEXT & ~filters.COMMAND, photo_fallback)],
            Q2A: [MessageHandler(filters.TEXT & ~filters.COMMAND, question2)],
            Q2P: [MessageHandler(filters.PHOTO, question2_photo),
                  MessageHandler(filters.TEXT & ~filters.COMMAND, photo_fallback)],
            Q3A: [MessageHandler(filters.TEXT & ~filters.COMMAND, question3)],
            Q3P: [MessageHandler(filters.PHOTO, question3_photo),
                  MessageHandler(filters.TEXT & ~filters.COMMAND, photo_fallback)],
            Q4A: [MessageHandler(filters.TEXT & ~filters.COMMAND, question4)],
            Q4S: [MessageHandler(filters.TEXT & ~filters.COMMAND, question4s)],
            Q4P: [MessageHandler(filters.PHOTO, question4_photo),
                  MessageHandler(filters.TEXT & ~filters.COMMAND, photo_fallback)],
            Q5A: [MessageHandler(filters.TEXT & ~filters.COMMAND, question5)],
            Q5P: [MessageHandler(filters.PHOTO, question5_photo),
                  MessageHandler(filters.TEXT & ~filters.COMMAND, photo_fallback)],
            Q6A: [MessageHandler(filters.TEXT & ~filters.COMMAND, question6)],
        },
        fallbacks = [CommandHandler("start", cancel)]      
    )

    app.add_handler(conv_handler)
    app.run_polling()


if __name__ == "__main__":
    main()