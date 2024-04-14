from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from XDB.data import MASTERS, ABUSE
from config import OWNER_ID
from config import CMD_HANDLER as cmd
from .help import *
import asyncio

@Client.on_message(filters.command("gali", cmd) & filters.me)
async def abuse(x: Client, e: Message):
    NOBI = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)

    if len(NOBI) == 2:
        ok = await x.get_users(NOBI[1])
        counts = int(NOBI[0])
        for _ in range(counts):
            reply = choice(ABUSE)
            msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
            await x.send_message(e.chat.id, msg)
            await asyncio.sleep(0.1)

    elif e.reply_to_message:
        user_id = e.reply_to_message.from_user.id
        ok = await x.get_users(user_id)
        counts = int(NOBI[0])
        for _ in range(counts):
            reply = choice(ABUSE)
            msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
            await x.send_message(e.chat.id, msg)
            await asyncio.sleep(0.1)

    else:
        await e.reply_text(".𝐠𝐚𝐥𝐢 𝟏𝟎 <𝐫𝐞𝐩𝐥𝐲 𝐭𝐨 𝐮ꜱ𝐞𝐫 𝐨𝐫 𝐮ꜱ𝐞𝐫𝐧𝐚𝐦𝐞>")


add_command_help(
    "➥ 𝐆ᴀʟɪ",
    [
        ["gali", "Tᴏ abuse someone."],
    ],
  )
