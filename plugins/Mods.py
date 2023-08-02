import pyrogram
import os
from pyrogram import Client, filters, enums
from pyrogram.types import Message, User
from datetime import datetime, timedelta
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, User, Message, ChatPermissions, CallbackQuery






bughunter0 = Client(
    "botname",
    bot_token=os.environ["BOT_TOKEN"],
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
)

START ="""
Hey {} 
All Things are Simple To do. Follow The writings given Below. 

⚙️™️ SETTING UP OF BOT ON GROUP.

™️• Add Bot To Group. 
™️• Promote The Bot as Admin on group with (Change group info and, delete messages) permission. 
™️• If you Trust Us You can Gib The bot Full permissions on group. We would Not do any illegal and Unwanted Things via bot on group. 

⚙️™️ FEATURES THAT I HAVE. 

™️• Remove Service Message (Join and Leave) on Group. 
™️• Remove Regex links of Websites and Telegram Group link invitation. 
™️• Remove Forwarded Messages on Group. 
™️• Remove Using Unwanted Commands From Group.

 NB :- BOT WOULD NOT DELETE ADMIN MESSEGES.
"""


@Client.on_message(filters.command(["start"]))
async def start(bot, message):
    
    await message.reply_text(START.format(message.from_user.mention))



@Client.on_message(filters.forwarded and filters.channel)
async def channeltag(bot, message):
   try:
       forward_msg = await message.copy(message.chat.id)
       await message.delete()
   except:
       await message.reply_text("Oops , Recheck My Admin Permissions & Try Again")

# @Client.on_message(filters.regex("http") | filters.regex("www") | filters.regex("t.me"))
# async def nolink(bot,message):
# 	try:
# 		await message.delete()
# 	except:
# 		return


@Client.on_message(filters.regex("http") | filters.regex("www") | filters.regex("t.me"))
async def nolink(bot,message):
    try:
        await message.delete()
    except:
	return





@Client.on_message(filters.forwarded)
async def forward(bot, message):
	await message.delete()

# show alert

# @Client.on_message(filters.edited)
# async def edited(bot,message):
# 	chatid= message.chat.id	
#	await bot.send_message(text=f"{message.from_user.mention} Edited This [Message]({message.link})",chat_id=chatid)


@Client.on_message(filters.via_bot & filters.group)
async def inline(bot,message):
     await message.delete()


@Client.on_message(filters.group & filters.regex("/" ) | filters.service)
async def delete(bot,message):
 await message.delete()



@Client.on_message(filters.new_chat_members)
async def welcome(bot, message):
	await message.delete()	
	
@Client.on_message(filters.left_chat_member)
async def goodbye(bot, message):
	await message.delete()	
