from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from X.helpers.basic import edit_or_reply

from .help import *


@Client.on_message(filters.command("create", cmd) & filters.me)
async def create(client: Client, message: Message):
    if len(message.command) < 3:
        return await edit_or_reply(
            message, f"**ᴛʏᴘᴇ {cmd}ʜᴇʟᴘ ᴄʀᴇᴀᴛᴇ ɪғ ʏᴏᴜ ɴᴇᴇᴅ ʜᴇʟᴘ**"
        )
    group_type = message.command[1]
    split = message.command[2:]
    group_name = " ".join(split)
    Man = await edit_or_reply(message, "`ᴘʀᴏᴄᴇssɪɴɢ...`")
    desc = "ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴍʏ " + ("ɢʀᴏᴜᴘ" if group_type == "gc" else "ᴄʜᴀɴɴᴇʟ")
    if group_type == "gc":  # for supergroup
        _id = await client.create_supergroup(group_name, desc)
        link = await client.get_chat(_id["id"])
        await Man.edit(
            f"**sᴜᴄᴄᴇᴇᴅ ᴍᴀᴋᴇ ɢʀᴏᴜᴘ ᴛᴇʟᴇɢʀᴀᴍ: [{group_name}]({link['invite_link']})**",
            disable_web_page_preview=True,
        )
    elif group_type == "ch":  # for channel
        _id = await client.create_channel(group_name, desc)
        link = await client.get_chat(_id["id"])
        await Man.edit(
            f"**sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʀᴇᴀᴛᴇᴅ ᴄʜᴀɴɴᴇʟ ᴛᴇʟᴇɢʀᴀᴍ: [{group_name}]({link['invite_link']})**",
            disable_web_page_preview=True,
        )


add_command_help(
    "➥ 𝐂ʀᴇᴀᴛᴇ",
    [
        ["create ch", "Tᴏ ᴍᴀᴋᴇ ᴄʜᴀɴɴᴇʟ ᴛᴇʟᴇɢʀᴀᴍ Jᴀᴘᴀɴᴇꜱᴇ ᴜꜱᴇʀʙᴏᴛ"],
        ["create gc", "Tᴏ ᴍᴀᴋᴇ ɢʀᴏᴜᴘ ᴛᴇʟᴇɢʀᴀᴍ Jᴀᴘᴀɴᴇꜱᴇ ᴜꜱᴇʀʙᴏᴛ"],
    ],
)
