from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from XDB.data import MASTERS, WISH, FLIRT, SRAID, LOVERAID
from config import OWNER_ID
from config import CMD_HANDLER as cmd
from .help import *
import asyncio

@Client.on_message(filters.command("sraid", cmd) & filters.me)
async def sraid(xspam: Client, e: Message):
    kex = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)

    if len(kex) == 2:
        ok = await xspam.get_users(kex[1])
        counts = int(kex[0])
        for _ in range(counts):
            reply = choice(SRAID)
            msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
            await xspam.send_message(e.chat.id, msg)
            await asyncio.sleep(0.1)

    elif e.reply_to_message:
        user_id = e.reply_to_message.from_user.id
        ok = await xspam.get_users(user_id)
        counts = int(kex[0])
        for _ in range(counts):
            reply = choice(SRAID)
            msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
            await xspam.send_message(e.chat.id, msg)
            await asyncio.sleep(0.1)

    else:
        await e.reply_text("!ꜱʀᴀɪᴅ 10 <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ>")

@Client.on_message(filters.command("pyaar", cmd) & filters.me)
async def pyaar(xspam: Client, e: Message):
    kex = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)

    if len(kex) == 2:
        ok = await xspam.get_users(kex[1])
        counts = int(kex[0])
        for _ in range(counts):
            reply = choice(LOVERAID)
            msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
            await xspam.send_message(e.chat.id, msg)
            await asyncio.sleep(0.1)

    elif e.reply_to_message:
        user_id = e.reply_to_message.from_user.id
        ok = await xspam.get_users(user_id)
        counts = int(kex[0])
        for _ in range(counts):
            reply = choice(LOVERAID)
            msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
            await xspam.send_message(e.chat.id, msg)
            await asyncio.sleep(0.1)

    else:
        await e.reply_text("!ʟᴏᴠᴇ 10 <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ>")

@Client.on_message(filters.command("flirt", cmd) & filters.me)
async def flirt(xspam: Client, e: Message):
    kex = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)

    if len(kex) == 2:
        ok = await xspam.get_users(kex[1])
        counts = int(kex[0])
        for _ in range(counts):
            reply = choice(FLIRT)
            msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
            await xspam.send_message(e.chat.id, msg)
            await asyncio.sleep(0.1)

    elif e.reply_to_message:
        user_id = e.reply_to_message.from_user.id
        ok = await xspam.get_users(user_id)
        counts = int(kex[0])
        for _ in range(counts):
            reply = choice(FLIRT)
            msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
            await xspam.send_message(e.chat.id, msg)
            await asyncio.sleep(0.1)

    else:
        await e.reply_text(".ꜰʟɪʀᴛ 10 <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ>")

@Client.on_message(filters.command("bday", cmd) & filters.me)
async def bday(xspam: Client, e: Message):
    kex = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)

    if len(kex) == 2:
        ok = await xspam.get_users(kex[1])
        counts = int(kex[0])
        for _ in range(counts):
            reply = choice(WISH)
            msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
            await xspam.send_message(e.chat.id, msg)
            await asyncio.sleep(0.1)

    elif e.reply_to_message:
        user_id = e.reply_to_message.from_user.id
        ok = await xspam.get_users(user_id)
        counts = int(kex[0])
        for _ in range(counts):
            reply = choice(WISH)
            msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
            await xspam.send_message(e.chat.id, msg)
            await asyncio.sleep(0.1)

    else:
        await e.reply_text("!ʙᴅᴀʏ 10 <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ>")

add_command_help(
    "💥 𝐒ᴀɪғ ",
    [
        ["sraid", "Shyari raid to user"],
        ["pyaar", " love raid to user"],
        ["flirt", "flirt a girl"],
        ["bday", " Wish happy birthday"],
    ],
  )
