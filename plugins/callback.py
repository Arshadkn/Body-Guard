from pyrogram import Client
from utils import is_subscribed
from info import AUTH_CHANNEL
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaPhoto

import os
import requests
from dotenv import load_dotenv
from requests.utils import requote_uri
from pyrogram import Client, filters
from pyrogram.types import *


load_dotenv()
API = "https://apibu.herokuapp.com/api/y-images?query="

JOIN_BUTTON = [
    InlineKeyboardButton(
        text='⚙ Join Updates Channel ⚙',
        url='https://telegram.me/FayasNoushad'
    )
]

Bot = Client(
    "Google-Search-Bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)



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
#        userid = query.message.reply_to_message.from_user.id                        
        await query.message.delete()
        await query.message.reply_to_message.delete()





@Client.on_message(filters.private & filters.command(["img"]))
async def searchimage(bot, message):
    
    results = requests.get(
        API + requests.utils.requote_uri(update, message)
    ).json()["result"][:50]
    
    for result in results:
        
        title=update.query.capitalize(),
        description=result,
        caption="Made by @FayasNoushad",
        photo_url=result
            
        
    
    await message.reply_photo(photo_url=result)
