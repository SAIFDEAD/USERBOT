# © @SAIFDEAD

import heroku3

from os import getenv
from config import SUDO_USERS, ALIVE_PIC, OWNER_ID, HEROKU_APP_NAME, HEROKU_API_KEY

from pyrogram import Client, filters
from pyrogram.types import Message


FIRST_TEXT = f"""★ 𝗦𝗔𝗜𝗙 𝗨𝗦𝗘𝗥𝗕𝗢𝗧 𝗛𝗘𝗟𝗣 𝗠𝗘𝗡𝗨 ★

**» 𝐀ʟʟ 𝐂ᴏᴍᴍᴀɴᴅ:** [𝐂ʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/SAIFALLBOT/19)
**» 𝐌ᴜsɪᴄ:** [𝐂ʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/HINATA_N_BOT)
**» 𝐑ᴏʙᴏᴛ:** [𝐂ʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/NARUTO_X_ROBOT)
**» 𝐎ᴡɴᴇʀ:** [𝐂ʟɪᴄᴋ](https://t.me/SAIF_DICTATOR)"""


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["help"], [".", "!", "/"]))
async def help(client: Client, message: Message):
    await client.send_photo(
        chat_id=message.chat.id,
        photo=ALIVE_PIC,
        caption=FIRST_TEXT
    )


@Client.on_message(filters.user(OWNER_ID) & filters.command(["sudo"], ["/", ".", "!"]))
async def add_sudo(_, message: Message):
       if not message.reply_to_message:
              await message.reply_text("» 𝐑ᴇᴘʟʏ 𝐓ᴏ 𝐀 𝐔ꜱᴇʀ !!")
              return
       elif HEROKU_APP_NAME is None:
              await message.reply_text("`[HEROKU]:" "\n𝐏ʟᴇᴀsᴇ 𝐒ᴇᴛᴜᴘ 𝐘ᴏᴜʀ` **HEROKU_APP_NAME**")
              return
       elif HEROKU_API_KEY is None:
              await message.reply_text("`[HEROKU]:" "\n𝐏ʟᴇᴀsᴇ 𝐒ᴇᴛᴜᴘ 𝐘ᴏᴜʀ` **HEROKU_API_KEY**")
              return
       else:
              heroku = heroku3.from_key(HEROKU_API_KEY)
              app = heroku.app(HEROKU_APP_NAME)

       ok = await message.reply_text(f"» 𝐀ᴅᴅɪɴɢ 𝐔ꜱᴇʀ 𝐀ꜱ 𝐒ᴜᴅᴏ...")
       heroku_var = app.config()

       sudousers = getenv("SUDO_USERS")
       target = message.reply_to_message.from_user.id
       if len(sudousers) > 0:
              newsudo = f"{sudousers} {target}"
       else:
              newsudo = f"{target}"
       await ok.edit(f"» **𝐍ᴇᴡ 𝐒ᴜᴅᴏ 𝐔ꜱᴇʀ**: `{target}`\n» `ʀᴇsᴛᴀʀᴛɪɴɢ ʙᴏᴛ...`")
       heroku_var["SUDO_USERS"] = newsudo   
