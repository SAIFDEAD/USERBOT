import os
import re

import aiofiles
from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from X.helpers.basic import edit_or_reply
from X.utils.pastebin import paste

from .help import *

pattern = re.compile(r"^text/|json$|yaml$|xml$|toml$|x-sh$|x-shellscript$")


@Client.on_message(filters.command("paste", cmd) & filters.me)
async def paste_func(client: Client, message: Message):
    if not message.reply_to_message:
        return await edit_or_reply(message, f"ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ {cmd}ᴘᴀsᴛᴇ")
    r = message.reply_to_message
    if not r.text and not r.document:
        return await edit_or_reply(message, "ᴏɴʟʏ ᴛᴇxᴛ ᴀɴᴅ ᴅᴏᴄᴜᴍᴇɴᴛs ᴀʀᴇ sᴜᴘᴘᴏʀᴛᴇᴅ.")
    m = await edit_or_reply(message, "`ᴘᴀsᴛɪɴɢ...`")
    if r.text:
        content = str(r.text)
    elif r.document:
        if r.document.file_size > 40000:
            return await m.edit("ʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ᴘᴀsᴛᴇ ғɪʟᴇs sᴍᴀʟʟᴇʀ ᴛʜᴀɴ 40ᴋʙ.")
        if not pattern.search(r.document.mime_type):
            return await m.edit("ᴏɴʟʏ ᴛᴇxᴛ ғɪʟᴇs ᴄᴀɴ ʙᴇ ᴘᴀsᴛᴇᴅ.")
        doc = await message.reply_to_message.download()
        async with aiofiles.open(doc, mode="r") as f:
            content = await f.read()
        os.remove(doc)
    link = await paste(content)
    try:
        if m.from_user.is_bot:
            await message.reply_photo(
                photo=link,
                quote=False,
                reply_markup=kb,
            )
        else:
            await message.reply_photo(
                photo=link,
                quote=False,
                caption=f"**ᴘᴀsᴛᴇ ʟɪɴᴋ:** [ʜᴇʀᴇ]({link})",
            )
        await m.delete()
    except Exception:
        await m.edit(f"[ʜᴇʀᴇ]({link}) your paste")


add_command_help(
    "➥ 𝐏ᴀꜱᴛᴇ",
    [
        ["paste <ʀᴇᴘʟʏ>", "Tᴏ ꜱᴀᴠᴇ ᴛᴇxᴛ ᴛᴏ ᴛʜᴇ ꜱᴇʀᴠɪᴄᴇ ᴘᴀꜱᴛᴇʙɪɴ"],
    ],
      ) 
