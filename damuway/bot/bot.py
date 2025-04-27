from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = "7048033462:AAH3LAQAp09knbFkP2PrvdmlLQvtTcu4WxE"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(
    KeyboardButton("👶 Питание"),
    KeyboardButton("😴 Сон"),
)
main_menu.add(
    KeyboardButton("🧸 Игрушки"),
    KeyboardButton("📚 Развитие"),
)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(
        "Привет! Я бот DamuWay 🤖\nВыбери категорию или задай свой вопрос.",
        reply_markup=main_menu
    )

@dp.message_handler()
async def handle_message(message: types.Message):
    text = message.text.lower()

    if "питание" in text:
        await message.reply("В 6 месяцев можно начинать прикорм: овощные пюре, безглютеновые каши.")
    elif "сон" in text:
        await message.reply("Ребёнку 1 года нужно 11–12 часов ночного сна и 1–2 дневных сна.")
    elif "игрушки" in text:
        await message.reply("В 3 месяца подойдут мягкие погремушки, коврики, мобили.")
    elif "развитие" in text:
        await message.reply("Занимайтесь лепкой, чтением, развивающими играми.")
    else:
        await message.reply("Пока не знаю, что ответить 😅 Попробуй выбрать категорию.")

async def on_startup(dp):
    await bot.delete_webhook(drop_pending_updates=True)
    print("Бот успешно запущен!")

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
