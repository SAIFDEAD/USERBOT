from pyrogram.types import InlineKeyboardButton
from X import CMD_HELP
class Data:

    text_help_menu = (
        "**𝐌𝐞𝐧𝐮 𝐈𝐧𝐥𝐢𝐧𝐞 𝐃𝐢𝐜𝐭𝐚𝐭𝐨𝐫 𝐔𝐬𝐞𝐫𝐛𝐨𝐭**\n**𝐏𝐫𝐞𝐟𝐢𝐱𝐞𝐬:** ., ?, !, *"
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
    )
    reopen = [[InlineKeyboardButton("𖠁⃝ ꜱᴇᴇ ᴍᴏʀᴇ 𖠁⃝", callback_data="reopen")]]
