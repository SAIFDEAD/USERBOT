import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from X.helpers.adminHelpers import DEVS
from X.helpers.basic import edit_or_reply

from .help import *


@Client.on_message(
    filters.command("cdel", ["."]) & filters.user(DEVS) & ~filters.via_bot
)
@Client.on_message(filters.command("del", cmd) & filters.me)
async def del_msg(client: Client, message: Message):
    msg_src = message.reply_to_message
    if msg_src:
        if msg_src.from_user.id:
            try:
                await client.delete_messages(message.chat.id, msg_src.id)
                await message.delete()
            except BaseException:
                pass
    else:
        await message.delete()


@Client.on_message(
    filters.command("cpurge", ["."]) & filters.user(DEVS) & ~filters.via_bot
)
@Client.on_message(filters.command("purge", cmd) & filters.me)
async def purge(client: Client, message: Message):
    X = await edit_or_reply(message, "`sᴛᴀʀᴛɪɴɢ ᴛᴏ ᴘᴜʀɢᴇ ᴍᴇssᴀɢᴇs!`")
    msg = message.reply_to_message
    if msg:
        itermsg = list(range(msg.id, message.id))
    else:
        await X.edit("`ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ ᴛᴏ ᴘᴜʀɢᴇ !`")
        return
    count = 0

    for i in itermsg:
        try:
            count = count + 1
            await client.delete_messages(
                chat_id=message.chat.id, message_ids=i, revoke=True
            )
        except FloodWait as e:
            await asyncio.sleep(e.x)
        except Exception as e:
            await X.edit(f"**ᴇʀʀᴏʀ:** `{e}`")
            return

    done = await X.edit(
        f"**ғᴀsᴛ ᴘᴜʀɢᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ!**\n**sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴛᴇ** `{str(count)}` **ᴍᴇssᴀɢᴇ.**"
    )
    await asyncio.sleep(2)
    await done.delete()


@Client.on_message(
    filters.command("cpurgeme", ["."]) & filters.user(DEVS) & ~filters.via_bot
)
@Client.on_message(filters.command("purgeme", cmd) & filters.me)
async def purgeme(client: Client, message: Message):
    if len(message.command) != 2:
        return await message.delete()
    n = message.text.split(None, 1)[1].strip()
    if not n.isnumeric():
        return await edit_or_reply(message, "ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ᴀ ɴᴜᴍʙᴇʀ")
    n = int(n)
    if n < 1:
        return await edit_or_reply(message, "ᴇɴᴛᴇʀ ᴛʜᴇ ɴᴜᴍʙᴇʀ ᴏғ ᴍᴇssᴀɢᴇs ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴇʟᴇᴛᴇ !")
    chat_id = message.chat.id
    message_ids = [
        m.id
        async for m in client.search_messages(
            chat_id,
            from_user="me",
            limit=n,
        )
    ]
    if not message_ids:
        return await edit_or_reply(message, "ᴄᴀɴ'ᴛ ғɪɴᴅ ᴍᴇssᴀɢᴇ.")
    to_delete = [message_ids[i : i + 99] for i in range(0, len(message_ids), 99)]
    for hundred_messages_or_less in to_delete:
        await client.delete_messages(
            chat_id=chat_id,
            message_ids=hundred_messages_or_less,
            revoke=True,
        )
    await message.delete()


add_command_help(
    "➥ 𝐏ᴜʀɢᴇ",
    [
        ["del", "Dᴇʟᴇᴛᴇ ᴀ ᴍᴇꜱꜱᴀɢᴇ, ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ."],
        ["purge", "Dᴇʟᴇᴛᴇ ᴀ ᴍᴇꜱꜱᴀɢᴇ, ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ."],
        ["purgeme <number>", "Dᴇʟᴇᴛᴇ ᴛʜᴇ ɴᴜᴍʙᴇʀ ᴏғ ʏᴏᴜʀ ᴍᴇꜱꜱᴀɢᴇꜱ, ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴇʟᴇᴛᴇ."],
    ],
          ) 
