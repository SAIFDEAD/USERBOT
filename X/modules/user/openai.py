from pyrogram import *
from pyrogram.types import *
from pyrogram import Client as kaz
from pyrogram.errors import MessageNotModified
from X.helpers.basic import *
from X.helpers.adminHelpers import DEVS
from config import *
from config import CMD_HANDLER
from X.utils import *
from urllib.parse import quote

import requests
import os
import json
import random

from .help import *

@Client.on_message(filters.command("ai", ".") & filters.me)
async def openai(client: Client, message: Message):
    if len(message.command) == 1:
        return await message.reply(f"𝐊𝐞𝐭𝐢𝐤 <code>.{message.command[0]} [ǫᴜᴇsᴛɪᴏɴ]</code> ǫᴜᴇsᴛɪᴏɴs ғᴏʀ ᴜsᴇ ᴏᴘᴇɴᴀɪ")
    
    question = message.text.split(" ", maxsplit=1)[1]
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }

    url = f"https://api.ajinkya.link/gpt.php?question={question}"
    
    msg = await message.reply("`Be patient..")
    
    try:
        response = requests.get(url).json()
        await msg.edit(response["answer"])
    except MessageNotModified:
        pass
    except Exception:
        await msg.edit("Sᴏʀʀʏ Cʜᴀᴛ Gᴘᴛ ɪs ᴀᴛ ʀᴇsᴛ ᴄᴜʀʀᴇɴᴛʟʏ ᴅᴏ ʏᴏᴜʀ ᴡᴏʀᴋ ʙʏ ʏᴏᴜʀ sᴇʟғ")

add_command_help(
    "➥ 𝐎ᴘᴇɴᴀɪ",
    [
        ["ai", "Tᴏ Aꜱᴋ Sᴏᴍᴇᴛʜɪɴɢ Tᴏ Cʜᴀᴛ Gᴘᴛ"],
    ],
)
