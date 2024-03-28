import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from X.helpers.tools import get_arg

from .help import *


@Client.on_message(filters.me & filters.command(["q", "quotly"], cmd))
async def quotly(client: Client, message: Message):
    args = get_arg(message)
    if not message.reply_to_message and not args:
        return await message.edit("**Please Reply to Messages**")
    bot = "QuotLyBot"
    if message.reply_to_message:
        await message.edit("`Be patient, dog . . .`")
        await client.unblock_user(bot)
        if args:
            await client.send_message(bot, f"/qcolor {args}")
            await asyncio.sleep(1)
        else:
            pass
        await message.reply_to_message.forward(bot)
        await asyncio.sleep(5)
        async for quotly in client.search_messages(bot, limit=1):
            if quotly:
                await message.delete()
                await message.reply_sticker(
                    sticker=quotly.sticker.file_id,
                    reply_to_message_id=message.reply_to_message.id
                    if message.reply_to_message
                    else None,
                )
            else:
                return await message.edit("**Failed to Make a Quotly Sticker**")


add_command_help(
    "•─╼⃝𖠁 ǫᴜᴏᴛʟʏ",
    [
        [
            f"q or quotly",
            "Mᴀᴋᴇ ᴍᴇꜱꜱᴀɢᴇꜱ ɪɴᴛᴏ ꜱᴛɪᴄᴋᴇʀꜱ ᴡɪᴛʜ ʀᴀɴᴅᴏᴍ ʙᴀᴄᴋɢʀᴏᴜɴᴅꜱ.",
        ],
        [
            f"q <color> or quotly <color>",
            "Mᴀᴋᴇ ᴍᴇꜱꜱᴀɢᴇꜱ ɪɴᴛᴏ ꜱᴛɪᴄᴋᴇʀꜱ ᴡɪᴛʜ ᴛʜᴇ ɢɪᴠᴇɴ ᴄᴜꜱᴛᴏᴍ ʙᴀᴄᴋɢʀᴏᴜɴᴅ ᴄᴏʟᴏʀ.",
        ],
    ],
) 
