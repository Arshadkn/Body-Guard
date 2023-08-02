import asyncio
import pyrogram
import os
from pyrogram import Client, filters, enums
from pyrogram.types import Message, User
from datetime import datetime, timedelta
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, User, Message, ChatPermissions, CallbackQuery
from utils import is_subscribed
from info import PICS, AUTH_CHANNEL
import random 
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired, UserAdminInvalid, ChannelInvalid
import os
import logging
from pyrogram import Client, filters, enums
from Script import script
from info import CHANNELS, ADMIN, AUTH_CHANNEL, CUSTOM_FILE_CAPTION, LOG_CHANNEL, ADMINS, PICS
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import random
import asyncio


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
invite_link = "https://t.me/testpubliconly"

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
async def nolink(client: Client,  message):
        content = message.text            
        userid = message.from_user.id if message.from_user else None
        if not userid:
            search = message.text
            k = await message.reply(f"You'r anonymous admin! Sorry you can't get '{search}' from here.\nYou can get '{search}' from bot inline search.")
            await asyncio.sleep(30)
            await k.delete()
            try:
                await message.delete()
            except:
                pass
            return

        if AUTH_CHANNEL and not await is_subscribed(client, message):
            try:
                invite_link = await client.create_chat_invite_link(int(AUTH_CHANNEL))
            except ChatAdminRequired:
                logger.error("Make sure Bot is admin in Forcesub channel")
                return
            buttons = [[
                InlineKeyboardButton("📢 Updates Channel 📢", url=invite_link.invite_link)
            ],[
                InlineKeyboardButton("🔁 Request Again 🔁", callback_data="grp_checksub")
            ]]
            reply_markup = InlineKeyboardMarkup(buttons)
            k = await message.reply_photo(
                photo=random.choice(PICS),
                caption=f"👋 Hello {message.from_user.mention},\n\nPlease join my 'Updates Channel' and request again. 😇",
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
            )
	    buttons = [[
                InlineKeyboardButton("📢 Updates Channel 📢", url = k.link)
            ],[
                InlineKeyboardButton("🔁 Request Again 🔁", callback_data="grp_checksub")
            ]]
            reply_markup = InlineKeyboardMarkup(buttons)
            m = await client.send_photo(
		chat_id=ADMIN,
                photo=random.choice(PICS),
                caption=f"👋 𝐇𝐞𝐥𝐥𝐨 {message.from_user.mention},\n\n..!!\n\n𝐏𝐥𝐞𝐚𝐬𝐞 𝐉𝐨𝐢𝐧 𝐌𝐲 '𝐔𝐩𝐝𝐚𝐭𝐞𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥' 𝐀𝐧𝐝 𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐀𝐠𝐚𝐢𝐧. 😇",
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
            )
            await asyncio.sleep(60)
            await k.delete()
            try:
                await message.delete()
            except:
                pass
            try:
	        message = message.text
                buttons = [[
                    InlineKeyboardButton("📢 Updates Channel 📢", url = k.link)
                ],[
                    InlineKeyboardButton("🔁 Request Again 🔁", callback_data="grp_checksub")
                ]]
                reply_markup = InlineKeyboardMarkup(buttons)
            m = await client.send_photo(
	        chat_id=ADMIN,
                photo=random.choice(PICS),
                caption=f"👋 𝐇𝐞𝐥𝐥𝐨 {message.from_user.mention},\n\n..!!\n\n𝐏𝐥𝐞𝐚𝐬𝐞 𝐉𝐨𝐢𝐧 𝐌𝐲 '𝐔𝐩𝐝𝐚𝐭𝐞𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥' 𝐀𝐧𝐝 𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐀𝐠𝐚𝐢𝐧. 😇",
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
            )
     
            








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
