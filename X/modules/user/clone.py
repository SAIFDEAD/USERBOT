import os

from pyrogram import *
from pyrogram.types import *

from config import CMD_HANDLER as cmd
from X.helpers.basic import edit_or_reply, get_text, get_user

from .help import *

OWNER = os.environ.get("OWNER", None)
BIO = os.environ.get("BIO", "𝐃ɪᴄᴛᴀᴛᴏʀ 𝐔sᴇʀ𝐁ᴏᴛ 𝐉ᴏɪɴ @SAIFALLBOT")


@Client.on_message(filters.command("clone", cmd) & filters.me)
async def clone(client: Client, message: Message):
    text = get_text(message)
    op = await edit_or_reply(message, "`𝐂𝐥𝐨𝐧𝐢𝐧𝐠`")
    userk = get_user(message, text)[0]
    user_ = await client.get_users(userk)
    if not user_:
        await op.edit("`ᴡʜᴏᴍ ɪ sʜᴏᴜʟᴅ ᴄʟᴏɴᴇ:(`")
        return

    get_bio = await client.get_chat(user_.id)
    f_name = user_.first_name
    c_bio = get_bio.bio
    pic = user_.photo.big_file_id
    poto = await client.download_media(pic)

    await client.set_profile_photo(photo=poto)
    await client.update_profile(
        first_name=f_name,
        bio=c_bio,
    )
    await message.edit(f"**ʜᴇʟʟᴏ ❣️** __{f_name}__")


@Client.on_message(filters.command("revert", cmd) & filters.me)
async def revert(client: Client, message: Message):
    await message.edit("`ʀᴇᴠᴇʀᴛɪɴɢ`")
    r_bio = BIO

    # Get ur Name back
    await client.update_profile(
        first_name=OWNER,
        bio=r_bio,
    )
    # Delete first photo to get ur identify
    photos = [p async for p in client.get_chat_photos("me")]
    await client.delete_profile_photos(photos[0].file_id)
    await message.edit("`ɪ ᴀᴍ ʙᴀᴄᴋ!`")


add_command_help(
    "➥ 𝐂ʟᴏɴᴇ",
    [
        ["clone", "Tᴏ Cʟᴏɴᴇ ꜱᴏᴍᴇᴏɴᴇ Pʀᴏғɪʟᴇ."],
        ["revert", "Tᴏ Gᴇᴛ Yᴏᴜʀ Aᴄᴄᴏᴜɴᴛ Bᴀᴄᴋ."],
    ],
  )
