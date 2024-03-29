from pyrogram import Client, filters
from X.Database.pm import *
from X.powers import get_id
from config import PMPERMIT_PIC, CMD_HANDLER
hl = CMD_HANDLER
pm_watcher = 5
NOBIGEY = PMPERMIT_PIC

TEXT = """
**Hᴇʟʟᴏ sɪʀ ᴍʏsᴇʟғ [Jᴀᴘᴀɴᴇsᴇ-X-Usᴇʀʙᴏᴛ](https://github.com/Team-Japanese/Japanese-X-Userbot), ᴏᴡɴᴇʀ » {} Pʀᴏᴛᴇᴄᴛɪᴏɴ **
**Hᴇʏ ᴛʜᴇʀᴇ!! I'ᴍ Jᴀᴘᴀɴᴇsᴇ-X-Usᴇʀʙᴏᴛ ᴀɴᴅ I'ᴍ ʜᴇʀᴇ ᴛᴏ Pʀᴏᴛᴇᴄᴛ ᴏᴡɴᴇʀ » {}..**
**Dᴏɴ'ᴛ Uɴᴅᴇʀ Esᴛɪᴍᴀᴛᴇ ᴍᴇ 😈😈**
**Mʏ ᴏᴡɴᴇʀ » {}  ɪs ʙᴜsʏ ʀɪɢʜᴛ ɴᴏᴡ !! **
• **ᴡᴀʀɴ ʟɪᴍɪᴛs** » {}      
╰• **ʏᴏᴜʀ ᴡᴀʀɴs** » {}
**Mʏ Mᴀsᴛᴇʀ ʜᴀs ᴀssɪɢɴᴇᴅ ᴍᴇ ᴛʜᴇ ᴅᴜᴛʏ ᴛᴏ ᴋᴇᴇᴘ ᴀ ᴄʜᴇᴄᴋ ᴏɴ ʜɪs PM, Aɴᴅ ɪ'ʟʟ ᴅᴏ ɪᴛ ғᴀɪᴛʜғᴜʟʟʏ..Sᴏ ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ᴅɪsᴛᴜʀʙ ʜɪᴍ..**
**Iғ ᴜ Sᴘᴀᴍ, ᴏʀ ᴛʀɪᴇᴅ ᴀɴʏᴛʜɪɴɢ ғᴜɴɴʏ, I'ᴠᴇ ғᴜʟʟ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ Bʟᴏᴄᴋ + Rᴇᴘᴏʀᴛ ʏᴏᴜ ᴀs Sᴘᴀᴍ ɪɴ Tᴇʟᴇɢʀᴀᴍ's sᴇʀᴠᴇʀ...**
"""

@Client.on_message(filters.command("pmpermit", hl) & filters.me)
async def pmpermit(client, message):
    x = await is_pm_on()
    try:
        tg = message.text.split()[1].lower()
    except:
        return await message.edit(f"{hl}pmpermit [on | off]")
    if not tg in ["on", "off"]:
        return await message.edit(f"{hl}pmpermit [on | off]")
    if tg == "on":
        if x:
            return await message.edit("ᴘᴍᴘᴇʀᴍɪᴛ ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ....")
        await toggle_pm()
        if await limit() == 0:
            await update_warns(3)
        return await message.edit("ᴘᴍᴘᴇʀᴍɪᴛ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴇɴᴀʙʟᴇᴅ....")
    if not x:
        return await message.edit("ᴘᴍᴘᴇʀᴍɪᴛ ɪꜱ ɴᴏᴛ ᴇɴᴀʙʟᴇᴅ....")
    await toggle_pm()
    return await message.edit("ᴘᴍᴘᴇʀᴍɪᴛ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴅɪꜱᴀʙʟᴇᴅ....")

