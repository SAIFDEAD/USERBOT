from asyncio import sleep

from pyrogram import Client, enums, filters
from pyrogram.raw import functions
from pyrogram.types import Message

from config import CMD_HANDLER
from X.helpers.PyroHelpers import ReplyCheck

from .help import *

commands = {
    "ftyping": enums.ChatAction.TYPING,
    "fvideo": enums.ChatAction.RECORD_VIDEO,
    "faudio": enums.ChatAction.RECORD_AUDIO,
    "fround": enums.ChatAction.RECORD_VIDEO_NOTE,
    "fphoto": enums.ChatAction.UPLOAD_PHOTO,
    "fsticker": enums.ChatAction.CHOOSE_STICKER,
    "fdocument": enums.ChatAction.UPLOAD_DOCUMENT,
    "flocation": enums.ChatAction.FIND_LOCATION,
    "fgame": enums.ChatAction.PLAYING,
    "fcontact": enums.ChatAction.CHOOSE_CONTACT,
    "fstop": enums.ChatAction.CANCEL,
    "fscreen": "screenshot",
}


@Client.on_message(filters.command(list(commands), cmd) & filters.me)
async def fakeactions_handler(client: Client, message: Message):
    cmd = message.command[0]
    try:
        sec = int(message.command[1])
        if sec > 60:
            sec = 60
    except:
        sec = None
    await message.delete()
    action = commands[cmd]
    try:
        if action != "screenshot":
            if sec and action != enums.ChatAction.CANCEL:
                await client.send_chat_action(chat_id=message.chat.id, action=action)
                await sleep(sec)
            else:
                return await client.send_chat_action(
                    chat_id=message.chat.id, action=action
                )
        else:
            for _ in range(sec if sec else 1):
                await client.send(
                    functions.messages.SendScreenshotNotification(
                        peer=await client.resolve_peer(message.chat.id),
                        reply_to_msg_id=0,
                        random_id=client.rnd_id(),
                    )
                )
                await sleep(0.1)
    except Exception as e:
        return await client.send_message(
            message.chat.id,
            f"**ERROR:** `{e}`",
            reply_to_message_id=ReplyCheck(message),
        )


add_command_help(
    "fakeaction",
    [
        ["ftyping [detik]", "Shows Fake Typing in chat."],
        ["fgame [detik]", "Shows playing a Fake game in chat."],
        [
            "faudio [detik]",
            "Shows the action of recording a fake voice in chat.",
        ],
        [
            "fvideo [detik]",
            "Shows the action of recording a fake video in chat.",
        ],
        [
            "fround [detik]",
            "Shows the action of recording a fake video in chat.",
        ],
        [
            "fphoto [detik]",
            "Shows the action of sending fake photos in chat.",
        ],
        [
            "fsticker [detik]",
            "Displays the action of selecting fake stickers in chat.",
        ],
        [
            "fcontact [detik]",
            "Displays a fake Share Contact action in chat.",
        ],
        [
            "flocation [detik]",
            "Displays a fake Share Location action in chat.",
        ],
        [
            "fdocument [detik]",
            "Displays the action of sending fake documents/files in chat.",
        ],
        [
            "fscreen [jumlah]",
            "Displays a fake screenshot action. (Use in Private Chat).",
        ],
        ["fstop", "Stops fake actions in chat."],
    ],
) 