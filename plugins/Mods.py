import pyrogram
import os
from pyrogram import Client, filters, enums
from pyrogram.types import Message, User

bughunter0 = Client(
    "botname",
    bot_token=os.environ["BOT_TOKEN"],
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
)


@Client.on_message(filters.command(["start"]))
async def start(bot, update):
    await update.reply_text("Start Message Here")



@Client.on_message(filters.forwarded and filters.channel)
async def channeltag(bot, message):
   try:
       forward_msg = await message.copy(message.chat.id)
       await message.delete()
   except:
       await message.reply_text("Oops , Recheck My Admin Permissions & Try Again")

@Client.on_message(filters.regex("http") | filters.regex("www") | filters.regex("t.me"))
async def nolink(bot,message):
	try:
		await message.delete()
	except:
		return
