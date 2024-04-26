from telebot import TeleBot
from keyboard import generate_main_menu, laptop_manu, buy_laptop
from malumot import rows

token = "6590114334:AAGuzj_tnxcW1FxHKQBEjb0UqE8TkVNe_L4"
bot = TeleBot(token)

@bot.message_handler(["start"])
def first(messege):
    chat_id = messege.chat.id
    send_id = messege.from_user.id
    send_name = messege.from_user.first_name
    send_last_name = messege.from_user.last_name
    final = f"Siz {send_id}\n {send_name} va {send_last_name} ingizni kirgizdingiz"
    contact = bot.send_message(final, reply_markup=generate_main_menu())
    bot.register_next_step_handler(contact, second_word)

def second_word(messege):
    chat_id = messege.chat.id
    phone_number = messege.contact.phone_number
    bot.send_message(f"Siz {chat_id} va {phone_number} orqali to'liq registratasiya o'tdingiz", reply_markup=laptop_manu())
    bot.register_next_step_handler(messege, tovar)


def tovar(messege):
    chat_id = messege.chat.id
    if messege.text == 'tovar':
        product_name = rows[0]
        product_image = rows[1]
        product_price = rows[2]
        credit_price = rows[3]
        laptop_data = f"Noutbok nomi: {product_name}\n\nNoutbok narxi: {product_price}\n\nMudatli to'lov: {credit_price}"
        bot.send_photo(chat_id, product_image, caption=laptop_data, reply_markup=buy_laptop())


while True:
    try:
        print("Bot run!")
        bot.polling()

    except:
        print("error")
        bot.stop_polling()