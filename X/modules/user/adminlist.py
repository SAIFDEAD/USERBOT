import html

from pyrogram import Client, enums, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from X.helpers.basic import edit_or_reply
from X.helpers.parser import mention_html, mention_markdown
from .help import *


@Client.on_message(filters.me & filters.command(["admins", "adminlist"], cmd))
async def adminlist(client: Client, message: Message):
    replyid = None
    toolong = False
    if len(message.text.split()) >= 2:
        chat = message.text.split(None, 1)[1]
        grup = await client.get_chat(chat)
    else:
        chat = message.chat.id
        grup = await client.get_chat(chat)
    if message.reply_to_message:
        replyid = message.reply_to_message.id
    creator = []
    admin = []
    badmin = []
    async for a in client.get_chat_members(
        message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS
    ):
        try:
            name = a.user.first_name + " " + a.user.last_name
        except:
            name = a.user.first_name
        if nama is None:
            name = "☠️ 𝐃𝐞𝐥𝐞𝐭𝐞𝐝 𝐚𝐜𝐜𝐨𝐮𝐧𝐭"
        if a.status == enums.ChatMemberStatus.ADMINISTRATOR:
            if a.user.is_bot:
                badmin.append(mention_markdown(a.user.id, name))
            else:
                admin.append(mention_markdown(a.user.id, name))
        elif a.status == enums.ChatMemberStatus.OWNER:
            creator.append(mention_markdown(a.user.id, name))
    admin.sort()
    badmin.sort()
    totaladmins = len(creator) + len(admin) + len(badmin)
    teks = "**Admins in {}**\n".format(grup.title)
    teks += "╒═══「 𝐂𝐫𝐞𝐚𝐭𝐨𝐫 」\n"
    for x in creator:
        teks += "│ • {}\n".format(x)
        if len(teks) >= 4096:
            await message.reply(message.chat.id, teks, reply_to_message_id=replyid)
            teks = ""
            toolong = True
    teks += "╞══「 {} 𝐇𝐮𝐦𝐚𝐧 𝐀𝐝𝐦𝐢𝐧𝐢𝐬𝐭𝐫𝐚𝐭𝐨𝐫 」\n".format(len(admin))
    for x in admin:
        teks += "│ • {}\n".format(x)
        if len(teks) >= 4096:
            await message.reply(message.chat.id, teks, reply_to_message_id=replyid)
            teks = ""
            toolong = True
    teks += "╞══「 {} 𝐁𝐨𝐭 𝐀𝐝𝐦𝐢𝐧𝐢𝐬𝐭𝐫𝐚𝐭𝐨𝐫 」\n".format(len(badmin))
    for x in badmin:
        teks += "│ • {}\n".format(x)
        if len(teks) >= 4096:
            await message.reply(message.chat.id, teks, reply_to_message_id=replyid)
            teks = ""
            toolong = True
    teks += "╘══「 𝐓𝐨𝐭𝐚𝐥 {} 𝐀𝐝𝐦𝐢𝐧𝐬 」".format(totaladmins)
    if toolong:
        await message.reply(message.chat.id, teks, reply_to_message_id=replyid)
    else:
        await message.edit(teks)


@Client.on_message(filters.command(["kickdel", "zombies"], cmd) & filters.me)
async def kickdel_cmd(client: Client, message: Message):
    Man = await edit_or_reply(message, "<b>𝐊𝐢𝐜𝐤𝐢𝐧𝐠 𝐝𝐞𝐥𝐞𝐭𝐞𝐝 𝐚𝐜𝐜𝐨𝐮𝐧𝐭𝐬...</b>")
    # noinspection PyTypeChecker
    values = [
        await message.chat.ban_member(user.user.id, int(time()) + 31)
        for member in await message.chat.get_members()
        if member.user.is_deleted
    ]
    await Man.edit(f"<b>𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐤𝐢𝐜𝐤𝐞𝐝 {len(values)} 𝐝𝐞𝐥𝐞𝐭𝐞𝐝 𝐚𝐜𝐜𝐨𝐮𝐧𝐭(s)</b>")


