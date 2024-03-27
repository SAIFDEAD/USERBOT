import asyncio

from pyrogram import Client, filters
from pyrogram.enums import ChatType, UserStatus
from pyrogram.types import Message

from config import CMD_HANDLER
from X import BOTLOG_CHATID
from X.helpers.basic import edit_or_reply

from .help import *


@Client.on_message(filters.me & filters.command("invite", cmd))
async def inviteee(client: Client, message: Message):
    mg = await edit_or_reply(message, "`Adding Users!`")
    user_s_to_add = message.text.split(" ", 1)[1]
    if not user_s_to_add:
        await mg.edit("`Give Me Users To Add! Check Help Menu For More Info!`")
        return
    user_list = user_s_to_add.split(" ")
    try:
        await client.add_chat_members(message.chat.id, user_list, forward_limit=100)
    except BaseException as e:
        await mg.edit(f"`Unable To Add Users! \nTraceBack : {e}`")
        return
    await mg.edit(f"`Sucessfully Added {len(user_list)} To This Group / Channel!`")


@Client.on_message(filters.command(["inviteall"], cmd) & filters.me)
async def inv(client: Client, message: Message):
    X = await edit_or_reply(message, "`Processing . . .`")
    text = message.text.split(" ", 1)
    queryy = text[1]
    chat = await client.get_chat(queryy)
    tgchat = message.chat
    await X.edit_text(f"inviting users from {chat.username}")
    async for member in client.get_chat_members(chat.id):
        user = member.user
        zxb = [
            UserStatus.ONLINE,
            UserStatus.OFFLINE,
            UserStatus.RECENTLY,
            UserStatus.LAST_WEEK,
        ]
        if user.status in zxb:
            try:
                await client.add_chat_members(tgchat.id, user.id)
            except Exception as e:
                mg = await client.send_message(BOTLOG_CHATID, f"**ERROR:** `{e}`")
                await asyncio.sleep(0.3)
                await mg.delete()


@Client.on_message(filters.command("invitelink", cmd) & filters.me)
async def invite_link(client: Client, message: Message):
    X = await edit_or_reply(message, "`Processing...`")
    if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        message.chat.title
        try:
            link = await client.export_chat_invite_link(message.chat.id)
            await X.edit(f"**Link Invite:** {link}")
        except Exception:
            await X.edit("Denied permission")


add_command_help(
    "•─╼⃝𖠁 ɪɴᴠɪᴛᴇ",
    [
        [
            "invitelink",
            "Tᴏ ɢᴇᴛ ᴀɴ ɪɴᴠɪᴛᴇ ʟɪɴᴋ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ ɢʀᴏᴜᴘ. [Nᴇᴇᴅ Aᴅᴍɪɴ]",
        ],
        ["invite @username", "Tᴏ Iɴᴠɪᴛᴇ Mᴇᴍʙᴇʀꜱ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ."],
        [
            "inviteall @usernamegc",
            "Tᴏ Iɴᴠɪᴛᴇ Mᴇᴍʙᴇʀꜱ ғʀᴏᴍ ᴀɴᴏᴛʜᴇʀ ɢʀᴏᴜᴘ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴄʜᴀᴛ,,(NOTES Fᴏʀ ID 𝟼/𝟻, ᴅᴏɴ'ᴛ ᴛʀʏ ᴛʜɪꜱ ғᴇᴀᴛᴜʀᴇ ᴏʀ ʏᴏᴜ'ʟʟ ᴄʀʏ).",
        ],
    ],
      )
