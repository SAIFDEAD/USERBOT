from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from X.helpers.basic import edit_or_reply
from X.utils.sections import section

from .help import *


@Client.on_message(filters.command("parse", cmd) & filters.me)
async def parse(client: Client, message: Message):
    r = message.reply_to_message
    has_wpp = False
    if not r:
        return await edit_or_reply(message, "ʀᴇᴘʟʏ ᴛᴏ a ᴍᴇssᴀɢᴇ ᴡɪᴛʜ ᴀ ᴡᴇʙᴘᴀɢᴇ")
    m_ = await edit_or_reply(message, "`ᴘᴀʀsɪɴɢ...`")
    if not r.web_page:
        text = r.text or r.caption
        if text:
            m = await client.send_message("me", text)
            await sleep(1)
            await m.delete()
            if m.web_page:
                r = m
                has_wpp = True
    else:
        has_wpp = True
    if not has_wpp:
        return await m_.edit(
            "ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ ʜᴀs ɴᴏ ᴡᴇʙᴘᴀɢᴇ ᴘʀᴇᴠɪᴇᴡ.",
        )
    wpp = r.web_page
    body = {
        "𝐓ɪᴛʟᴇ": [wpp.title or "Null"],
        "𝐃ᴇsᴄʀɪᴘᴛɪᴏɴ": [(wpp.description[:50] + "...") if wpp.description else "Null"],
        "𝐔ʀʟ": [wpp.display_url or "Null"],
        "𝐀ᴜᴛʜᴏʀ": [wpp.author or "Null"],
        "𝐒ɪᴛᴇ 𝐍ᴀᴍᴇ": [wpp.site_name or "Null"],
        "𝐓ʏᴘᴇ": wpp.type or "Null",
    }
    text = section("Preview", body)
    t = wpp.type
    if t == "Photo":
        media = wpp.photo
        func = client.send_photo
    elif t == "Audio":
        media = wpp.audio
        func = client.send_audio
    elif t == "Video":
        media = wpp.video
        func = client.send_video
    elif t == "Document":
        media = wpp.document
        func = client.send_document
    else:
        media = None
        func = None
    if media and func:
        await m_.delete()
        return await func(
            m_.chat.id,
            media.file_id,
            caption=text,
        )
    await m_.edit(text, disable_web_page_preview=True)


add_command_help(
    "➥ 𝐏ᴀʀꜱᴇ",
    [
        [
            "parse",
            "Pᴀʀꜱᴇ ᴀ ᴡᴇʙ_ᴘᴀɢᴇ(ʟɪɴᴋ) ᴘʀᴇᴠɪᴇᴡ",
        ]
    ],
  ) 
