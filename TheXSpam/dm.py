# 𝑪𝒐𝒑𝒚𝒓𝒊𝒈𝒉𝒕 𝑩𝒚 𝑆𝑎𝑖𝑓𝑑𝑒𝑎𝑑
# 𝑨𝒍𝒍 𝑹𝒊𝒈𝒉𝒕𝒔 𝑹𝒆𝒔𝒆𝒓𝒗𝒆𝒅


import asyncio

from random import choice

from pyrogram import filters, Client
from pyrogram.types import Message

from data import OneWord, RAID, THE_ALTS
from config import SUDO_USERS


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dmraid"], [".", "/", "!"]))
async def dmraid(xspam: Client, message: Message):
      alt = message.text.split(" ")

      if len(alt) == 3:
          ok = await xspam.get_users(alt[2])
          id = ok.id

          if id in THE_ALTS:
                await message.reply_text(f"`𝐕ᴇʀɪғɪᴇᴅ 𝐁ʏ 𝐒ᴀɪғ 𝐁ᴏᴛᴢ`")
          elif id in SUDO_USERS:
                await message.reply_text(f"`𝐓ʜɪs 𝐏ᴇʀsᴏɴ 𝐈s 𝐌ʏ 𝐒ᴜᴅᴏ 𝐔sᴇʀ`")
          else:
              counts = int(alt[1])
              await message.reply_text("`𝐃ᴍ 𝐑ᴀɪᴅ 𝐒ᴛᴀʀᴛᴇᴅ 𝐒ᴜᴄᴄᴇssғᴜʟʟʏ`")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.1)

      elif message.reply_to_message and (len(alt) == 2):
          user_id = message.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = ok.id

          if id in THE_ALTS:
                await message.reply_text(f"`𝐕ᴇʀɪғɪᴇᴅ 𝐁ʏ 𝐒ᴀɪғ 𝐁ᴏᴛᴢ`")
          elif id in SUDO_USERS:
                await message.reply_text(f"`𝐓ʜɪs 𝐏ᴇʀsᴏɴ 𝐈s 𝐌ʏ 𝐒ᴜᴅᴏ 𝐔sᴇʀ`")
          else:
              counts = int(alt[1])
              await message.reply_text("`𝐃ᴍ 𝐑ᴀɪᴅ 𝐒ᴛᴀʀᴛᴇᴅ 𝐒ᴜᴄᴄᴇssғᴜʟʟʏ`")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.1)

      else:
            await message.reply_text("❣️ 𝐔sᴀɢᴇ:\n   !dmraid 13 <𝐑ᴇᴘʟʏ 𝐓ᴏ 𝐔sᴇʀ 𝐎ʀ 𝐔sᴇʀɴᴀᴍᴇ>")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dmspam"], [".", "!", "/"]))
async def dmspam(client: Client, message: Message):
    alt = message.text.split(" ", 3)

    if  len(alt) == 4:
        uid = int(alt[2])
        if uid in THE_ALTS:
            await message.reply_text(f"`𝐕ᴇʀɪғɪᴇᴅ 𝐁ʏ 𝐒ᴀɪғ 𝐁ᴏᴛᴢ`")
        elif uid in SUDO_USERS:
            await message.reply_text(f"`𝐓ʜɪs 𝐏ᴇʀsᴏɴ 𝐈s 𝐌ʏ 𝐒ᴜᴅᴏ 𝐔sᴇʀ`")
        else:
            quantity, spam_text = int(alt[1]), alt[3]
            await message.reply_text("`𝐃ᴍ 𝐒ᴘᴀᴍ 𝐒ᴛᴀʀᴛᴇᴅ 𝐒ᴜᴄᴄᴇssғᴜʟʟʏ`")
            for _ in range(quantity):
                await client.send_message(uid, spam_text)
                await asyncio.sleep(0.3)

    elif message.reply_to_message and (len(alt) == 3):
        id = message.reply_to_message.from_user.id

        if id in THE_ALTS:
            await message.reply_text(f"`𝐕ᴇʀɪғɪᴇᴅ 𝐁ʏ 𝐒ᴀɪғ 𝐁ᴏᴛᴢ`")
        elif id in SUDO_USERS:
            await message.reply_text(f"`𝐓ʜɪs 𝐏ᴇʀsᴏɴ 𝐈s 𝐌ʏ 𝐒ᴜᴅᴏ 𝐔sᴇʀ`")
        else:
            quantity = int(alt[1])
            spam_text = alt[2]
            await message.reply_text("`𝐃ᴍ 𝐒ᴘᴀᴍ 𝐒ᴛᴀʀᴛᴇᴅ 𝐒ᴜᴄᴄᴇssғᴜʟʟʏ`")
            for _ in range(quantity):
                await client.send_message(id, spam_text)
                await asyncio.sleep(0.3)

    else:
        await message.reply_text("🥀 𝐔sᴀɢᴇ:\n .dmspam 13 <𝐔ꜱᴇʀ 𝐈ᴅ> Saif Op\n .dmspam 10 Saif Op <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ>")
