from asyncio import gather
from os import remove

from pyrogram import Client, filters
from pyrogram.enums import ChatType
from pyrogram.types import Message

from config import CMD_HANDLER
from X.helpers.basic import edit_or_reply
from X.helpers.PyroHelpers import ReplyCheck
from X.utils import extract_user

from .help import *


@Client.on_message(filters.command(["whois", "info"], cmd) & filters.me)
async def who_is(client: Client, message: Message):
    user_id = await extract_user(message)
    X = await edit_or_reply(message, "`Processing . . .`")
    if not user_id:
        return await X.edit(
            "**Give userid/username/reply to get that user's info.**"
        )
    try:
        user = await client.get_users(user_id)
        username = f"@{user.username}" if user.username else "-"
        first_name = f"{user.first_name}" if user.first_name else "-"
        last_name = f"{user.last_name}" if user.last_name else "-"
        fullname = (
            f"{user.first_name} {user.last_name}" if user.last_name else user.first_name
        )
        user_details = (await client.get_chat(user.id)).bio
        bio = f"{user_details}" if user_details else "-"
        h = f"{user.status}"
        if h.startswith("UserStatus"):
            y = h.replace("UserStatus.", "")
            status = y.capitalize()
        else:
            status = "-"
        dc_id = f"{user.dc_id}" if user.dc_id else "-"
        common = await client.get_common_chats(user.id)
        out_str = f"""<b>USER INFORMATION:</b>

🆔 <b>User ID:</b> <code>{user.id}</code>
👤 <b>First Name:</b> {first_name}
🗣️ <b>Last Name:</b> {last_name}
🌐 <b>Username:</b> {username}
🏛️ <b>DC ID:</b> <code>{dc_id}</code>
🤖 <b>Is Bot:</b> <code>{user.is_bot}</code>
🚷 <b>Is Scam:</b> <code>{user.is_scam}</code>
🚫 <b>Restricted:</b> <code>{user.is_restricted}</code>
✅ <b>Verified:</b> <code>{user.is_verified}</code>
⭐ <b>Premium:</b> <code>{user.is_premium}</code>
📝 <b>User Bio:</b> {bio}

👀 <b>Same groups seen:</b> {len(common)}
👁️ <b>Last Seen:</b> <code>{status}</code>
🔗 <b>User permanent link:</b> <a href='tg://user?id={user.id}'>{fullname}</a>
"""
        photo_id = user.photo.big_file_id if user.photo else None
        if photo_id:
            photo = await client.download_media(photo_id)
            await gather(
                X.delete(),
                client.send_photo(
                    message.chat.id,
                    photo,
                    caption=out_str,
                    reply_to_message_id=ReplyCheck(message),
                ),
            )
            remove(photo)
        else:
            await X.edit(out_str, disable_web_page_preview=True)
    except Exception as e:
        return await X.edit(f"**INFO:** `{e}`")


@Client.on_message(filters.command(["chatinfo", "cinfo", "ginfo"], cmd) & filters.me)
async def chatinfo_handler(client: Client, message: Message):
    X = await edit_or_reply(message, "`Processing...`")
    try:
        if len(message.command) > 1:
            chat_u = message.command[1]
            chat = await client.get_chat(chat_u)
        else:
            if message.chat.type == ChatType.PRIVATE:
                return await message.edit(
                    f"Use this command in a group or use `{cmd}chatinfo [group username or id]`"
                )
            else:
                chatid = message.chat.id
                chat = await client.get_chat(chatid)
        h = f"{chat.type}"
        if h.startswith("ChatType"):
            y = h.replace("ChatType.", "")
            type = y.capitalize()
        else:
            type = "Private"
        username = f"@{chat.username}" if chat.username else "-"
        description = f"{chat.description}" if chat.description else "-"
        dc_id = f"{chat.dc_id}" if chat.dc_id else "-"
        out_str = f"""<b>CHAT INFORMATION:</b>

🆔 <b>Cʜᴀᴛ ID:</b> <code>{chat.id}</code>
👥 <b>Tɪᴛʟᴇ:</b> {chat.title}
👥 <b>Uꜱᴇʀɴᴀᴍᴇ:</b> {username}
📩 <b>Tʏᴘᴇ:</b> <code>{type}</code>
🏛️ <b>DC ID:</b> <code>{dc_id}</code>
🗣️ <b>Iꜱ Sᴄᴀᴍ:</b> <code>{chat.is_scam}</code>
🎭 <b>Iꜱ Fᴀᴋᴇ:</b> <code>{chat.is_fake}</code>
✅ <b>Vᴇʀɪғɪᴇᴅ:</b> <code>{chat.is_verified}</code>
🚫 <b>Rᴇꜱᴛʀɪᴄᴛᴇᴅ:</b> <code>{chat.is_restricted}</code>
🔰 <b>Pʀᴏᴛᴇᴄᴛᴇᴅ:</b> <code>{chat.has_protected_content}</code>

🚻 <b>Tᴏᴛᴀʟ ᴍᴇᴍʙᴇʀꜱ:</b> <code>{chat.members_count}</code>
📝 <b>Dᴇꜱᴄʀɪᴘᴛɪᴏɴ:</b>
<code>{description}</code>
"""
        photo_id = chat.photo.big_file_id if chat.photo else None
        if photo_id:
            photo = await client.download_media(photo_id)
            await gather(
                X.delete(),
                client.send_photo(
                    message.chat.id,
                    photo,
                    caption=out_str,
                    reply_to_message_id=ReplyCheck(message),
                ),
            )
            remove(photo)
        else:
            await X.edit(out_str, disable_web_page_preview=True)
    except Exception as e:
        return await X.edit(f"**INFO:** `{e}`")


add_command_help(
    "•─╼⃝𖠁 ɪɴғᴏ",
    [
        [
            "info <ᴜꜱᴇʀɴᴀᴍᴇ/ᴜꜱᴇʀɪᴅ/ʀᴇᴘʟʏ>",
            "ɢᴇᴛ ᴛᴇʟᴇɢʀᴀᴍ ᴜꜱᴇʀ ɪɴғᴏ ᴡɪᴛʜ ᴄᴏᴍᴘʟᴇᴛᴇ ᴅᴇꜱᴄʀɪᴘᴛɪᴏɴ.",
        ],
        [
            "chatinfo <ᴜꜱᴇʀɴᴀᴍᴇ/ᴄʜᴀᴛɪᴅ/ʀᴇᴘʟʏ>",
            "ɢᴇᴛ ɢʀᴏᴜᴘ ɪɴғᴏ ᴡɪᴛʜ ᴄᴏᴍᴘʟᴇᴛᴇ ᴅᴇꜱᴄʀɪᴘᴛɪᴏɴ.",
        ],
    ],
                  )
