import pyrogram
import os
from pyrogram import Client, filters, enums
from pyrogram.types import Message, User
from datetime import datetime, timedelta
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, User, Message, ChatPermissions, CallbackQuery


import asyncio
import os
import shlex
from datetime import datetime
from os.path import basename

import requests
import tracemoepy
from bs4 import BeautifulSoup
from pyrogram import filters
from typing import Tuple, Optional





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
screen_shot = "nana/downloads/"


@Client.on_message(filters.command(["reverse"]))
async def google_rs(client, message):
    start = datetime.now()
    dis_loc = ''
    base_url = "http://www.google.com"
    out_str = "`Reply to an image`"
    if message.reply_to_message:
        message_ = message.reply_to_message
        if message_.sticker and message_.sticker.file_name.endswith('.tgs'):
            await message.delete()
            return
        if message_.photo or message_.animation or message_.sticker:
            dis = await client.download_media(
                message=message_,
                file_name=screen_shot
            )
            dis_loc = os.path.join(screen_shot, os.path.basename(dis))
        if message_.animation or message_.video:
            await message.edit("`Converting this Gif`")
            img_file = os.path.join(screen_shot, "grs.jpg")
            await take_screen_shot(dis_loc, 0, img_file)
            if not os.path.lexists(img_file):
                await message.edit("`Something went wrong in Conversion`")
                await asyncio.sleep(5)
                await message.delete()
                return
            dis_loc = img_file
        if dis_loc:
            search_url = "{}/searchbyimage/upload".format(base_url)
            multipart = {
                "encoded_image": (dis_loc, open(dis_loc, "rb")),
                "image_content": ""
            }
            google_rs_response = requests.post(search_url, files=multipart, allow_redirects=False)
            the_location = google_rs_response.headers.get("Location")
            os.remove(dis_loc)
        else:
            await message.delete()
            return
        await message.edit("`Found Google Result.`")
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0"
        }
        response = requests.get(the_location, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        prs_div = soup.find_all("div", {"class": "r5a77d"})[0]
        prs_anchor_element = prs_div.find("a")
        prs_url = base_url + prs_anchor_element.get("href")
        prs_text = prs_anchor_element.text
        end = datetime.now()
        ms = (end - start).seconds
        out_str = f"""<b>Time Taken</b>: {ms} seconds
<b>Possible Related Search</b>: <a href="{prs_url}">{prs_text}</a>
<b>More Info</b>: Open this <a href="{the_location}">Link</a>
"""
    await message.edit(out_str, parse_mode=enums.ParseMode.HTML, disable_web_page_preview=True)

async def take_screen_shot(video_file: str, duration: int, path: str = '') -> Optional[str]:
    """take a screenshot"""
    ttl = duration // 2
    thumb_image_path = path or os.path.join(screen_shot, f"{basename(video_file)}.jpg")
    command = f"ffmpeg -ss {ttl} -i '{video_file}' -vframes 1 '{thumb_image_path}'"
    err = (await run_cmd(command))[1]
    if err:
        _LOG.error(err)
    return thumb_image_path if os.path.exists(thumb_image_path) else None


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
