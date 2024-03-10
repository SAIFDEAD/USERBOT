import asyncio

from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message

from data import THE_ALTS, RAID
from config import OWNER_ID, SUDO_USERS


# RAIDING FEATURES

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], ["/", "!", "."]))
async def raid(xspam: Client, message: Message):  
      # Hero = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      alt = message.text.split(" ")

      if len(alt) > 2:
            ok = await xspam.get_users(alt[2])
            id = ok.id
            if id in THE_ALTS:
                  await message.reply_text("» 𝐍ᴏ, 𝐓ʜɪꜱ 𝐆ᴜʏ 𝐈ꜱ 𝐘ᴏᴜʀ 𝐅ᴀᴛʜᴇʀ ")
            elif id == OWNER_ID:
                  await message.reply_text("» 𝐍ᴏ, 𝐓ʜɪꜱ 𝐆ᴜʏ 𝐈ꜱ 𝐎ᴡɴᴇʀ 𝐎ꜰ 𝐓ʜᴇ 𝐒ᴀɪғ 𝐁ᴏᴛꜱ.")
            elif id in SUDO_USERS:
                  await message.reply_text("» 𝐍ᴏ, 𝐓ʜɪꜱ 𝐆ᴜʏ 𝐈ꜱ 𝐀 𝐒ᴜᴅᴏ 𝐔ꜱᴇʀ")
            else:
                  counts = int(alt[1])
                  fname = ok.first_name
                  mention = f"[{fname}](tg://user?id={id})"
                  for _ in range(counts):
                        reply = choice(RAID)
                        msg = f"{mention} {reply}"
                        await xspam.send_message(message.chat.id, msg)
                        await asyncio.sleep(0.1)

      elif message.reply_to_message and (len(alt) == 2):
            user_id = message.reply_to_message.from_user.id
            ok = await xspam.get_users(user_id)
            id = ok.id
            if id in THE_ALTS:
                  await message.reply_text("» 𝐍ᴏ, 𝐓ʜɪꜱ 𝐆ᴜʏ 𝐈ꜱ 𝐘ᴏᴜʀ 𝐅ᴀᴛʜᴇʀ")
            elif id == OWNER_ID:
                  await message.reply_text("» 𝐍ᴏ, 𝐓ʜɪꜱ 𝐆ᴜʏ 𝐈ꜱ 𝐎ᴡɴᴇʀ 𝐎ꜰ 𝐓ʜᴇ 𝐒ᴀɪғ 𝐁ᴏᴛꜱ.")
            elif id in SUDO_USERS:
                  await message.reply_text("» 𝐍ᴏ, 𝐓ʜɪꜱ 𝐆ᴜʏ 𝐈ꜱ 𝐀 𝐒ᴜᴅᴏ 𝐔ꜱᴇʀ")
            else:
                  counts = int(alt[1])
                  fname = ok.first_name
                  mention = f"[{fname}](tg://user?id={id})"
                  for _ in range(counts):
                        reply = choice(RAID)
                        msg = f"{mention} {reply}"
                        await xspam.send_message(message.chat.id, msg)
                        await asyncio.sleep(0.1)

      else:
          await message.reply_text("ᴍᴏᴅᴜʟᴇ ɴᴀᴍᴇ: 𝐑𝐚𝐢𝐝\n  » .raid <𝐔ꜱᴇʀɴᴀᴍᴇ 𝐎ꜰ 𝐔ꜱᴇʀ>\n  » .raid <𝐑ᴇᴘʟʏ 𝐓ᴏ 𝐀 𝐔ꜱᴇʀ>")


