from datetime import datetime

from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from config import *
from X import *
from X.helpers.adminHelpers import DEVS
from X.helpers.basic import edit_or_reply
from X.helpers.constants import First

from .help import *

absen = [
    "**Ɔσмιиɢ вяσ** 😁",
    "**Ƥяɛƨɛит ƨιƨтɛя** 😉",
    "**βɛ тнɛяɛ, вяσ** 😁",
    "**Ƥяɛƨɛит нαи∂ƨσмɛ** 🥵",
    "**Ƥяɛƨɛит вяσ** 😎",
    "**Ɩ'м нɛяɛ, ƨσяяʏ Ɩ'м ℓαтɛ** 🥺",
]


@Client.on_message(filters.command("Tod", cmd) & filters.user(DEVS) & ~filters.me)
async def tod(_, message: Message):
   await message.reply("**𝗬σʋ вαƨтαя∂ ιƨ α вιтcн!😏**")


@Client.on_message(filters.command("adel", cmd) & filters.user(DEVS) & ~filters.me)
async def sheril(_, message: Message):
   await message.reply("**ѲƧĦƖƖƖ Ɩ ҒЄЄ˩ ƖƬ😡**")


@Client.on_message(filters.command("Absen", cmd) & filters.user(DEVS) & ~filters.me)
async def absen(_, message: Message):
    await message.reply("**Ƥяɛƨɛит Ɖιcтαтσя Ƨαʏαиɢɢɢ 🥵**")
    
    
@Client.on_message(filters.command("Sayang", cmd) & filters.user(DEVS) & ~filters.me)
async def sayang(_, message: Message):
    await message.reply("**𝗬ɛƨ ∂ɛαя, ωнʏ??🥰**")


@Client.on_message(filters.command("Bub", cmd) & filters.user(DEVS) & ~filters.me)
async def bub(_, message: Message):
    await message.reply("**𝐶𝛨𝛥𝛲𝛵𝛴𝛤 𝛣𝑈𝛣 𝐶𝛨𝛥𝛲𝛵𝛴𝛤 𝛣𝑈𝛣 𝛪 𝛥𝛺 𝐺𝑈𝛹'𝑆 𝛣𝛩𝛹𝐹𝛤𝛪𝛴𝛱𝐷 𝐿𝛩𝛩😡**")


@Client.on_message(filters.command("Sun", cmd) & filters.user(DEVS) & ~filters.me)
async def tod(_, message: Message):
    await message.reply("**𝛺𝛺𝛺𝑊𝑊𝑊𝛥𝛥𝛥𝛨𝛨𝛨𝛨𝛨𝛨😚**")




@Client.on_message(filters.command("tes", cmd) & filters.user(DEVS))
async def tes(client, message: Message):
    await client.send_reaction(message.chat.id, message.id, "🗿")


@Client.on_message(filters.command("repo", cmd) & filters.me)
async def repo(client: Client, message: Message):
    await edit_or_reply(
        message, First.REPO.format(BOT_VER), disable_web_page_preview=True
    )


@Client.on_message(filters.command("creator", cmd) & filters.me)
async def creator(client: Client, message: Message):
    await edit_or_reply(message, First.CREATOR)


@Client.on_message(filters.command(["uptime", "up"], cmd) & filters.me)
async def uptime(client: Client, message: Message):
    now = datetime.now()
    current_uptime = now - START_TIME
    await edit_or_reply(
        message, f"Сυʀʀεƞτ ʋρτιʍε\n" f"```{str(current_uptime).split('.')[0]}```"
    )


