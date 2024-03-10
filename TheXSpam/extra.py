# © @PyXen

import heroku3

from os import getenv
from config import SUDO_USERS, ALIVE_PIC, OWNER_ID, HEROKU_APP_NAME, HEROKU_API_KEY

from pyrogram import Client, filters
from pyrogram.types import Message


FIRST_TEXT = f"""★ 𝗦𝗔𝗜𝗙 𝗨𝗦𝗘𝗥𝗕𝗢𝗧 𝗛𝗘𝗟𝗣 𝗠𝗘𝗡𝗨 ★

**» 𝐀ʟʟ 𝐂ᴏᴍᴍᴀɴᴅ:** [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/AltronAds/11)
**» 𝐌ᴜsɪᴄ:** [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/AltronAds/12)
**» 𝐑ᴏʙᴏᴛ:** [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/)
**» 𝐎ᴡɴᴇʀ:** [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/SAIF_DICTATOR)"""


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
              await message.reply_text("» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ !!")
              return
       elif HEROKU_APP_NAME is None:
              await message.reply_text("`[HEROKU]:" "\nᴘʟᴇᴀsᴇ sᴇᴛᴜᴘ ʏᴏᴜʀ` **HEROKU_APP_NAME**")
              return
       elif HEROKU_API_KEY is None:
              await message.reply_text("`[HEROKU]:" "\nᴘʟᴇᴀsᴇ sᴇᴛᴜᴘ ʏᴏᴜʀ` **HEROKU_API_KEY**")
              return
       else:
              heroku = heroku3.from_key(HEROKU_API_KEY)
              app = heroku.app(HEROKU_APP_NAME)

       ok = await message.reply_text(f"» __ᴀᴅᴅɪɴɢ ᴜꜱᴇʀ ᴀꜱ ꜱᴜᴅᴏ...__")
       heroku_var = app.config()

       sudousers = getenv("SUDO_USERS")
       target = message.reply_to_message.from_user.id
       if len(sudousers) > 0:
              newsudo = f"{sudousers} {target}"
       else:
              newsudo = f"{target}"
       await ok.edit(f"» **ɴᴇᴡ ꜱᴜᴅᴏ ᴜꜱᴇʀ**: `{target}`\n» `ʀᴇsᴛᴀʀᴛɪɴɢ ʙᴏᴛ...`")
       heroku_var["SUDO_USERS"] = newsudo   
