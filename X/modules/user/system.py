import sys
from os import environ, execle, remove

from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from X import BOTLOG_CHATID, LOGGER
from X.helpers.adminHelpers import DEVS
from X.helpers.basic import edit_or_reply

from .help import *

HAPP = None


@Client.on_message(filters.command("restc", ["."]) & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.command("restart", cmd) & filters.me)
async def restart_bot(_, message: Message):
    try:
        msg = await edit_or_reply(message, "`𝐃ɪᴄᴛᴀᴛᴏʀ 𝐔sᴇʀ𝐁ᴏᴛ 𝐑𝐄𝐒𝐓𝐀𝐑𝐓𝐈𝐍𝐆.....`")
        LOGGER(__name__).info("BOT SERVER RESTARTED !!")
    except BaseException as err:
        LOGGER(__name__).info(f"{err}")
        return
    await msg.edit_text("✅ ʙᴏᴛ ʜᴀs ʀᴇsᴛᴀʀᴛᴇᴅ !\n\n")
    if HAPP is not None:
        HAPP.restart()
    else:
        args = [sys.executable, "-m", "X"]
        execle(sys.executable, *args, environ)


@Client.on_message(filters.command("shutdown", cmd) & filters.me)
async def shutdown_bot(client: Client, message: Message):
    if BOTLOG_CHATID:
        await client.send_message(
            BOTLOG_CHATID,
            "**#sʜᴜᴛᴅᴏᴡɴ** \n"
            "**𝐃ɪᴄᴛᴀᴛᴏʀ 𝐔sᴇʀ𝐁ᴏᴛ** ʜᴀs ʙᴇᴇɴ ᴛᴜʀɴᴇᴅ ᴏғғ!\ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴛᴜʀɴ it ʙᴀᴄᴋ on, ᴘʟᴇᴀsᴇ ᴏᴘᴇɴ it heroku",
        )
    await edit_or_reply(message, "**𝐃ɪᴄᴛᴀᴛᴏʀ 𝐔sᴇʀ𝐁ᴏᴛ sᴜᴄᴄᴇssғᴜʟʟʏ ᴛᴜʀɴᴇᴅ ɪᴛ ᴏғғ!**")
    if HAPP is not None:
        HAPP.process_formation()["worker"].scale(0)
    else:
        sys.exit(0)


@Client.on_message(filters.command("logs", cmd) & filters.me)
async def logs_ubot(client: Client, message: Message):
    if HAPP is None:
        return await edit_or_reply(
            message,
            "Make sure `HEROKU_API_KEY` and `HEROKU_APP_NAME` you are configured correctly in config vars heroku",
        )
    Man = await edit_or_reply(message, "**Currently Taking Logs Heroku**")
    with open("Logs-Heroku.txt", "w") as log:
        log.write(HAPP.get_log())
    await client.send_document(
        message.chat.id,
        "𝐃ɪᴄᴛᴀᴛᴏʀ 𝐔sᴇʀ𝐁ᴏᴛ",
        thumb="X/resources/logo.jpg",
        caption="**ᴛʜɪs ɪs ʏᴏᴜʀ ʜᴇʀᴏᴋᴜ ʟᴏɢs**",
    )
    await Man.delete()
    remove("Logs-Heroku.txt")


add_command_help(
    "➥ 𝐒ʏꜱᴛᴇᴍ",
    [
        ["restart", "Tᴏ ʀᴇꜱᴛᴀʀᴛ ᴜꜱᴇʀʙᴏᴛ."],
        ["shutdown", "Tᴏ ᴛᴜʀɴ ᴏғғ ᴜꜱᴇʀʙᴏᴛ."],
        ["logs", "Tᴏ ꜱᴇᴇ ʟᴏɢꜱ ᴜꜱᴇʀʙᴏᴛ."],
    ],
) 
