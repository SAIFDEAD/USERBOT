import asyncio
from html import escape

import aiohttp
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram import enums

from X.helpers.basic import edit_or_reply
from .help import *


@Client.on_message(filters.command(["weather", "w"], ".") & filters.me)
async def get_weather(bot: Client, message: Message):
    if len(message.command) == 1:
        await message.edit("Usage: `.weather Delhi`")
        await asyncio.sleep(3)
        await message.delete()

    if len(message.command) > 1:
        location = message.command[1]
        headers = {"user-agent": "httpie"}
        url = f"https://wttr.in/{location}?mnTC0&lang=en"
        try:
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.get(url) as resp:
                    data = await resp.text()
        except Exception:
            await message.edit("Failed to get the weather forecast")

        if "ᴡᴇ ᴘʀᴏᴄᴇꜱꜱᴇᴅ ᴍᴏʀᴇ ᴛʜᴀɴ 𝟷M ʀᴇǫᴜᴇꜱᴛꜱ ᴛᴏᴅᴀʏ" in data:
            await message.edit("`Sᴏʀʀʏ, ᴡᴇ ᴄᴀɴɴᴏᴛ ᴘʀᴏᴄᴇꜱꜱ ᴛʜɪꜱ ʀᴇǫᴜᴇꜱᴛ ᴛᴏᴅᴀʏ!`")
        else:
            weather = f"{escape(data.replace('report', 'Report'))}"
            await message.edit(weather, parse_mode=enums.ParseMode.MARKDOWN)


add_command_help(
    "•─╼⃝𖠁 ᴡᴇᴀᴛʜᴇʀ",
    [
        [".weather", "Gᴇᴛꜱ ᴡᴇᴀᴛʜᴇʀ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғᴏʀ ᴘʀᴏᴠɪᴅᴇᴅ ʟᴏᴄᴀᴛɪᴏɴ."],
    ],
)
