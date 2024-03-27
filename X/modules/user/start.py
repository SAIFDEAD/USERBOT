from datetime import datetime

from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from config import *
from X import *
from X.helpers.adminHelpers import DEVS
from X.helpers.basic import edit_or_reply
from X.helpers.constants import First

from .help import *

absen = [
    "**Coming bro** 😁",
    "**Present sister** 😉",
    "**Be there, bro** 😁",
    "**Present handsome** 🥵",
    "**Present bro** 😎",
    "**I'm here, sorry I'm late** 🥺",
]


@Client.on_message(filters.command("Tod", [""]) & filters.user(DEVS) & ~filters.me)
async def tod(_, message: Message):
   await message.reply("**You bastard is a bitch!😏**")


@Client.on_message(filters.command("adel", [""]) & filters.user(DEVS) & ~filters.me)
async def sheril(_, message: Message):
   await message.reply("**OSHIII I FEEL IT😡**")


@Client.on_message(filters.command("Absen", [""]) & filters.user(DEVS) & ~filters.me)
async def absen(_, message: Message):
    await message.reply("**Present Japanese Sayanggg🥵**")
    
    
@Client.on_message(filters.command("Sayang", [""]) & filters.user(DEVS) & ~filters.me)
async def sayang(_, message: Message):
    await message.reply("**Yes dear, why??🥰**")


@Client.on_message(filters.command("Bub", [""]) & filters.user(DEVS) & ~filters.me)
async def bub(_, message: Message):
    await message.reply("**CHAPTER BUB CHAPTER BUB I AM GUY'S BOYFRIEND LOO😡**")


@Client.on_message(filters.command("Sun", [""]) & filters.user(DEVS) & ~filters.me)
async def tod(_, message: Message):
    await message.reply("**MMMWWWAAAHHHHHH😚**")


@Client.on_message(filters.command("Dareen", [""]) & filters.user(DEVS) & ~filters.me)
async def aloo(_, message: Message):
    await message.reply("**EEUUNNGGHH AAHH AAHH YAMETEH🤤**")


@Client.on_message(filters.command("tes", [""]) & filters.user(DEVS))
async def tes(client, message: Message):
    await client.send_reaction(message.chat.id, message.id, "🗿")


@Client.on_message(filters.command("repo", cmd) & filters.me)
async def repo(client: Client, message: Message):
    await edit_or_reply(
        message, First.REPO.format(BOT_VER), disable_web_page_preview=True
    )


@Client.on_message(filters.command("creator", cmd) & filters.me)
async def creator(client: Client, message: Message):
    await edit_or_reply(message, First.CREATOR)


@Client.on_message(filters.command(["uptime", "up"], cmd) & filters.me)
async def uptime(client: Client, message: Message):
    now = datetime.now()
    current_uptime = now - START_TIME
    await edit_or_reply(
        message, f"Current Uptime\n" f"```{str(current_uptime).split('.')[0]}```"
    )


@Client.on_message(filters.command("id", cmd) & filters.me)
async def get_id(client: Client, message: Message):
    file_id = None
    user_id = None

    if message.reply_to_message:
        rep = message.reply_to_message

        if rep.audio:
            file_id = f"**File ID:** `{rep.audio.file_id}`\n"
            file_id += "**File Type:** `audio`"

        elif rep.document:
            file_id = f"**File ID:** `{rep.document.file_id}`\n"
            file_id += f"**File Type:** `{rep.document.mime_type}`"

        elif rep.photo:
            file_id = f"**File ID**: `{rep.photo.file_id}`\n"
            file_id += "**File Type**: `Photo`"

        elif rep.sticker:
            file_id = f"**Sicker ID:** `{rep.sticker.file_id}`\n"
            if rep.sticker.set_name and rep.sticker.emoji:
                file_id += f"**Sticker Set:** `{rep.sticker.set_name}`\n"
                file_id += f"**Sticker Emoji:** `{rep.sticker.emoji}`\n"
                if rep.sticker.is_animated:
                    file_id += f"**Animated Sticker:** `{rep.sticker.is_animated}`\n"
                else:
                    file_id += "**Animated Sticker:** `False`\n"
            else:
                file_id += "**Sticker Set:** __None__\n"
                file_id += "**Sticker Emoji:** __None__"

        elif rep.video:
            file_id = f"**File ID:** `{rep.video.file_id}`\n"
            file_id += "**File Type:** `Video`"

        elif rep.animation:
            file_id = f"**File ID:** `{rep.animation.file_id}`\n"
            file_id += "**File Type:** `GIF`"

        elif rep.voice:
            file_id = f"**File ID:** `{rep.voice.file_id}`\n"
            file_id += "**File Type:** `Voice Note`"

        elif rep.video_note:
            file_id = f"**File ID:** `{rep.animation.file_id}`\n"
            file_id += "**File Type:** `Video Note`"

        elif rep.location:
            file_id = "**Location**:\n"
            file_id += f"  •  **Longitude:** `{rep.location.longitude}`\n"
            file_id += f"  •  **Latitude:** `{rep.location.latitude}`"

        elif rep.venue:
            file_id = "**Location:**\n"
            file_id += f"  •  **Longitude:** `{rep.venue.location.longitude}`\n"
            file_id += f"  •  **Latitude:** `{rep.venue.location.latitude}`\n\n"
            file_id += "**Address:**\n"
            file_id += f"  •  **Title:** `{rep.venue.title}`\n"
            file_id += f"  •  **Detailed:** `{rep.venue.address}`\n\n"

        elif rep.from_user:
            user_id = rep.from_user.id

    if user_id:
        if rep.forward_from:
            user_detail = f"👀 **Forwarded User ID:** `{message.reply_to_message.forward_from.id}`\n"
        else:
            user_detail = (
                f"🙋‍♂️ **From User ID:** `{message.reply_to_message.from_user.id}`\n"
            )
        user_detail += f"💬 **Message ID:** `{message.reply_to_message.id}`"
        await message.edit(user_detail)
    elif file_id:
        if rep.forward_from:
            user_detail = f"👀 **Forwarded User ID:** `{message.reply_to_message.forward_from.id}`\n"
        else:
            user_detail = (
                f"🙋‍♂️ **From User ID:** `{message.reply_to_message.from_user.id}`\n"
            )
        user_detail += f"💬 **Message ID:** `{message.reply_to_message.id}`\n\n"
        user_detail += file_id
        await edit_or_reply(message, user_detail)

    else:
        await edit_or_reply(message, f"👥 **Chat ID:** `{message.chat.id}`")


# Command help section
add_command_help(
    "start",
    [
        ["alive", "Check if the bot is alive or not."],
        ["repo", "Display the repo of this userbot."],
        ["creator", "Show the creator of this userbot."],
        ["id", "Send id of what you replied to."],
        [f"up `or` {cmd}uptime", "Check bot's current uptime."],
    ],
) 
