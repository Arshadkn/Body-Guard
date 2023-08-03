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

    elif query.data == "close_data":
        await query.message.delete()
        if AUTH_CHANNEL and not await is_subscribed(client, query):
            await query.answer(f"Hello {query.from_user.first_name},\nPlease join my updates channel and request again.", show_alert=True)
            return
        else:
                    await query.answer(f"Hᴇʏ {query.from_user.first_name}, Tʜɪs Is Nᴏᴛ Yᴏᴜʀ Mᴏᴠɪᴇ Rᴇǫᴜᴇsᴛ. Rᴇǫᴜᴇsᴛ Yᴏᴜʀ's !", show_alert=True)
                await query.answer('Cʜᴇᴄᴋ PM, I ʜᴀᴠᴇ sᴇɴᴛ ғɪʟᴇs ɪɴ PM', show_alert=True)
        except UserIsBlocked:
            await query.answer('Uɴʙʟᴏᴄᴋ ᴛʜᴇ ʙᴏᴛ ᴍᴀʜɴ !', show_alert=True)
        except PeerIdInvalid:
            await query.answer(url=f"https://telegram.me/{temp.U_NAME}")
        except Exception as e:
            await query.answer(url=f"https://telegram.me/{temp.U_NAME}")
            await query.message.delete()
           
