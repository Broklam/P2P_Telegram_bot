import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from tracksys import get_prices

token = "5393889257:AAH1H4uxjgh2eVq2RH7sOgXnGtH-q8yFTpU"

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher


def prices(update, context):
    chat_id = update.effective_chat.id
    message = ""
    crypto_data = get_prices()
    for i in crypto_data:
        coin = crypto_data[i]["coin"]
        price = crypto_data[i]["price"]
        change_day = crypto_data[i]["change_day"]
        change_hour = crypto_data[i]["change_hour"]
        message += f"Coin: {coin}\nPrice: ${price:,.2f}\nHour Change: {change_hour:.3f}%\nDay Change: {change_day:.3f}%\n\n"
    context.bot.send_message(chat_id=chat_id, text=message)


dispatcher.add_handler(CommandHandler("GetPrices", prices))
updater.start_polling()
###Add Buttons + Personalization in choosing coins + agenda + alerts