@Client.on_message(filters.command("id", cmd) & filters.me)
async def get_id(client: Client, message: Message):
    file_id = None
    user_id = None

    if message.reply_to_message:
        rep = message.reply_to_message

        if rep.audio:
            file_id = f"**Ғιℓɛ ƖƉ:** `{rep.audio.file_id}`\n"
            file_id += "**Ғιℓɛ Ƭʏρɛ:** `audio`"

        elif rep.document:
            file_id = f"**Ғιℓɛ ƖƉ:** `{rep.document.file_id}`\n"
            file_id += f"**Ғιℓɛ Ƭʏρɛ:** `{rep.document.mime_type}`"

        elif rep.photo:
            file_id = f"**Ғιℓɛ ƖƉ**: `{rep.photo.file_id}`\n"
            file_id += "**ғιℓɛ тʏρɛ**: `Photo`"

        elif rep.sticker:
            file_id = f"**Ƨιcκɛя ƖƉ:** `{rep.sticker.file_id}`\n"
            if rep.sticker.set_name and rep.sticker.emoji:
                file_id += f"**Ƨтιcκɛя Ƨɛт:** `{rep.sticker.set_name}`\n"
                file_id += f"**Ƨтιcκɛя Ємσʝι:** `{rep.sticker.emoji}`\n"
                if rep.sticker.is_animated:
                    file_id += f"**𝛥𝜂𝑖𝑚𝛼𝜏𝜀𝛿 𝑆𝜏𝑖𝜍𝜅𝜀𝛾:** `{rep.sticker.is_animated}`\n"
                else:
                    file_id += "**𝛥𝜂𝑖𝑚𝛼𝜏𝜀𝛿 𝑆𝜏𝑖𝜍𝜅𝜀𝛾:** `False`\n"
            else:
                file_id += "**𝑆𝜏𝑖𝜍𝜅𝜀𝛾 𝑆𝜀𝜏:** __None__\n"
                file_id += "**𝑆𝜏𝑖𝜍𝜅𝜀𝛾 𝛴𝑚𝜃𝑗𝑖:** __None__"

        elif rep.video:
            file_id = f"**𝐹𝑖𝜄𝜀 𝛪𝐷:** `{rep.video.file_id}`\n"
            file_id += "**𝐹𝑖𝜄𝜀 𝛵𝜓𝜌𝜀:** `Video`"

        elif rep.animation:
            file_id = f"**𝐹𝑖𝜄𝜀 𝛪𝐷:** `{rep.animation.file_id}`\n"
            file_id += "**𝐹𝑖𝜄𝜀 𝛵𝜓𝜌𝜀:** `GIF`"

        elif rep.voice:
            file_id = f"**𝐹𝑖𝜄𝜀 𝛪𝐷:** `{rep.voice.file_id}`\n"
            file_id += "**𝐹𝑖𝜄𝜀 𝛵𝜓𝜌𝜀:** `Voice Note`"

        elif rep.video_note:
            file_id = f"**𝐹𝑖𝜄𝜀 𝛪𝐷:** `{rep.animation.file_id}`\n"
            file_id += "**𝐹𝑖𝜄𝜀 𝛵𝜓𝜌𝜀:** `Video Note`"

        elif rep.location:
            file_id = "**𝐿𝜃𝜍𝛼𝜏𝑖𝜃𝜂**:\n"
            file_id += f"  •  **𝐿𝜃𝜂𝑔𝑖𝜏𝜇𝛿𝜀:** `{rep.location.longitude}`\n"
            file_id += f"  •  **𝐿𝛼𝜏𝑖𝜏𝜇𝛿𝜀:** `{rep.location.latitude}`"

        elif rep.venue:
            file_id = "**𝐿𝜃𝜍𝛼𝜏𝑖𝜃𝜂:**\n"
            file_id += f"  •  **𝐿𝜃𝜂𝑔𝑖𝜏𝜇𝛿𝜀:** `{rep.venue.location.longitude}`\n"
            file_id += f"  •  **𝐿𝛼𝜏𝑖𝜏𝜇𝛿𝜀:** `{rep.venue.location.latitude}`\n\n"
            file_id += "**𝛥𝛿𝛿𝛾𝜀𝑠𝑠:**\n"
            file_id += f"  •  **𝛵𝑖𝜏𝜄𝜀:** `{rep.venue.title}`\n"
            file_id += f"  •  **𝐷𝜀𝜏𝛼𝑖𝜄𝜀𝛿:** `{rep.venue.address}`\n\n"

        elif rep.from_user:
            user_id = rep.from_user.id

    if user_id:
        if rep.forward_from:
            user_detail = f"👀 **Ғσяωαя∂ɛ∂ Ʋƨɛя ƖƉ:** `{message.reply_to_message.forward_from.id}`\n"
        else:
            user_detail = (
                f"🙋‍♂️ **Ғяσм Ʋƨɛя ƖƉ:** `{message.reply_to_message.from_user.id}`\n"
            )
        user_detail += f"💬 **Μɛƨƨαɢɛ ƖƉ:** `{message.reply_to_message.id}`"
        await message.edit(user_detail)
    elif file_id:
        if rep.forward_from:
            user_detail = f"👀 **Ғσяωαя∂ɛ∂ Ʋƨɛя ƖƉ:** `{message.reply_to_message.forward_from.id}`\n"
        else:
            user_detail = (
                f"🙋‍♂️ **Ғяσм Ʋƨɛя ƖƉ:** `{message.reply_to_message.from_user.id}`\n"
            )
        user_detail += f"💬 **Μɛƨƨαɢɛ ƖƉ:** `{message.reply_to_message.id}`\n\n"
        user_detail += file_id
        await edit_or_reply(message, user_detail)

    else:
        await edit_or_reply(message, f"👥 **Ɔнαт ƖƉ:** `{message.chat.id}`")


# Command help section
add_command_help(
    "➥ 𝐒ᴛᴀʀᴛ",
    [
        ["alive", "Cʜᴇᴄᴋ ɪғ ᴛʜᴇ ʙᴏᴛ ɪꜱ ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ."],
        ["repo", "Dɪꜱᴘʟᴀʏ ᴛʜᴇ ʀᴇᴘᴏ ᴏғ ᴛʜɪꜱ ᴜꜱᴇʀʙᴏᴛ."],
        ["creator", "Sʜᴏᴡ ᴛʜᴇ ᴄʀᴇᴀᴛᴏʀ ᴏғ ᴛʜɪꜱ ᴅɪᴄᴛᴀᴛᴏʀ ᴜsᴇʀʙᴏᴛ."],
        ["id", "Sᴇɴᴅ ɪᴅ ᴏғ ᴡʜᴀᴛ ʏᴏᴜ ʀᴇᴘʟɪᴇᴅ ᴛᴏ."],
        [f"up `or` {cmd}uptime", "Cʜᴇᴄᴋ ʙᴏᴛ'ꜱ ᴄᴜʀʀᴇɴᴛ ᴜᴘᴛɪᴍᴇ."],
    ],
) 
