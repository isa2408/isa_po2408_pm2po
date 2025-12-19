import telebot
import database
TOKEN = "8549479870:AAGa7lkFhGhteXXQJlSHXcySb_ucyvYw20w"

bot = telebot.TeleBot(TOKEN)
database.start_db()
from telebot.types import ReplyKeyboardMarkup
def gender_keyboard():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("👔 Мужское", "👗 Женское")
    kb.add("👕 Unisex")
    return kb

user_cart = {}
@bot.message_handler(commands=['add'])
def add_to_cart(message):
    args = message.text.split(maxsplit=1)

    if len(args) < 2:
        bot.send_message(message.chat.id, "Используй: /add Название")
        return

    item_name = args[1]

    if message.chat.id not in user_cart:
        user_cart[message.chat.id] = []

    user_cart[message.chat.id].append(item_name)
    bot.send_message(message.chat.id, f"🛒 {item_name} добавлен в корзину")

@bot.message_handler(commands=['cart'])
def show_cart(message):
    cart = user_cart.get(message.chat.id, [])

    if not cart:
        bot.send_message(message.chat.id, "🛒 Корзина пуста")
        return

    text = "🛒 Ваша корзина:\n"
    for item in cart:
        text += f"• {item}\n"

    bot.send_message(message.chat.id, text)

# Команда /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "чо хотел?"
    )


catalog = database.select_catalog()
# Команда /catalog
@bot.message_handler(commands=['catalog'])
def choose_gender(message):
    bot.send_message(
        message.chat.id,
        "Выберите категорию:",
        reply_markup=gender_keyboard()
    )

@bot.message_handler(func=lambda m: m.text in ["👔 Мужское", "👗 Женское", "👕 Unisex"])
def show_gender_catalog(message):

    mapping = {
        "👔 Мужское": "Men",
        "👗 Женское": "Women",
        "👕 Unisex": "Unisex"
    }

    items = database.select_catalog_by_gender(mapping[message.text])

    if not items:
        bot.send_message(message.chat.id, "Нет товаров")
        return

    text = "🛍 Товары:\n\n"
    for name, price, gender, style, image in items:
        medias = [telebot.types.InputMediaPhoto(image)]
        text += (
            f"👕 {name}\n"
            f"💰 {price}\n"
            f"🎨 {style}\n"
            f" {gender}\n"
            f"{image}\n"
            "────────────\n"
        )
        # bot.send_media_group(message.chat.id, medias)
    bot.send_message(message.chat.id, text)
    

@bot.message_handler(commands=['style'])
def style_search(message):
    args = message.text.split(maxsplit=1)

    if len(args) < 2:
        bot.send_message(message.chat.id, "Пример: /style Casual")
        return

    items = database.select_by_style(args[1])

    if not items:
        bot.send_message(message.chat.id, "Ничего не найдено")
        return

    text = "🎨 Найдено:\n"
    for name, price in items:
        text += f"{name} — {price}\n"

    bot.send_message(message.chat.id, text)
 

# Ответ на любые сообщения
@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(
        message.chat.id,
        f"Ты написал: {message.text}"
    )
# Запуск бота
bot.polling(none_stop=True)
