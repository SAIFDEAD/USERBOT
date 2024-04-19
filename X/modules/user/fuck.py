from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from XDB.data import MASTERS, RAID, SDICTATOR, HRAID
from config import OWNER_ID
from config import CMD_HANDLER as cmd
from .help import *
import asyncio

@Client.on_message(filters.command("raid", cmd) & filters.me)
async def raid(xspam: Client, message: Message):  
    kex = message.text.split(" ")

    if len(kex) > 2:
        ok = await xspam.get_users(kex[2])  
        id = ok.id
        if id in MASTERS:
            await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴅᴇᴠᴇʟᴏᴘᴇʀ ❣️")
        elif id == OWNER_ID:
            await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ 🥀")
        else:
            counts = int(kex[1])
            fname = ok.first_name
            mention = f"[{fname}](tg://user?id={id})"
            for _ in range(counts):
                reply = choice(RAID)
                msg = f"{mention} {reply}"
                await xspam.send_message(message.chat.id, msg)
                await asyncio.sleep(0.1)

    elif message.reply_to_message and (len(kex) == 2):
        user_id = message.reply_to_message.from_user.id
        ok = await xspam.get_users(user_id)
        id = ok.id
        if id in MASTERS:
            await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴅᴇᴠᴇʟᴏᴘᴇʀ ❣️")
        elif id == OWNER_ID:
            await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ 🥀")
        else:
            counts = int(kex[1])
            fname = ok.first_name
            mention = f"[{fname}](tg://user?id={id})"
            for _ in range(counts):
                reply = choice(RAID)
                msg = f"{mention} {reply}"
                await xspam.send_message(message.chat.id, msg)
                await asyncio.sleep(0.3)

    else:
        await message.reply_text(".ʀᴀɪᴅ 10 <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")

rusers = []

@Client.on_message(filters.command("hraid", cmd) & filters.me)
async def hraid(xspam: Client, message: Message):  
    kex = message.text.split(" ")

    if len(kex) > 2:
        ok = await xspam.get_users(kex[2])
        id = ok.id
        if id in MASTERS:
            await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴅᴇᴠᴇʟᴏᴘᴇʀ ❣️")
        elif id == OWNER_ID:
            await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ 🥀")
        else:
            counts = int(kex[1])
            fname = ok.first_name
            mention = f"[{fname}](tg://user?id={id})"
            for _ in range(counts):
                reply = choice(HRAID)
                msg = f"{mention} {reply}"
                await xspam.send_message(message.chat.id, msg)
                await asyncio.sleep(0.3)

    elif message.reply_to_message and (len(kex) == 2):
        user_id = message.reply_to_message.from_user.id
        ok = await xspam.get_users(user_id)
        id = ok.id
        if id in MASTERS:
            await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴅᴇᴠᴇʟᴏᴘᴇʀ ❣️")
        elif id == OWNER_ID:
            await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ 🥀")
        else:
            counts = int(kex[1])
            fname = ok.first_name
            mention = f"[{fname}](tg://user?id={id})"
            for _ in range(counts):
                reply = choice(HRAID)
                msg = f"{mention} {reply}"
                await xspam.send_message(message.chat.id, msg)
                await asyncio.sleep(0.3)

    else:
        await message.reply_text(".ʜʀᴀɪᴅ 10 <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")

add_command_help(
    "➥ 𝐅ᴜᴄᴋ ",
    [
        ["raid", "Raid to user."],
        ["hraid", " Raid to user in hindi"],
    ],
  )
