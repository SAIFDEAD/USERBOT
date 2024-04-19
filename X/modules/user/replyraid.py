from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from XDB.data import MASTERS, SDICTATOR
from config import OWNER_ID
from config import CMD_HANDLER as cmd
from .help import *
import asyncio

async def rraid(e):
    if e.sender_id in SUDO_USERS:
        mkrr = e.text.split(" ", 1)
        if len(mkrr) == 2:
            entity = await e.client.get_entity(mkrr[1])

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)

        try:
            user_id = entity.id
            if user_id in ALTRON:
                await e.reply("𝙽𝙾, 𝚃𝙷𝙸𝚂 𝙶𝚄𝚈 𝙸𝚂 𝙳𝙴𝚅𝙻𝙾𝙿𝙴𝚁 𝙾𝙵 𝙳𝙴𝙰𝙳 𝙱𝙾𝚃 ")
            elif user_id == OWNER_ID:
                await e.reply("𝙽𝙾, 𝚃𝙷𝙸𝚂 𝙶𝚄𝚈 𝙸𝚂 𝙾𝚆𝙽𝙴𝚁 𝙾𝙵 𝙳𝙴𝙰𝙳 𝙱𝙾𝚃 .")
            elif user_id in SUDO_USERS:
                await e.reply("𝙽𝙾, 𝚃𝙷𝙸𝚂 𝙶𝚄𝚈 𝙸𝚂 𝚂𝚄𝙳𝙾 𝚄𝚂𝙴𝚁 𝙾𝙵 𝙳𝙴𝙰𝙳 𝙱𝙾𝚃 .")
            else:
                global REPLY_RAID
                check = f"{user_id}_{e.chat_id}"
                if check not in REPLY_RAID:
                    REPLY_RAID.append(check)
                await e.reply("» ᴛʜɪᴋ ʜᴀɪ ʙʜᴀɪ ʙᴏʟɴᴇ ᴅᴏ ᴇs ᴍᴄ ᴋᴏ !! ✅")
        except NameError:
            await e.reply(f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐑𝐞𝐩𝐥𝐲𝐑𝐚𝐢𝐝\n  » {hl}rraid <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » {hl}rraid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>"

async def drraid(e):
    if e.sender_id in SUDO_USERS:
        text = e.text.split(" ", 1)

        if len(text) == 2:
            entity = await e.client.get_entity(text[1])
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)

        try:
            check = f"{entity.id}_{e.chat_id}"
            global REPLY_RAID
            if check in REPLY_RAID:
                REPLY_RAID.remove(check)
            await e.reply("» ᴛʜɪᴋ ʜᴀɪ ᴍᴀғ ᴋᴀʀ ʀʜᴇ ʜᴀɪ !! ✅")
        except NameError:
            await e.reply(f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐃𝐑𝐞𝐩𝐥𝐲𝐑𝐚𝐢𝐝\n  » {hl}drraid <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » {hl}drraid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
