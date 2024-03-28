import asyncio

from pyrogram import Client, filters
from pyrogram.raw import functions
from pyrogram.types import Message

from X.helpers.basic import edit_or_reply

from .help import *


@Client.on_message(
    filters.command(["screenshot", "ss"], ".") & filters.private & filters.me
)
async def screenshot(bot: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        bot.invoke(
            functions.messages.SendScreenshotNotification(
                peer=await X.resolve_peer(message.chat.id),
                reply_to_msg_id=0,
                random_id=X.rnd_id(),
            )
        ),
    )


add_command_help(
    "•─╼⃝𖠁 ꜱᴄʀᴇᴇɴꜱʜᴏᴛ",
    [
        [
            ".screenshot",
            "Sᴇɴᴅ ᴀ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ɪɴ ᴀ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ (ɴᴏᴛ ꜱᴇᴄʀᴇᴛ) ᴛᴏ ᴀɴɴᴏʏ ᴏʀ ᴛʀᴏʟʟ ʏᴏᴜʀ ғʀɪᴇɴᴅꜱ.",
        ],
    ],
)
