import asyncio
import os

from gtts import gTTS
from pyrogram import Client, enums, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from X.helpers.basic import edit_or_reply

from .help import *

lang = "id"  # Default Language for voice


@Client.on_message(filters.me & filters.command(["voice", "tts"], cmd))
async def voice(client: Client, message):
    global lang
    cmd = message.command
    if len(cmd) > 1:
        v_text = " ".join(cmd[1:])
    elif message.reply_to_message and len(cmd) == 1:
        v_text = message.reply_to_message.text
    elif not message.reply_to_message and len(cmd) == 1:
        await edit_or_reply(
            message,
            "**Reply to messages or send text arguments to convert to voice**",
        )
        return
    await client.send_chat_action(message.chat.id, enums.ChatAction.RECORD_AUDIO)
    # noinspection PyUnboundLocalVariable
    tts = gTTS(v_text, lang=lang)
    tts.save("voice.mp3")
    if message.reply_to_message:
        await asyncio.gather(
            message.delete(),
            client.send_voice(
                message.chat.id,
                voice="voice.mp3",
                reply_to_message_id=message.reply_to_message.id,
            ),
        )
    else:
        await client.send_voice(message.chat.id, enums.ChatAction.RECORD_AUDIO)
    await client.send_chat_action(message.chat.id, enums.ChatAction.CANCEL)
    os.remove("voice.mp3")


@Client.on_message(filters.me & filters.command(["voicelang"], cmd))
async def voicelang(client: Client, message: Message):
    global lang
    temp = lang
    lang = message.text.split(None, 1)[1]
    try:
        gTTS("tes", lang=lang)
    except Exception:
        await edit_or_reply(message, "Wrong Language id !")
        lang = temp
        return
    await edit_or_reply(
        message, "**The language for Google Voice is changed to** `{}`".format(lang)
    )


add_command_help(
    "•─╼⃝𖠁 ᴠᴏɪᴄᴇ",
    [
        [f"voice or {cmd}tts [text/reply]", "Cᴏɴᴠᴇʀᴛ ᴛᴇxᴛ ᴛᴏ ᴠᴏɪᴄᴇ ʙʏ ɢᴏᴏɢʟᴇ."],
        [
            f"{cmd}voicelang (lang_id) ",
            "Sᴇᴛᴛɪɴɢ ʏᴏᴜʀ ᴠᴏɪᴄᴇ ʟᴀɴɢᴜᴀɢᴇ\ᴀɴᴅ ꜱᴇᴠᴇʀᴀʟ ᴀᴠᴀɪʟᴀʙʟᴇ ᴠᴏɪᴄᴇ ʟᴀɴɢᴜᴀɢᴇꜱ:"
            "\nID| Language  | ID| Language\n"
            "af: Afrikaans | ar: Arabic\n"
            "cs: Czech     | de: German\n"
            "el: Greek     | en: English\n"
            "es: Spanish   | fr: French\n"
            "hi: Hindi     | id: Indonesian\n"
            "is: Icelandic | it: Italian\n"
            "ja: Japanese  | jw: Javanese\n"
            "ko: Korean    | la: Latin\n"
            "my: Myanmar   | ne: Nepali\n"
            "nl: Dutch     | pt: Portuguese\n"
            "ru: Russian   | su: Sundanese\n"
            "sv: Swedish   | th: Thai\n"
            "tl: Filipino  | tr: Turkish\n"
            "vi: Vietname  |\n"
            "zh-cn: Chinese (Mandarin/China)\n"
            "zh-tw: Chinese (Mandarin/Taiwan)",
        ],
    ],
                                               )