@Client.on_message(filters.command(["approve", "disapprove"], hl) & filters.me)
async def appr_dis(client, message):
    if str(message.chat.id)[0] == "-":
        try:
            id = await get_id(_, message)
        except:
            return await message.edit("ꜰᴏʀ ᴀᴘᴘʀᴏᴠᴇ ᴜꜱᴇʀ ɪɴ ɢʀᴏᴜᴘ ᴜ ᴡᴀɴᴛ ᴛᴏ ɢɪᴠᴇ ᴍᴇ ɪ'ᴅ ᴏʀ ʀᴇᴘʟʏ ᴛʜᴀᴛ ᴜꜱᴇʀ..")
    else:
        id = message.chat.id
    tg = message.text.split()[0][1]
    x = await is_approved(id)
    if tg == "d":
        if not x:
            return await message.edit("ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ɴᴏᴛ ᴀᴘᴘʀᴏᴠᴇᴅ..")
        await disapprove(id)
        return await message.edit("ᴜꜱᴇʀ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴅɪꜱᴀᴘᴘʀᴏᴠᴇᴅ ᴛᴏ ᴘᴍ....")
    if x:
        return await message.edit("ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ ᴜꜱᴇʀ ᴀʟʀᴇᴀᴅʏ ᴀᴘᴘʀᴏᴠᴇᴅ....")
    await approve(id) 
    await reset_warns(id)
    return await message.edit("ᴜꜱᴇʀ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴀᴘᴘʀᴏᴠᴇᴅ ᴛᴏ ᴘᴍ....")

@Client.on_message(filters.command("setwarns", hl) & filters.me)
async def setwarn(client, message):
    try:
        count = int(message.text.split()[1])
    except:
        return await message.edit(f"{hl}setwarns [ᴠᴀʟᴜᴇ]")
    if count == 0:
        return await message.edit("ɢɪᴠᴇ ᴍᴇ ᴠᴀʟᴜᴇ ᴛᴏ ꜱᴇᴛ ᴡᴀʀɴꜱ..")
    await update_warns(count)
    await message.edit(f"ᴅᴍ ᴡᴀʀɴꜱ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ꜱᴇᴛ ᴛᴏ {count}..")
    
@Client.on_message(filters.private, group=pm_watcher)
async def wtch(client, message):
    user_ = message.from_user
    if message.from_user.id == client.me.id:
        return
    if not await is_pm_on():
        return
    if user_.is_bot:
        return
    if await is_approved(message.from_user.id):
        return
    await add_warn(message.from_user.id)
    if await limit() <= await get_warns(message.from_user.id):
        await message.reply("ꜱᴘᴀᴍᴍᴇʀ ᴅᴇᴛᴇᴄᴛᴇᴅ ᴀɴᴅ ʙʟᴏᴄᴋᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ.....")
        await reset_warns(message.from_user.id)
        return await client.block_user(message.from_user.id)
    await message.reply_photo(NOBIGEY, caption=TEXT.format((await client.get_me()).first_name, await limit(), await get_warns(message.from_user.id)))


add_command_help(
    "•─╼⃝𖠁 ᴘᴍᴘᴇʀᴍɪᴛ",
    [
        [
            f"ok ᴏʀ {cmd}setuju",
            "Rᴇᴄᴇɪᴠᴇ ꜱᴏᴍᴇᴏɴᴇ'ꜱ ᴍᴇꜱꜱᴀɢᴇ ʙʏ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴛʜᴇɪʀ ᴍᴇꜱꜱᴀɢᴇ ᴏʀ ᴛᴀɢꜱ ᴀɴᴅ ᴀʟꜱᴏ ᴛᴏ ᴅᴏ ɪɴ ᴘᴍ",
        ],
        [
            f"minus ᴏʀ {cmd}nopm",
            "Rᴇɪᴇᴄᴛ ꜱᴏᴍᴇᴏɴᴇ'ꜱ ᴍᴇꜱꜱᴀɢᴇ ʙʏ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ ᴏʀ ᴛᴀɢꜱ ᴀɴᴅ ᴀʟꜱᴏ ᴛᴏ ᴅᴏ ɪɴ ᴘᴍ",
        ],
        [
            "pmlimit <ɴᴜᴍʙᴇʀ>",
            "Tᴏ ᴄᴜꜱᴛᴏᴍɪᴢᴇ ᴛʜᴇ ᴀᴜᴛᴏ ʙʟᴏᴄᴋ ᴍᴇꜱꜱᴀɢᴇ ʟɪᴍɪᴛ ᴍᴇꜱꜱᴀɢᴇ",
        ],
        [
            "pmpermit ᴏɴ/ᴏғғ",
            "Tᴏ ᴇɴᴀʙʟᴇ ᴏʀ ᴅɪꜱᴀʙʟᴇ PMPERMIT",
        ],
    ],
)
