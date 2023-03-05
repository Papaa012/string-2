import asyncio

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    text1 = await bot.send_message(msg.chat.id, f"ʜᴇʏ🥀 `{msg.from_user.mention}`, ʜᴏᴡ ᴀʀᴇ ʏᴏᴜ!!")
    await asyncio.sleep(1.5)
    text2 = await text1.edit(f"ᴡᴀɪᴛ ʙᴀʙʏ✨❣️! ʟᴇᴛ ᴍᴇ ɢᴇᴛ ꜱᴛᴀʀᴛᴇᴅ \nꜱᴏ ᴛʜᴀᴛ ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴍʏ ᴘᴏᴡᴇʀ✨❣️🥀")
    await asyncio.sleep(1.5)
    await text2.delete()
    stck = await bot.send_sticker(msg.chat.id, "CAACAgUAAxkBAAIPlmQDr4j4Ayqm57slsq-l53KmEHJ9AAI9CQACFm7gVI4RHTP_GrcvLgQ")
    await asyncio.sleep(1.5)
    await stck.delete()
    alt = await bot.get_me()
    me2 = alt.mention
    await bot.send_photo(
        chat_id=msg.chat.id,
         photo="https://telegra.ph/file/102e741cfaa429587f807.jpg",
         caption=f"""Hᴇʏ🥀 {msg.from_user.mention},
         
ɪ'ᴍ {me2} ,

ᴀ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ ꜱᴛʀɪɴɢ
ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @iro_bot_support ✨❣️🥀""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="✨ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ🍁", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("✨ᴜᴘᴅᴀᴛᴇꜱ✨", url="https://t.me/iro_bot_support"),
                    InlineKeyboardButton(" 🥀ᴅᴇᴠᴇʟᴏᴩᴇʀ🥀 ", user_id=OWNER_ID)
                ]
            ]
        ),
    )
