import time
import traceback
from sys import version as pyver
from datetime import datetime
import os
import shlex
import textwrap
import asyncio

from pyrogram import Client
from pyrogram import __version__ as pyrover
from pyrogram.enums import ParseMode
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message,
)
from X.helpers.data import Data
from X.helpers.inline import inline_wrapper, paginate_help
from config import BOT_VER, BRANCH as branch
from X import CMD_HELP, StartTime, app

modules = CMD_HELP

async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "Day"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


async def alive_function(message: Message, answers):
    uptime = await get_readable_time((time.time() - StartTime))
    msg = f"""
<b> — Hi, I'm Alive.</b>

<b> • 𝙼𝚈 𝙼𝙰𝚂𝚃𝙴𝚁 :</b> {message.from_user.mention}
<b> • 𝙼𝙾𝙳𝚄𝙻𝙴𝚂 :</b> <code>{len(CMD_HELP)} Modules</code>
<b> • 𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽:</b> <code>{pyver.split()[0]}</code>
<b> • 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 :</b> <code>{pyrover}</code>
<b> • 𝙱𝙾𝚃 𝚄𝙿𝚃𝙸𝙼𝙴 :</b> <code>{uptime}</code>

<b> — 𝙱𝙾𝚃 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 : 1.0</b>
"""
    answers.append(
        InlineQueryResultArticle(
            title="alipp",
            description="Check Bot's Stats",
            thumb_url="https://graph.org/file/83978974fe5be2da118d7.jpg",
            input_message_content=InputTextMessageContent(
                msg, parse_mode=ParseMode.HTML, disable_web_page_preview=True
            ),
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("──「 ʜᴇʟᴘ 」──", callback_data="helper")]]
            ),
        )
    )
    return answers


async def pingme(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await message.reply_text(
        f"❏ **PONG!!🏓**\n"
        f"├• **Pinger** - `%sms`\n"
        f"├• **Uptime -** `{uptime}` \n"
        f"└• **Owner :** {client.me.mention}" % (duration)
    )

async def peler_function(message: Message, answers):
    msg = (
        f"Japanese-X-Userbot \n"
        "ㅤㅤStatus : Ubot Active \n"
        f"ㅤㅤㅤㅤModules:</b> <code>{len(modules)} Modules</code> \n"
        f"ㅤㅤㅤㅤBot Version: {BOT_VER} \n"
        f"ㅤㅤㅤㅤBranch: {branch} \n\n"
    )
    answers.append(
        InlineQueryResultArticle(
            title="alive",
            description="Check Bot's Stats",
            thumb_url="https://graph.org/file/0ed7be5cf4fdbf052afa9.jpg",
            input_message_content=InputTextMessageContent(
                msg, parse_mode=ParseMode.HTML, disable_web_page_preview=True
            ),
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url="https://t.me/Japanese_Userbot"), InlineKeyboardButton(text="ᴏᴡɴᴇʀ", url="https://t.me/Nobitaa_xd")], [InlineKeyboardButton(text="ᴍᴇɴᴜ", callback_data="reopen")]]
            ),
        )
    )
    return answers


async def help_function(answers):
    bttn = paginate_help(0, CMD_HELP, "helpme")
    answers.append(
        InlineQueryResultArticle(
            title="Help Article!",
            description="Check Command List & Help",
            thumb_url="https://graph.org/file/0ed7be5cf4fdbf052afa9.jpg",
            input_message_content=InputTextMessageContent(
                Data.text_help_menu.format(len(CMD_HELP))
            ),
            reply_markup=InlineKeyboardMarkup(bttn),
        )
    )
    return answers


@app.on_inline_query()
@inline_wrapper
async def inline_query_handler(client: Client, query):
    try:
        text = query.query.strip().lower()
        string_given = query.query.lower()
        answers = []
        if text.strip() == "":
            return
        elif text.split()[0] == "alipp":
            answerss = await alive_function(query, answers)
            await client.answer_inline_query(query.id, results=answerss, cache_time=10)
        elif string_given.startswith("helper"):
            answers = await help_function(answers)
            await client.answer_inline_query(query.id, results=answers, cache_time=0)
        elif string_given.startswith("alive"):
            answers = await peler_function(query, answers)
            await client.answer_inline_query(query.id, results=answers, cache_time=5)
    except Exception as e:
        e = traceback.format_exc()
        print(e, "InLine")