rusers = []

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["rraid", "replyraid"], ["/", ".", "!"]))
async def rraid(xspam: Client, message: Message):
      global rusers
      alt = message.text.split(" ")

      if len(alt) > 1:
          ok = await xspam.get_users(alt[1])
          id = ok.id
          if id in THE_ALTS:
                await message.reply_text("» 𝐍ᴏ, 𝐓ʜɪꜱ 𝐆ᴜʏ 𝐈ꜱ 𝐘ᴏᴜʀ 𝐅ᴀᴛʜᴇʀ")
          elif id == OWNER_ID:
                await message.reply_text("» 𝐍ᴏ, 𝐓ʜɪꜱ 𝐆ᴜʏ 𝐈ꜱ 𝐎ᴡɴᴇʀ 𝐎ꜰ 𝐓ʜᴇ 𝐒ᴀɪғ 𝐁ᴏᴛꜱ.")
          elif id in SUDO_USERS:
                await message.reply_text("» 𝐍ᴏ, 𝐓ʜɪꜱ 𝐆ᴜʏ 𝐈ꜱ 𝐀 𝐒ᴜᴅᴏ 𝐔ꜱᴇʀ")
          else:
              rusers.append(id)
              await message.reply_text("» 𝐀ᴄᴛɪᴠᴀᴛᴇᴅ 𝐑ᴇᴘʟʏ 𝐑ᴀɪᴅ !! ✅")

      elif message.reply_to_message:
          user_id = message.reply_to_message.from_user.id
          if user_id in THE_ALTS:
                await message.reply_text("» 𝐍ᴏ, 𝐓ʜɪꜱ 𝐆ᴜʏ 𝐈ꜱ 𝐘ᴏᴜʀ 𝐅ᴀᴛʜᴇʀ")
          elif user_id == OWNER_ID:
                await message.reply_text("» 𝐍ᴏ, 𝐓ʜɪꜱ 𝐆ᴜʏ 𝐈ꜱ 𝐎ᴡɴᴇʀ 𝐎ꜰ 𝐓ʜᴇ 𝐒ᴀɪғ 𝐁ᴏᴛꜱ.")
          elif user_id in SUDO_USERS:
                await message.reply_text("» 𝐍ᴏ, 𝐓ʜɪꜱ 𝐆ᴜʏ 𝐈ꜱ 𝐀 𝐒ᴜᴅᴏ 𝐔ꜱᴇʀ")
          else:
              rusers.append(user_id)
              await message.reply_text("» 𝐀ᴄᴛɪᴠᴀᴛᴇᴅ 𝐑ᴇᴘʟʏ 𝐑ᴀɪᴅ !! ✅")

      else:
          await message.reply_text("𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐑𝐞𝐩𝐥𝐲𝐑𝐚𝐢𝐝\n  » .rraid <𝐔ꜱᴇʀɴᴀᴍᴇ 𝐎ꜰ 𝐔ꜱᴇʀ>\n  » .rraid <𝐑ᴇᴘʟʏ 𝐓ᴏ 𝐀 𝐔ꜱᴇʀ>")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["drraid", "draid", "dreplyraid"], ["/", ".", "!"]))
async def draid(xspam: Client, message: Message):
      global rusers
      alt = message.text.split(" ")

      if len(alt) > 1:
          ok = await xspam.get_users(alt[1])
          id = ok.id
          if id in rusers:
              rusers.remove(id)
              await message.reply_text("» 𝐑ᴇᴘʟʏ 𝐑ᴀɪᴅ 𝐃ᴇ-𝐀ᴄᴛɪᴠᴀᴛᴇᴅ !! ✅")

      elif message.reply_to_message:
          user_id = message.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = ok.id
          if id in rusers:
              rusers.remove(id)
              await message.reply_text("» 𝐑ᴇᴘʟʏ 𝐑ᴀɪᴅ 𝐃ᴇ-𝐀ᴄᴛɪᴠᴀᴛᴇᴅ !! ✅")

      else:
          await message.reply_text("𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐃𝐑𝐞𝐩𝐥𝐲𝐑𝐚𝐢𝐝\n  » .drraid <𝐔ꜱᴇʀɴᴀᴍᴇ 𝐎ꜰ 𝐔ꜱᴇʀ>\n  » .drraid <𝐑ᴇᴘʟʏ 𝐓ᴏ 𝐀 𝐔ꜱᴇʀ>")
    

@Client.on_message(~filters.me & filters.incoming)
async def watcher(_, msg: Message):
      global rusers
      id = msg.from_user.id
      if id in rusers:
            reply = choice(RAID)
            await msg.reply_text(reply)
