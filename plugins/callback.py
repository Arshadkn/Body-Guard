from pyrogram import Client
from utils import is_subscribed
from info import AUTH_CHANNEL
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaPhoto



@Client.on_callback_query()
async def cb_handler(client, query):

    if query.data == "grp_checksub":
        if AUTH_CHANNEL and not await is_subscribed(client, query):
            await query.answer(f"Hello {query.from_user.first_name},\nPlease join my updates channel and request again.", show_alert=True)
            return
        await query.answer(f"Hello {query.from_user.first_name},\nGood, Can You Request Now!", show_alert=True)
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
        return

    elif query.data.startswith("close_data"):
        userid = query.message.reply_to_message.from_user.id                        
        await query.message.delete()
        await query.message.reply_to_message.delete()