@Client.on_message(
    filters.me & filters.command(["reportadmin", "reportadmins", "report"], cmd)
)
async def report_admin(client: Client, message: Message):
    await message.delete()
    if len(message.text.split()) >= 2:
        text = message.text.split(None, 1)[1]
    else:
        text = None
    grup = await client.get_chat(message.chat.id)
    admin = []
    async for a in client.get_chat_members(
        message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS
    ):
        if (
            a.status == enums.ChatMemberStatus.ADMINISTRATOR
            or a.status == enums.ChatMemberStatus.OWNER
        ):
            if not a.user.is_bot:
                admin.append(mention_html(a.user.id, "\u200b"))
    if message.reply_to_message:
        if text:
            teks = "{}".format(text)
        else:
            teks = "{} reported to admins.".format(
                mention_html(
                    message.reply_to_message.from_user.id,
                    message.reply_to_message.from_user.first_name,
                )
            )
    else:
        if text:
            teks = "{}".format(html.escape(text))
        else:
            teks = "𝐂𝐚𝐥𝐥𝐢𝐧𝐠 𝐚𝐝𝐦𝐢𝐧𝐬 𝐢𝐧 {}.".format(grup.title)
    teks += "".join(admin)
    if message.reply_to_message:
        await client.send_message(
            message.chat.id,
            teks,
            reply_to_message_id=message.reply_to_message.id,
            parse_mode=enums.ParseMode.HTML,
        )
    else:
        await client.send_message(
            message.chat.id, teks, parse_mode=enums.ParseMode.HTML
        )


@Client.on_message(filters.me & filters.command(["everyone", "tagall"], cmd))
async def tag_all_users(client: Client, message: Message):
    await message.delete()
    if len(message.text.split()) >= 2:
        text = message.text.split(None, 1)[1]
    else:
        text = "𝐇𝐢 𝐚𝐥𝐥 😊"
    kek = client.get_chat_members(message.chat.id)
    async for a in kek:
        if not a.user.is_bot:
            text += mention_html(a.user.id, "\u200b")
    if message.reply_to_message:
        await client.send_message(
            message.chat.id,
            text,
            reply_to_message_id=message.reply_to_message.id,
            parse_mode=enums.ParseMode.HTML,
        )
    else:
        await client.send_message(
            message.chat.id, text, parse_mode=enums.ParseMode.HTML
        )


@Client.on_message(filters.me & filters.command(["botlist", "bots"], cmd))
async def get_list_bots(client: Client, message: Message):
    replyid = None
    if len(message.text.split()) >= 2:
        chat = message.text.split(None, 1)[1]
        grup = await client.get_chat(chat)
    else:
        chat = message.chat.id
        grup = await client.get_chat(chat)
    if message.reply_to_message:
        replyid = message.reply_to_message.id
    getbots = client.get_chat_members(chat)
    bots = []
    async for a in getbots:
        try:
            name = a.user.first_name + " " + a.user.last_name
        except:
            name = a.user.first_name
        if name is None:
            name = "☠️ 𝐃𝐞𝐥𝐞𝐭𝐞𝐝 𝐚𝐜𝐜𝐨𝐮𝐧𝐭"
        if a.user.is_bot:
            bots.append(mention_markdown(a.user.id, nama))
    teks = "**𝐀𝐥𝐥 𝐛𝐨𝐭𝐬 𝐢𝐧 𝐠𝐫𝐨𝐮𝐩 {}**\n".format(grup.title)
    teks += "╒═══「 𝐁𝐨𝐭𝐬 」\n"
    for x in bots:
        teks += "│ • {}\n".format(x)
    teks += "╘══「 𝐓𝐨𝐭𝐚𝐥 {} 𝐁𝐨𝐭𝐬 」".format(len(bots))
    if replyid:
        await client.send_message(message.chat.id, teks, reply_to_message_id=replyid)
    else:
        await message.edit(teks)


add_command_help(
    "tag",
    [
        [f"{cmd}admins", "𝐆𝐞𝐭 𝐜𝐡𝐚𝐭𝐬 𝐀𝐝𝐦𝐢𝐧𝐬 𝐥𝐢𝐬𝐭."],
        [f"{cmd}kickdel", "𝐓𝐨 𝐊𝐢𝐜𝐤 𝐝𝐞𝐥𝐞𝐭𝐞𝐝 𝐀𝐜𝐜𝐨𝐮𝐧𝐭𝐬."],
        [
            f"{cmd}everyone `or` {cmd}tagall",
            "𝐭𝐨 𝐦𝐞𝐧𝐭𝐢𝐨𝐧 𝐄𝐯𝐞𝐫𝐲𝐨𝐧𝐞 ",
        ],
        [
            f"{cmd}botlist",
            "𝐓𝐨 𝐠𝐞𝐭 𝐂𝐡𝐚𝐭𝐬 𝐁𝐨𝐭𝐬 𝐥𝐢𝐬𝐭",
        ],
    ],
) 
