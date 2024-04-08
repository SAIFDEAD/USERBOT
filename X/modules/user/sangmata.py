import asyncio

from pyrogram import *
from pyrogram import filters
from pyrogram.errors import YouBlockedUser
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.types import *

from config import CMD_HANDLER
from X.helpers.basic import edit_or_reply
from X.utils import extract_user

from .help import *


@Client.on_message(filters.command(["sg", "sa", "sangmata"], cmd) & filters.me)
async def sg(client: Client, message: Message):
    args = await extract_user(message)
    lol = await edit_or_reply(message, "ɪ'ᴍ ᴄᴜʀɪᴏᴜs, ᴡʜᴀᴛ's ᴛʜᴇ ɴᴀᴍᴇ ᴏғ ᴘᴇᴘᴇᴋ?....`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            return await lol.edit(f"`ᴘʟᴇᴀsᴇ sᴘᴇᴄɪғʏ ᴀ ᴠᴀʟɪᴅ ᴜsᴇʀ !`")
    bot = "@SangMata_BOT"
    try:
        await client.send_message(bot, f"{user.id}")
    except YouBlockedUser:
        await client.unblock_user(bot)
        await client.send_message(bot, f"{user.id}")
    await asyncio.sleep(1)

    async for stalk in client.search_messages(bot, query="Name", limit=10):
        if not stalk:
            await message.edit_text("**ᴛʜɪs ᴘᴇʀsᴏɴ ʜᴀs ɴᴇᴠᴇʀ ᴄʜᴀɴɢᴇᴅ ʜɪs ɴᴀᴍᴇ**")
            return
        elif stalk:
            await message.edit(stalk.text)
            await stalk.delete()

    async for stalk in client.search_messages(bot, query="Username", limit=1):
        if not stalk:
            return
        elif stalk:
            await message.reply(stalk.text)
            await stalk.delete()
    user_info = await client.resolve_peer(bot)
    return await client.send(DeleteHistory(peer=user_info, max_id=0, revoke=True))


add_command_help(
    "➥ 𝐒ᴀɴɢᴍᴀᴛᴀ",
    [
        [
            f"{cmd}sg <ʀᴇᴘʟʏ/ᴜꜱᴇʀɪᴅ/ᴜꜱᴇʀɴᴀᴍᴇ>",
            "Tᴏ ɢᴇᴛ ᴜꜱᴇʀ ɴᴀᴍᴇ ʜɪꜱᴛᴏʀʏ ᴡʜɪʟᴇ ᴏɴ Tᴇʟᴇɢʀᴀᴍ.",
        ],
    ],
) 
