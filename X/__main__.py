import importlib
from pyrogram import idle
from uvloop import install


from X.modules import ALL_MODULES
from X import BOTLOG_CHATID, LOGGER, LOOP, aiosession, app, bots, ids, bot1
from X.helpers import join
from X.helpers.misc import create_botlog, heroku

BOT_VER = "3.0.0"
CMD_HANDLER = ["." "?" "!" "*"]
MSG_ON = """
✧✧ **𝐃ɪᴄᴛᴀᴛᴏʀ 𝐔sᴇʀ𝐁ᴏᴛ 𝐈s 𝐀ʟɪᴠᴇ** ✧✧
▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭

➥ **𝐃ɪᴄᴛᴀᴛᴏʀ 𝐕ᴇʀsɪᴏɴ 🥀 ** `{}`
➥ **𝐓ʏᴘᴇ** **.alive** **𝐓ᴏ 𝐂ʜᴇᴄᴋ 𝐀ʟɪᴠᴇ 𝐎ғ 𝐃ɪᴄᴛᴀᴛᴏʀ 𝐔sᴇʀ𝐁ᴏᴛ**
▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭
➥ 𝐎ᴡɴᴇʀ :- @SAIF_DICTATOR
➥ 𝐆ʀᴘ :- @DEAD_GRPCHAT
➥ 𝐂ʜᴀɴ :- @SAIFALLBOT
▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭
"""


async def main():
    await app.start()
    print("𝐋𝐎𝐆: 𝐅𝐨𝐮𝐧𝐝𝐞𝐝 𝐁𝐨𝐭 𝐭𝐨𝐤𝐞𝐧 𝐁𝐨𝐨𝐭𝐢𝐧𝐠..")
    for all_module in ALL_MODULES:
        importlib.import_module("X.modules" + all_module)
        print(f"𝐃ɪᴄᴛᴀᴛᴏʀ 𝐔sᴇʀ𝐁ᴏᴛ 𝐒ᴜᴄᴄᴇssғᴜʟʟʏ 𝐈ᴍᴘᴏʀᴛᴇᴅ {all_module} ")
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            await join(bot)
            try:
                await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER))
            except BaseException:
                pass
            print(f"𝐘ᴏᴜʀ 𝐃ɪᴄᴛᴀᴛᴏʀ 𝐔sᴇʀ𝐁ᴏᴛ 𝐒ᴛᴀʀᴛᴇᴅ 𝐀s{ex.first_name} | {ex.id} ")
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")
    if not str(BOTLOG_CHATID).startswith("-100"):
        await create_botlog(bot1)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("X").info("𝐷𝛪𝐶𝛵𝛥𝛵𝛩𝛤 𝑈𝑆𝛴𝛤𝛣𝛩𝛵 𝛪𝑆 𝑆𝛹𝛥𝛤𝛵𝛴𝐷 ✨")
    install()
    heroku()
    LOOP.run_until_complete(main())
