from pyrogram import Client, filters
from pyrogram.types import Message
from X.helpers.basic import edit_or_reply
from .help import *

the_regex = r"^r\/([^\s\/])+"

f = filters.chat([])


@Client.on_message(f)
async def auto_read(bot: Client, message: Message):
    await X.read_history(message.chat.id)
    message.continue_propagation()


@Client.on_message(filters.command("autoscroll", ".") & filters.me)
async def add_to_auto_read(bot: Client, message: Message):
    if message.chat.id in f:
        f.remove(message.chat.id)
        await message.edit("Autoscroll deactivated")
    else:
        f.add(message.chat.id)
        await message.edit("Autoscroll activated")


add_command_help(
    "•─╼⃝𖠁 ᴀᴜᴛᴏꜱᴄʀᴏʟʟ",
    [
        [
            ".autoscroll",
            "Sᴇɴᴅ .ᴀᴜᴛᴏꜱᴄʀᴏʟʟ ɪɴ ᴀɴʏ ᴄʜᴀᴛ ᴛᴏ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʀᴇᴀᴅ ᴀʟʟ ꜱᴇɴᴛ ᴍᴇꜱꜱᴀɢᴇꜱ ᴜɴᴛɪʟ ʏᴏᴜ ᴄᴀʟʟ "
            "ᴀᴜᴛᴏꜱᴄʀᴏʟʟ ᴀɢᴀɪɴ. Tʜɪꜱ ɪꜱ ᴜꜱᴇғᴜʟ ɪғ ʏᴏᴜ ʜᴀᴠᴇ Tᴇʟᴇɢʀᴀᴍ ᴏᴘᴇɴ ᴏɴ ᴀɴᴏᴛʜᴇʀ ꜱᴄʀᴇᴇɴ.",
        ],
    ],
)
