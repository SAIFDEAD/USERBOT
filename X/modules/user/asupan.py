from asyncio import gather
from random import choice

from pyrogram import Client, enums, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from X.helpers.basic import edit_or_reply
from X.helpers.PyroHelpers import ReplyCheck

from .help import *


@Client.on_message(filters.command(["asupan", "ptl"], cmd) & filters.me)
async def asupan_cmd(client: Client, message: Message):
    X = await edit_or_reply(message, "`Wait More Search for Lu's Intake...`")
    await gather(
        X.delete(),
        client.send_video(
            message.chat.id,
            choice(
                [
                    asupan.video.file_id
                    async for asupan in client.search_messages(
                        "have it", filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )

@Client.on_message(filters.command(["bkp"], cmd) & filters.me)
async def bkp_cmd(client: Client, message: Message):
    X = await edit_or_reply(message, "`Wait More Find Bra Material For Lu..`")
    await gather(
        X.delete(),
        client.send_video(
            message.chat.id,
            choice(
                [
                    bkp.video.file_id
                    async for bkp in client.search_messages(
                        "bokepX", filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )


# WARNING PORNO VIDEO THIS !!!



@Client.on_message(filters.command(["ayang"], cmd) & filters.me)
async def ayang(client, message):
    yanto = await message.reply("🔎 `Search Is...`")
    pop = message.from_user.first_name
    ah = message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "CeweLogoPack", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"Unfortunately [{pop}](tg://user?id={ah}) 💝",
    )

    await yanto.delete()


@Client.on_message(filters.command(["ppcp", "couple"], cmd) & filters.me)
async def ppcp(client, message):
    yanto = await message.reply("🔎 `Search PP Couple...`")
    message.from_user.first_name
    message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "ppcpcilik", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"📌 PP Couple Alay Lo This is Tod",
    )

    await yanto.delete()


@Client.on_message(filters.command(["ppanime"], cmd) & filters.me)
async def ppanime(client, message):
    yanto = await message.reply("🔎 `Search PP Anime...`")
    message.from_user.first_name
    message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "animehikarixa", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"📌 PP Wibu Lu Nih Tod",
    )

    await yanto.delete()


add_command_help(
    "asupan",
    [
        [
            f"asupan atau {cmd}ptl",
            "To send intake videos randomly.",
        ],
        [
            f"ayang {cmd}",
            "To search for random photos of Ayang.",
        ],
        [
            f"ppcp atau {cmd}couple",
            "To Search for Pp Couples Randomly.",
        ],
        [
            f"ppanime {cmd}",
            "To search for anime pp randomly.",
        ]
    ],
) 