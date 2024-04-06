import os
from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from X.helpers.basic import edit_or_reply
from X.helpers.PyroHelpers import ReplyCheck
from X.utils.misc import extract_user

from .help import *

flood = {}
profile_photo = "X/modules/cache/pfp.jpg"


@Client.on_message(filters.command(["block"], cmd) & filters.me)
async def block_user_func(client: Client, message: Message):
    user_id = await extract_user(message)
    X = await edit_or_reply(message, "`Be patient, block again . . .`")
    if not user_id:
        return await message.edit(
            "Provide User ID/Username or reply to user message to unblock."
        )
    if user_id == client.me.id:
        return await X.edit("ANY FOOL CAN BLOCK YOURSELF.")
    await client.block_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await message.edit(f"**managed to Block This Dick Kid** {umention}")


@Client.on_message(filters.command(["unblock"], cmd) & filters.me)
async def unblock_user_func(client: Client, message: Message):
    user_id = await extract_user(message)
    X = await edit_or_reply(message, "`Be patient and unblock stupid people . . .`")
    if not user_id:
        return await message.edit(
            "Provide User ID/Username or reply to user message to unblock."
        )
    if user_id == client.me.id:
        return await X.edit("If you are stressed, please take medicine immediately.")
    await client.unblock_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await message.edit(f"**sᴜᴄᴄᴇssғᴜʟʟʏ ᴜɴʙʟᴏᴄᴋᴇᴅ ᴛʜɪs ᴅɪᴄᴋ ʙᴏʏ ✌** {umention}")


@Client.on_message(filters.command(["setname"], cmd) & filters.me)
async def setname(client: Client, message: Message):
    X = await edit_or_reply(message, "`ʙᴇ ᴘᴀᴛɪᴇɴᴛ ᴄʜᴀɴɢᴇ ɴᴀᴍᴇ. . .`")
    if len(message.command) == 1:
        return await X.edit(
            "ᴘʀᴏᴠɪᴅᴇ ᴛᴇxᴛ ᴛᴏ sᴇᴛ ᴀs ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ɴᴀᴍᴇ."
        )
    elif len(message.command) > 1:
        name = message.text.split(None, 1)[1]
        try:
            await client.update_profile(first_name=name)
            await X.edit(f"**sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ɴᴀᴍᴇ ᴛᴏ** `{name}`")
        except Exception as e:
            await X.edit(f"**ᴇʀʀᴏʀ:** `{e}`")
    else:
        return await X.edit(
            "ᴘʀᴏᴠɪᴅᴇ ᴛᴇxᴛ ᴛᴏ sᴇᴛ ᴀs ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ɴᴀᴍᴇ."
        )


@Client.on_message(filters.command(["setbio"], cmd) & filters.me)
async def set_bio(client: Client, message: Message):
    X = await edit_or_reply(message, "`ᴘʀᴏᴄᴇssɪɴɢ . . .`")
    if len(message.command) == 1:
        return await X.edit("ᴘʀᴏᴠɪᴅᴇ ᴛᴇxᴛ ᴛᴏ sᴇᴛ ᴀs ʙɪᴏ.")
    elif len(message.command) > 1:
        bio = message.text.split(None, 1)[1]
        try:
            await client.update_profile(bio=bio)
            await X.edit(f"**sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ ʏᴏᴜʀ ʙɪᴏ ᴛᴏ** `{bio}`")
        except Exception as e:
            await X.edit(f"**ᴇʀʀᴏʀ:** `{e}`")
    else:
        return await X.edit("ᴘʀᴏᴠɪᴅᴇ ᴛᴇxᴛ ᴛᴏ sᴇᴛ ᴀs ʙɪᴏ.")


@Client.on_message(filters.me & filters.command(["setpfp"], cmd))
async def set_pfp(client: Client, message: Message):
    replied = message.reply_to_message
    if (
        replied
        and replied.media
        and (
            replied.photo
            or (replied.document and "image" in replied.document.mime_type)
        )
    ):
        await client.download_media(message=replied, file_name=profile_photo)
        await client.set_profile_photo(profile_photo)
        if os.path.exists(profile_photo):
            os.remove(profile_photo)
        await message.edit("**ʏᴏᴜʀ ᴘʀᴏғɪʟᴇ ᴘʜᴏᴛᴏ ʜᴀs ʙᴇᴇɴ sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ.**")
    else:
        await message.edit(
            "`ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴘʜᴏᴛᴏ ᴛᴏ sᴇᴛ ᴀs ᴀ ᴘʀᴏғɪʟᴇ ᴘʜᴏᴛᴏ`"
        )
        await sleep(3)
        await message.delete()


@Client.on_message(filters.me & filters.command(["vpfp"], cmd))
async def view_pfp(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id:
        user = await client.get_users(user_id)
    else:
        user = await client.get_me()
    if not user.photo:
        await message.edit("ᴘʀᴏғɪʟᴇ ᴘʜᴏᴛᴏ ɴᴏᴛ ғᴏᴜɴᴅ !")
        return
    await client.download_media(user.photo.big_file_id, file_name=profile_photo)
    await client.send_photo(
        message.chat.id, profile_photo, reply_to_message_id=ReplyCheck(message)
    )
    await message.delete()
    if os.path.exists(profile_photo):
        os.remove(profile_photo)


add_command_help(
    "➥ 𝐏ʀᴏғɪʟᴇ",
    [
        ["block", "Tᴏ ʙʟᴏᴄᴋ ᴛᴇʟᴇɢʀᴀᴍ ᴜꜱᴇʀꜱ"],
        ["unblock", "Tᴏ ᴜɴʙʟᴏᴄᴋ ᴛᴇʟᴇɢʀᴀᴍ ᴜꜱᴇʀꜱ"],
        ["setname", "Tᴏ Cʜᴀɴɢᴇ Tᴇʟᴇɢʀᴀᴍ Nᴀᴍᴇ."],
        ["setbio", "Tᴏ Cʜᴀɴɢᴇ Tᴇʟᴇɢʀᴀᴍ Bɪᴏ."],
        [
            "setpfp",
            "Rᴇᴘʟʏ Tᴏ Iᴍᴀɢᴇ Tʏᴘᴇ {cmd}ꜱᴇᴛᴘғᴘ Tᴏ Cʜᴀɴɢᴇ Tᴇʟᴇɢʀᴀᴍ Pʀᴏғɪʟᴇ Pʜᴏᴛᴏ.",
        ],
        ["vpfp", "Tᴏ ꜱᴇᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴜꜱᴇʀ'ꜱ ᴘʀᴏғɪʟᴇ ᴘʜᴏᴛᴏ."],
    ],
  ) 
