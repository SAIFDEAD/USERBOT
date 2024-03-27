import time
from datetime import datetime

import speedtest
from pyrogram import Client, filters
from pyrogram.raw import functions
from pyrogram.types import Message

from config import CMD_HANDLER
from config import BOT_VER, BRANCH as brch
from X import CMD_HELP, StartTime
from X.helpers.basic import edit_or_reply
from X.helpers.constants import WWW
from X.helpers.PyroHelpers import SpeedConvert
from X.modules.bot.inline import get_readable_time
from X.helpers.adminHelpers import DEVS

from .help import *

modules = CMD_HELP

@Client.on_message(filters.command(["speed", "speedtest"], cmd) & filters.me)
async def speed_test(client: Client, message: Message):
    new_msg = await edit_or_reply(message, "`Running speed test . . .`")
    spd = speedtest.Speedtest()

    new_msg = await message.edit(
        f"`{new_msg.text}`\n" "`Getting best server based on ping . . .`"
    )
    spd.get_best_server()

    new_msg = await message.edit(f"`{new_msg.text}`\n" "`Testing download speed . . .`")
    spd.download()

    new_msg = await message.edit(f"`{new_msg.text}`\n" "`Testing upload speed . . .`")
    spd.upload()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`Getting results and preparing formatting . . .`"
    )
    results = spd.results.dict()

    await message.edit(
        WWW.SpeedTest.format(
            start=results["timestamp"],
            ping=results["ping"],
            download=SpeedConvert(results["download"]),
            upload=SpeedConvert(results["upload"]),
            isp=results["client"]["isp"],
        )
    )


@Client.on_message(filters.command("dc", cmd) & filters.me)
async def nearest_dc(client: Client, message: Message):
    dc = await client.send(functions.help.GetNearestDc())
    await edit_or_reply(
        message, WWW.NearestDC.format(dc.country, dc.nearest_dc, dc.this_dc)
    )


@Client.on_message(
    filters.command("Cpink", [""]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command("ping", cmd) & filters.me)
async def pingme(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await message.reply_text(
        f"❏ **ᴘɪɴɢ ᴘᴏɴɢ !!**\n"
        f"**├• ** `%sms`\n"
        f"╰•** Mᴀsᴛᴇʀ :** {client.me.mention}" % (duration)
    )


@Client.on_message(filters.command("Cping", [""]) & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.command("pink", cmd) & filters.me)
async def pink(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    X = await message.reply("**Sabarr Dog Lagging...**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await X.edit(
        f"**❏Japanese-X-Userbot**\n"
        f"**├• PING   :** "
        f"`%sms` \n"
        f"**├•  Uptime  :** "
        f"`{uptime}` \n"
        f"**└•  my father   :** {client.me.mention}" % (duration)
    )
  

@Client.on_message(
    filters.command("Ceping", [""]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command("pong", cmd) & filters.me)
async def uputt(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await edit_or_reply(message, "DEAR COCOKIN")
    await xx.edit("8=✊==D")
    await xx.edit("8==✊=D")
    await xx.edit("8===✊D")
    await xx.edit("8==✊=D")
    await xx.edit("8=✊==D")
    await xx.edit("8✊===D")
    await xx.edit("8=✊==D")
    await xx.edit("8==✊=D")
    await xx.edit("8===✊D")
    await xx.edit("8==✊=D")
    await xx.edit("8=✊==D")
    await xx.edit("8✊===D")
    await xx.edit("8=✊==D")
    await xx.edit("8==✊=D")
    await xx.edit("8===✊D")
    await xx.edit("**AHH I'M GOING TO CROT**")
    await xx.edit("8===✊D💦")
    await xx.edit("8====D💦💦")
    await xx.edit("**CROOTTTT**")
    await xx.edit("**CROOTTTT AAAHHH.....**")
    await xx.edit("AHHH ENAKKKKK DARLINGGGG🥵🥵")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xx.edit(
        f"❏ **CROTTT!!🥵**\n"
        f"├• **AHHH🤤** - `%sms`\n"
        f"├• **Lottery -** `{uptime}` \n"
        f"└• **Dick :** {client.me.mention}" % (duration)
  )
