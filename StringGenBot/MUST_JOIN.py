from config import MUST_JOIN
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"ʏᴏᴜ ᴍᴜꜱᴛ ɴᴇᴇᴅ ᴛᴏ ᴊᴏɪɴ [𝙄𝙍𝙊]({link}) ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ \n\n ᴛʀʏ ᴀɢᴀɪɴ ᴀꜰᴛᴇʀ ᴊᴏɪɴɪɴɢ ᴄʜᴀɴɴᴇʟ",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("✨ ᴊᴏɪɴ ✨", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"ɪ'ᴍ ɴᴏᴛ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ ᴍᴜꜱᴛ_ᴊᴏɪɴ ᴄʜᴀᴛ : {MUST_JOIN} !")
