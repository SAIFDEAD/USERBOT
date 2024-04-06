import asyncio
import random
from pyrogram import Client, filters
from pyrogram.types import Message
from config import CMD_HANDLER
from X import *
from X.helpers.adminHelpers import DEVS
from X.utils.misc import extract_user_and_reason
from X.helpers.tools import get_arg

from .help import *

ok = []
nyet = [
    "50",
    "350",
    "97",
    "670",
    "24",
    "909",
    "57",
    "89",
    "4652",
    "153",
    "877",
    "890",
]
babi = [
    "2",
    "3",
    "6",
    "7",
    "9"
]


@Client.on_message(
    filters.command(["cigiben"], ".") & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command(["giben"], cmd) & filters.me)
async def giben(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    if message.from_user.id != client.me.id:
        ex = await message.reply_text("`ɢʙᴀɴɪɴɢ...`")
    else:
        ex = await message.edit("`ɢʙᴀɴɴɪɴɢ!`")
    if not user_id:
        return await ex.edit("ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ ᴍᴇssᴀɢᴇs ᴏʀ ᴘʀᴏᴠɪᴅᴇ ᴜsᴇʀɴᴀᴍᴇ/ᴜsᴇʀ_id")
    if user_id == client.me.id:
        return await ex.edit("**ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ʙᴀɴ ʏᴏᴜʀsᴇʟғ? sᴛᴜᴘɪᴅ!**")
    if user_id in DEVS:
        return await ex.edit("**ᴅᴇᴠs ʏᴏᴜ ᴄᴀɴ'ᴛ ʙᴀɴ ɪᴛ **")
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await ex.edit("`ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ ᴍᴇssᴀɢᴇs ᴏʀ ᴘʀᴏᴠɪᴅᴇ ᴜsᴇʀɴᴀᴍᴇ/ᴜsᴇʀ_id`")        
    ok.append(user.id)
    done = random.choice(nyet)
    msg = (
        r"**#𝐆ʙᴀɴɴᴇᴅ**"
        f"\n\n**𝐍ᴀᴍᴇ:** [{user.first_name}](tg://user?id={user.id})"
        f"\n**𝐔sᴇʀ 𝐈ᴅ:** `{user.id}`"
    )
    if reason:
        msg += f"\n**𝐑ᴇᴀsᴏɴ:** `{reason}`"
    msg += f"\n**𝐒ᴜᴄᴄᴇss 𝐎ғ:** `{done}` **𝐂ʜᴀᴛ**"
    await asyncio.sleep(5)
    await ex.edit(msg)

@Client.on_message(
    filters.command("cigimut", ["."]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command(["gimut"], cmd) & filters.me)
async def gimut(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    if message.from_user.id != client.me.id:
        ex = await message.reply_text("`GMuting...`")
    else:
        ex = await message.edit("`Gmuting...`")
    if not user_id:
        return await ex.edit("Reply to user messages or provide username/user_id")
    if user_id == client.me.id:
        return await ex.edit("**Do you want to mute yourself? Stupid!**")
    if user_id in DEVS:
        return await ex.edit("**Devs You can't ban it, you bastard, only God can🗿**")
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await ex.edit("`Reply to user messages or provide username/user_id`")
    ok.append(user.id)
    done = random.choice(nyet)
    msg = (
        r"**#GMuted**"
        f"\n\n**Namae** [{user.first_name}](tg://user?id={user.id})"
        f"\n**User ID:** `{user.id}`"
    )
    if reason:
        msg += f"\n**Reason:** `{reason}`"
    msg += f"\n**Sukses Of:** `{done}` **Chat**"
    await asyncio.sleep(5)
    await ex.edit(msg)

@Client.on_message(
    filters.command("cigikik", ["."]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command(["gikik"], cmd) & filters.me)
async def gikik(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    if message.from_user.id != client.me.id:
        ex = await message.reply_text("`GKick...`")
    else:
        ex = await message.edit("`Gkicking...!`")
    if not user_id:
        return await ex.edit("Reply to user messages or provide username/user_id")
    if user_id == client.me.id:
        return await ex.edit("**Do you want to kick yourself? Stupid!**")
    if user_id in DEVS:
        return await ex.edit("**ᴅᴇᴠs ʏᴏᴜ ᴄᴀɴ'ᴛ ᴋɪᴄᴋ ɪᴛ, ʏᴏᴜ ʙᴀsᴛᴀʀᴅ, ᴏɴʟʏ ɢᴏᴅ ᴄᴀɴ🗿**")
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await ex.edit("`ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ ᴍᴇssᴀɢᴇs ᴏʀ ᴘʀᴏᴠɪᴅᴇ ᴜsᴇʀɴᴀᴍᴇ/ᴜsᴇʀ_id`")
    ok.append(user.id)
    done = random.choice(nyet)
    msg = (
        r"**#ɢᴋɪᴄᴋᴇᴅ**"
        f"\n\n**ɴᴀᴍᴇ:** [{user.first_name}](tg://user?id={user.id})"
        f"\n**ᴜsᴇʀ ɪᴅ:** `{user.id}`"
    )
    if reason:
        msg += f"\n**ʀᴇᴀsᴏɴ:** `{reason}`"
    msg += f"\n**sᴜᴄᴄᴇss ᴏғ:** `{done}` **ᴄʜᴀᴛ**"
    await asyncio.sleep(5)
    await ex.edit(msg)


@Client.on_message(
    filters.command("cigikes", ["."]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command(["gikes"], cmd) & filters.me)
async def gcast_cmd(client: Client, message: Message):
    if message.reply_to_message or get_arg(message):
        tex = await message.reply_text("`sᴛᴀʀᴛᴇᴅ ɢʟᴏʙᴀʟ ʙʀᴏᴀᴅᴄᴀsᴛ...`")
    else:
        return await message.edit_text("**ɢɪᴠᴇ A ᴍᴇssᴀɢᴇ ᴏʀ ʀᴇᴘʟʏ**")
    done = random.choice(nyet)
    fail = random.choice(babi)
    await asyncio.sleep(5)
    await tex.edit_text(
        f"**sᴜᴄᴄᴇssғᴜʟʟʏ sᴇɴᴛ ᴍᴇssᴀɢᴇ ᴛᴏ** `{done}` **Groups chat, Failed to Send Message To** `{fail}` **Groups**"
    )

add_command_help(
    "➥ 𝐅ᴀᴋᴇ",
    [
        [f"giben <ʀᴇᴘʟʏ/ᴜꜱᴇʀɴᴀᴍᴇ/ᴜꜱᴇʀɪᴅ>", "Fᴀᴋᴇ Gʟᴏʙᴀʟ Bᴀɴɴɪɴɢ."],
        [f"gimut <ʀᴇᴘʟʏ/ᴜꜱᴇʀɴᴀᴍᴇ/ᴜꜱᴇʀɪᴅ>", "Fᴀᴋᴇ Gʟᴏʙᴀʟ Mᴜᴛᴇ."],
        [f"gikik <ʀᴇᴘʟʏ/ᴜꜱᴇʀɴᴀᴍᴇ/ᴜꜱᴇʀɪᴅ>", "Fᴀᴋᴇ Gʟᴏʙᴀʟ Kɪᴄᴋ."],
        [f"gikes <ʀᴇᴘʟʏ/ᴜꜱᴇʀɴᴀᴍᴇ/ᴜꜱᴇʀɪᴅ>", "Fᴀᴋᴇ Gʟᴏʙᴀʟ ʙʀᴏᴀᴅᴄᴀꜱᴛ."],
    ],
  )
