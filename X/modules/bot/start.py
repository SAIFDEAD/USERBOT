import random
from X import app
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from config import OWNER_ID as owner 

@app.on_callback_query()
def pmowner(client, callback_query):
    user_id = owner
    message = "A Pᴏᴡᴇʀғᴜʟ Assɪᴛᴀɴᴛ 𝐉𝐀𝐏𝐀𝐍𝐄𝐒𝐄 𝐗 𝐔𝐒𝐄𝐑𝐁𝐎𝐓!!!!"
    client.send_message(user_id, message)
    client.answer_callback_query(callback_query.id, text="Message sent")

logoX = [
    "https://graph.org/file/83978974fe5be2da118d7.jpg"
]

alive_logo = random.choice(logoX)

@app.on_message(filters.command("start") & filters.private)
async def start(app, message):
    chat_id = message.chat.id
    file_id = alive_logo
    caption = "Hello, Mʏ Mᴀsᴛᴇʀ!!\nNice To Meet You 🤗 !!\nI guess, that you know me, Uhh you don't, np..\nWell.\n\nA Pᴏᴡᴇʀғᴜʟ Assɪᴛᴀɴᴛ \n\n Pᴏᴡᴇʀᴇᴅ Bʏ [𝐉𝐀𝐏𝐀𝐍𝐄𝐒𝐄 𝐗 𝐔𝐒𝐄𝐑𝐁𝐎𝐓](t.me/Japanese_Userbot)\n\nYᴏᴜ Cᴀɴ Cʜᴀᴛ Wɪᴛʜ Mʏ Mᴀsᴛᴇʀ Tʜʀᴏᴜɢʜ Tʜɪs Bᴏᴛ.\nIғ Yᴏᴜ Wᴀɴᴛ Yᴏᴜʀ Oᴡɴ Assɪᴛᴀɴᴛ Yᴏᴜ Cᴀɴ Dᴇᴘʟᴏʏ Fʀᴏᴍ Bᴜᴛᴛᴏɴ Bᴇʟᴏᴡ."
    reply_markup = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("𝐒𝐮𝐩𝐩𝐨𝐫𝐭", url="https://t.me/Japanese_Userbot_Support"),
            InlineKeyboardButton("𝐂𝐡𝐚𝐧𝐧𝐞𝐥", url="https://t.me/Japanese_Userbot"),
            InlineKeyboardButton("𝐎𝐰𝐧𝐞𝐫", url="https://t.me/Nobitaa_xd"),
            InlineKeyboardButton("𝐑𝐞𝐩𝐨", url="https://github.com/Team-Japanese/Japanese-X-Userbot"),
        ],
    ])

    await app.send_photo(chat_id, file_id, caption=caption, reply_markup=reply_markup)
