# 𝑪𝒐𝒑𝒚𝒓𝒊𝒈𝒉𝒕 𝑩𝒚 𝑆𝑎𝑖𝑓𝑑𝑒𝑎𝑑
# 𝑨𝒍𝒍 𝑹𝒊𝒈𝒉𝒕𝒔 𝑹𝒆𝒔𝒆𝒓𝒗𝒆𝒅

import sys
import datetime

from os import execle, environ
from config import ALIVE_PIC, SUDO_USERS

from pyrogram import Client, filters
from pyrogram.types import Message


ALT = f"""❖ 𝙎𝘼𝙄𝙁 𝙐𝙎𝙀𝙍𝘽𝙊𝙏 𝙎𝙔𝙎𝙏𝙀𝙈  ❖

➠ **𝐏ʏᴛʜᴏɴ 𝐕ᴇʀsɪᴏɴ** : `3.11.1`
➠ **𝐏ʏʀᴏ 𝐕ᴇʀsɪᴏɴ** : `1.4.16`
➠ **𝐒ᴀɪғ 𝐔sᴇʀʙᴏᴛ 𝐕ᴇʀsɪᴏɴ**  : `3.3`
➠ **𝐔ᴘᴅᴀᴛᴇꜱ** : @SAIFALLBOT\n"""


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], ["/", ".", "!"]))
async def ping(_, e: Message):       
      start = datetime.datetime.now()
      Fuk = await e.reply("**𝗦𝗔𝗜𝗙 𝗢𝗣**")
      end = datetime.datetime.now()
      ms = (end-start).microseconds / 1000
      await Fuk.edit_text(f"𝐀ʟɪᴠᴇ 𝐌ʏ [𝐌ᴀsᴛᴇʀ](https://t.me/SAIFALLBOT)")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], ["/", ".", "!"]))
async def alive(xspam: Client, msg: Message):
       if ".jpg" in ALIVE_PIC or ".png" in ALIVE_PIC:
              await xspam.send_photo(msg.chat.id, ALIVE_PIC, caption=ALT)
       if ".mp4" in ALIVE_PIC or ".MP4," in ALIVE_PIC:
              await xspam.send_video(msg.chat.id, ALIVE_PIC, caption=ALT)


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["reboot", "restart"], ["/", ".", "!"]))
async def restart_bot(_, message: Message):
    msg = await message.reply("`ʀᴇsᴛᴀʀᴛɪɴɢ ʙᴏᴛ sᴀɪғ ᴜsᴇʀ ʙᴏᴛ...`")
    args = [sys.executable, "main.py"]
    await msg.edit("» ʙᴏᴛ ʀᴇsᴛᴀʀᴛᴇᴅ...\n» ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ sᴀɪғ ᴜsᴇʀ ʙᴏᴛ ᴀғᴛᴇʀ 𝟷 ᴍɪɴᴜᴛᴇ ")
    execle(sys.executable, *args, environ)
