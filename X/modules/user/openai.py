from pyrogram import *
from pyrogram.types import *
from pyrogram import Client as kaz
from pyrogram.errors import MessageNotModified
from X.helpers.basic import *
from X.helpers.adminHelpers import DEVS
from config import *
from config import CMD_HANDLER
from X.utils import *

import requests
import os
import json
import random

from .help import *

@kaz.on_message(filters.command("cask", cmd) & filters.user(DEVS) & ~filters.me)
@kaz.on_message(filters.command("ai", cmd) & filters.me)
async def openai(client: Client, message: Message):
    if len(message.command) == 1:
        return await message.reply(f"Ketik <code>.{message.command[0]} [question]</code> Questions for use OpenAI")
    question = message.text.split(" ", maxsplit=1)[1]
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }

    json_data = {
        "model": "gpt-3.5-turbo-instruct",
        "prompt": question,
        "max_tokens": 200,
        "temperature": 0,
    }
    msg = await message.reply("`Be patient..")
    try:
        response = (await http.post("https://api.openai.com/v1/completions", headers=headers, json=json_data)).json()
        await msg.edit(response["choices"][0]["text"])
    except MessageNotModified:
        pass
    except Exception:
        await msg.edit("An Error Has Occurred!!\nYou Have Not Entered OPENAI_API_KEY")

add_command_help(
    "openai",
    [
        ["ai", "To Ask Something To Google"]
    ],
) 
