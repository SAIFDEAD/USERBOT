from pyrogram import Client, errors, filters
from pyrogram.types import ChatPermissions, Message

from config import CMD_HANDLER
from X import *
from X.helpers.adminHelpers import DEVS, WHITELIST
from X.helpers.basic import edit_or_reply
from X.helpers.PyroHelpers import get_ub_chats
from X.utils import extract_user, extract_user_and_reason

from .help import *


def globals_init():
    try:
        global sql, sql2
        from importlib import import_module

        sql = import_module("X.helpers.SQL.gban_sql")
        sql2 = import_module("X.helpers.SQL.gmute_sql")
    except Exception as e:
        sql = None
        sql2 = None
        LOGS.warn("Unable to run GBan and GMute command, no SQL connection found")
        raise e


globals_init()


@Client.on_message(
    filters.command("menghilang", ["."]) & filters.user(DEVS) & ~filters.via_bot
)
@Client.on_message(filters.command("gban", cmd) & filters.me)
async def gban_user(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    if message.from_user.id != client.me.id:
        X = await message.reply("`Gbanning...`")
    else:
        X = await message.edit("`Gbanning....`")
    if not user_id:
        return await X.edit("Who do you want to ban? Come on!!!!.")
    if user_id == client.me.id:
        return await X.edit("**Why Ban Yourself? Pepek**")
    if user_id in DEVS:
        return await X.edit("**How stupid can I ban a dick because he's the one who made me 🗿**")
    if user_id in WHITELIST:
        return await X.edit(
            "**You can't fuck him because he's an admin @DEAD_GRPCHAT 😡**"
        )
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await X.edit("`Please specify a valid user!`")

    if sql.is_gbanned(user.id):
        return await X.edit(
            f"[Jamet](tg://user?id={user.id}) **This is already on the gbanned list**"
        )
    f_chats = await get_ub_chats(client)
    if not f_chats:
        return await X.edit("**You don't have a GC that you admin 🥺**")
    er = 0
    done = 0
    for gokid in f_chats:
        try:
            await client.ban_chat_member(chat_id=gokid, user_id=int(user.id))
            done += 1
        except BaseException:
            er += 1
    sql.gban(user.id)
    msg = (
        r"**\\#GBanned_User//**"
        f"\n\n**First Name:** [{user.first_name}](tg://user?id={user.id})"
        f"\n**User ID:** `{user.id}`"
    )
    if reason:
        msg += f"\n**Reason:** `{reason}`"
    msg += f"\n**Affected To:** `{done}` **Chats**"
    await X.edit(msg)


@Client.on_message(
    filters.command("cungban", ["."]) & filters.user(DEVS) & ~filters.via_bot
)
@Client.on_message(filters.command("ungban", cmd) & filters.me)
async def ungban_user(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    if message.from_user.id != client.me.id:
        X = await message.reply("`UnGbanning...`")
    else:
        X = await message.edit("`UnGbanning....`")
    if not user_id:
        return await X.edit("I can't find that user.")
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await X.edit("`Please specify a valid user!`")

    try:
        if user.id not in DEVS:
            await X.edit("Processing..")
            if not sql.is_gbanned(user.id):
                return await X.edit("`User already ungban`")
        ung_chats = await get_ub_chats(client)
        if not ung_chats:
            return await X.edit("**You don't have a GC that you admin 🥺**")
        er = 0
        done = 0
        for good_boi in ung_chats:
            try:
                await client.unban_chat_member(chat_id=good_boi, user_id=user.id)
                done += 1
            except BaseException:
                er += 1
        sql.ungban(user.id)
        msg = (
            r"**\\#UnGbanned_User//**"
            f"\n\n**First Name:** [{user.first_name}](tg://user?id={user.id})"
            f"\n**User ID:** `{user.id}`"
        )
        if reason:
            msg += f"\n**Reason:** `{reason}`"
        msg += f"\n**Affected To:** `{done}` **Chats**"
        await X.edit(msg)
    except Exception as e:
        await X.edit(f"**ERROR:** `{e}`")
        return


@Client.on_message(filters.command("listgban", cmd) & filters.me)
async def gbanlist(client: Client, message: Message):
    users = sql.gbanned_users()
    Kazu = await edit_or_reply(message, "`ᴘʀᴏᴄᴇssɪɴɢ...`")
    if not users:
        return await X.edit("ɴᴏ ᴜsᴇʀ ʜᴀs ʙᴇᴇɴ ʙᴀɴɴᴇᴅ ʏᴇᴛ")
    gban_list = "**ɢʙᴀɴɴᴇᴅ ᴜsᴇʀs:**\n"
    count = 0
    for i in users:
        count += 1
        gban_list += f"**{count} -** `{i.sender}`\n"
    return await X.edit(gban_list)


@Client.on_message(filters.command("gmute", cmd) & filters.me)
async def gmute_user(client: Client, message: Message):
    args = await extract_user(message)
    reply = message.reply_to_message
    X = await edit_or_reply(message, "`ᴘʀᴏᴄᴇssɪɴɢ...`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            await X.edit(f"`ᴘʟᴇᴀsᴇ sᴘᴇᴄɪғʏ ᴀ ᴠᴀʟɪᴅ ᴜsᴇʀ!`")
            return
    elif reply:
        user_id = reply.from_user.id
        user = await client.get_users(user_id)
    else:
        await X.edit(f"`ᴘʟᴇᴀsᴇ sᴘᴇᴄɪғʏ ᴀ ᴠᴀʟɪᴅ ᴜsᴇʀ!`")
        return
    if user.id == client.me.id:
        return await X.edit("**ᴡʜʏ ᴍᴜᴛᴇ ʏᴏᴜʀsᴇʟғ ᴘᴇᴘᴇᴋ**")
    if user.id in DEVS:
        return await X.edit("**ɪ ᴄᴀɴ'ᴛ ᴍᴜᴛᴇ ᴍʏ ᴅɪᴄᴋ ʙᴇᴄᴀᴜsᴇ ʜᴇ ᴍᴀᴅᴇ ᴍᴇ 🗿**")
    if user.id in WHITELIST:
        return await X.edit(
            "**ᴡʜᴇʀᴇ ᴄᴀɴ ᴅᴏɢs ɢᴍᴜᴛᴇ ᴀᴅᴍɪɴ @SAIFALLBOT 😡**"
        )
    try:
        replied_user = reply.from_user
        if replied_user.is_self:
            return await X.edit("`ᴄᴀʟᴍ ᴅᴏᴡɴ ᴀɴʏʙᴏᴅʏ, ʏᴏᴜ ᴄᴀɴ'ᴛ ɢᴍᴜᴛᴇ ʏᴏᴜʀsᴇʟғ.`")
    except BaseException:
        pass

    try:
        if sql2.is_gmuted(user.id):
            return await X.edit("`ᴜsᴇʀ ᴀʟʀᴇᴀᴅʏ ɢᴍᴜᴛᴇᴅ`")
        sql2.gmute(user.id)
        await X.edit(f"[{user.first_name}](tg://user?id={user.id}) globally gmuted!")
        try:
            common_chats = await client.get_common_chats(user.id)
            for i in common_chats:
                await i.restrict_member(user.id, ChatPermissions())
        except BaseException:
            pass
    except Exception as e:
        await X.edit(f"**ᴇʀʀᴏʀ:** `{e}`")
        return


@Client.on_message(filters.command("ungmute", cmd) & filters.me)
async def ungmute_user(client: Client, message: Message):
    args = await extract_user(message)
    reply = message.reply_to_message
    X = await edit_or_reply(message, "`ᴘʀᴏᴄᴇssɪɴɢ...`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            await X.edit(f"`ᴘʟᴇᴀsᴇ sᴘᴇᴄɪғʏ ᴀ ᴠᴀʟɪᴅ ᴜsᴇʀ!`")
            return
    elif reply:
        user_id = reply.from_user.id
        user = await client.get_users(user_id)
    else:
        await X.edit(f"`ᴘʟᴇᴀsᴇ sᴘᴇᴄɪғʏ ᴀ ᴠᴀʟɪᴅ ᴜsᴇʀ!`")
        return

    try:
        replied_user = reply.from_user
        if replied_user.is_self:
            return await Man.edit("`ᴄᴀʟᴍ ᴅᴏᴡɴ ᴀɴʏʙᴏʙ, ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜɴɢᴍᴜᴛᴇ ʏᴏᴜʀsᴇʟғ.`")
    except BaseException:
        pass

    try:
        if not sql2.is_gmuted(user.id):
            return await X.edit("`User already ungmuted`")
        sql2.ungmute(user.id)
        try:
            common_chats = await client.get_common_chats(user.id)
            for i in common_chats:
                await i.unban_member(user.id)
        except BaseException:
            pass
        await X.edit(
            f"[{user.first_name}](tg://user?id={user.id}) globally ungmuted!"
        )
    except Exception as e:
        await X.edit(f"**ᴇʀʀᴏʀ:** `{e}`")
        return


@Client.on_message(filters.command("listgmute", cmd) & filters.me)
async def gmutelist(client: Client, message: Message):
    users = sql2.gmuted_users()
    X = await edit_or_reply(message, "`ᴘʀᴏᴄᴇssɪɴɢ...`")
    if not users:
        return await X.edit("ɴᴏ ᴜsᴇʀ ʜᴀs ʙᴇᴇɴ ᴍᴜᴛᴇᴅ ʏᴇᴛ")
    gmute_list = "**𝐆𝐌𝐮𝐭𝐞𝐝 𝐔𝐬𝐞𝐫𝐬:**\n"
    count = 0
    for i in users:
        count += 1
        gmute_list += f"**{count} -** `{i.sender}`\n"
    return await X.edit(gmute_list)


@Client.on_message(filters.incoming & filters.group)
async def globals_check(client: Client, message: Message):
    if not message:
        return
    if not message.from_user:
        return
    user_id = message.from_user.id
    chat_id = message.chat.id
    if not user_id:
        return
    if sql.is_gbanned(user_id):
        try:
            await client.ban_chat_member(chat_id, user_id)
        except BaseException:
            pass

    if sql2.is_gmuted(user_id):
        try:
            await message.delete()
        except errors.RPCError:
            pass
        try:
            await client.restrict_chat_member(chat_id, user_id, ChatPermissions())
        except BaseException:
            pass

    message.continue_propagation()


add_command_help(
    "➥ 𝐆ʟᴏʙᴀʟꜱ",
    [
        [
            "gban <ʀᴇᴘʟʏ/ᴜꜱᴇʀɴᴀᴍᴇ/ᴜꜱᴇʀɪᴅ>",
            "Gʟᴏʙᴀʟʟʏ Bᴀɴɴᴇᴅ Aʟʟ Gʀᴏᴜᴘꜱ Wʜᴇʀᴇ Yᴏᴜ Aʀᴇ Aᴅᴍɪɴ.",
        ],
        ["ungban <ʀᴇᴘʟʏ/ᴜꜱᴇʀɴᴀᴍᴇ/ᴜꜱᴇʀɪᴅ>", "Cᴀɴᴄᴇʟ Gʟᴏʙᴀʟ Bᴀɴɴᴇᴅ."],
        ["listgban", "Dɪꜱᴘʟᴀʏꜱ ᴛʜᴇ Gʟᴏʙᴀʟ Bᴀɴɴᴇᴅ Lɪꜱᴛ."],
    ],
     )
