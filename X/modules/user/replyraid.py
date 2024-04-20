from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from XDB.data import MASTERS, SDICTATOR
from config import OWNER_ID
from config import CMD_HANDLER as cmd
from .help import *
import asyncio 

rusers = []

@Client.on_message(filters.command("rraid", cmd) & filters.me)
async def rraid(xspam: Client, message: Message):
    global rusers
    kex = message.text.split(" ")

    if len(kex) > 1:
        ok = await xspam.get_users(kex[1])
        id = ok.id
        if id in MASTERS:
            await message.reply_text("𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 𝙾𝙵 𝙳𝙸𝙲𝚃𝙰𝚃𝙾𝚁 𝚄𝚂𝙴𝚁𝙱𝙾𝚃")
        elif id == OWNER_ID:
            await message.reply_text("𝙾𝚆𝙽𝙴𝚁 𝙾𝙵 𝚄𝚂𝙴𝚁𝙱𝙾𝚃🥀")
        else:
            rusers.append(id)
            await message.reply_text("ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏʀᴀɪᴅ ✅")

    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        if id in MASTERS:
            await message.reply_text("𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 𝙾𝙵 𝙳𝙸𝙲𝚃𝙰𝚃𝙾𝚁 𝚄𝚂𝙴𝚁𝙱𝙾𝚃")
        elif id == OWNER_ID:
            await message.reply_text("𝙾𝚆𝙽𝙴𝚁 𝙾𝙵 𝚄𝚂𝙴𝚁𝙱𝙾𝚃🥀")
        else:
            rusers.append(user_id)
            await message.reply_text("» ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏʀᴀɪᴅ ✅")

    else:
        await message.reply_text(".ʀʀᴀɪᴅ <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")

@Client.on_message(filters.command("draid", cmd) & filters.me)
async def draid(xspam: Client, message: Message):
    global rusers
    kex = message.text.split(" ")

    if len(kex) > 1:
        ok = await xspam.get_users(kex[1])
        id = ok.id
        if id in rusers:
            rusers.remove(id)
            await message.reply_text("ʀᴇᴘʟʏ ʀᴀɪᴅ ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛᴇᴅ ✅")

    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        ok = await xspam.get_users(user_id)
        id = ok.id
        if id in rusers:
            rusers.remove(id)
            await message.reply_text("ʀᴇᴘʟʏ ʀᴀɪᴅ ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛᴇᴅ ✅")

    else:
        await message.reply_text(".ᴅʀʀᴀɪᴅ <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")

@Client.on_message(~filters.me & filters.incoming)
async def watcher(_, msg: Message):
    global rusers
    id = msg.from_user.id
    if id in rusers:
        reply = choice(SDICTATOR)
        await msg.reply_text(reply)


add_command_help(
    "➥ 𝐑ᴇᴘʟʏʀᴀɪᴅ",
    [
        ["rraid", "start rraid."],
        ["draid", "remove rraid"],

    ],
        
  )
