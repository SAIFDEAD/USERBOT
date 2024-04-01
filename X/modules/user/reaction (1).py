import asyncio

import aiohttp
from pyrogram import filters, Client
from pyrogram.types import Message


from X.helpers.PyroHelpers import GetChatID, ReplyCheck
from .help import *


@Client.on_message(filters.command(["bully", "bullys"], ".") & filters.me)
async def give_bully(bot: Client, message: Message):
    URL = "https://api.waifu.pics/sfw/bully"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no reaction for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )

@Client.on_message(filters.command(["cuddle", "cuddles"], ".") & filters.me)
async def give_cuddle(bot: Client, message: Message):
    URL = "https://api.waifu.pics/sfw/cuddle"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no reaction for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )

@Client.on_message(filters.command(["cry", "cries"], ".") & filters.me)
async def give_cry(bot: Client, message: Message):
    URL = "https://api.waifu.pics/sfw/cry"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no reaction for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )

@Client.on_message(filters.command(["hug", "hugs"], ".") & filters.me)
async def give_hug(bot: Client, message: Message):
    URL = "https://api.waifu.pics/sfw/hug"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no reaction for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )

@Client.on_message(filters.command(["awoo", "awoos"], ".") & filters.me)
async def give_awoo(bot: Client, message: Message):
    URL = "https://api.waifu.pics/sfw/awoo"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no reaction for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )

@Client.on_message(filters.command(["kiss", "ki"], ".") & filters.me)
async def give_kiss(bot: Client, message: Message):
    URL = "https://api.waifu.pics/sfw/kiss"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no reaction for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )

@Client.on_message(filters.command(["lick", "lic"], ".") & filters.me)
async def give_lick(bot: Client, message: Message):
    URL = "https://api.waifu.pics/sfw/lick"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no reaction for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )

@Client.on_message(filters.command(["pat", "pats"], ".") & filters.me)
async def give_pat(bot: Client, message: Message):
    URL = "https://api.waifu.pics/sfw/pat"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no reaction for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )

@Client.on_message(filters.command(["smug", "smugs"], ".") & filters.me)
async def give_smug(bot: Client, message: Message):
    URL = "https://api.waifu.pics/sfw/smug"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no reaction for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )

@Client.on_message(filters.command(["bonk", "bonks"], ".") & filters.me)
async def give_bonk(bot: Client, message: Message):
    URL = "https://api.waifu.pics/sfw/bonk"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no reaction for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )

@Client.on_message(filters.command(["yeet", "yeets"], ".") & filters.me)
async def give_yeet(bot: Client, message: Message):
    URL = "https://api.waifu.pics/sfw/yeet"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no reaction for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )

@Client.on_message(filters.command(["blush", "blushes"], ".") & filters.me)
async def give_blush(bot: Client, message: Message):
    URL = "https://api.waifu.pics/sfw/blush"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no reaction for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )

@Client.on_message(filters.command(["smile", "smiles"], ".") & filters.me)
async def give_smile(bot: Client, message: Message):
    URL = "https://api.waifu.pics/sfw/smile"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no reaction for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )

@Client.on_message(filters.command(["waves", "wave"], ".") & filters.me)
async def give_wave(bot: Client, message: Message):
    URL = "https://api.waifu.pics/sfw/wave"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no reaction for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )

@Client.on_message(filters.command(["handhold", "hh"], ".") & filters.me)
async def give_handhold(bot: Client, message: Message):
    URL = "https://api.waifu.pics/sfw/handhold"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no reaction for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )

@Client.on_message(filters.command(["highfive", "hf"], ".") & filters.me)
async def give_highfive(bot: Client, message: Message):
    URL = "https://api.waifu.pics/sfw/highfive"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no reaction for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )

@Client.on_message(filters.command(["glomp", "glomps"], ".") & filters.me)
async def give_glomp(bot: Client, message: Message):
    URL = "https://api.waifu.pics/sfw/glomp"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no reaction for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )

@Client.on_message(filters.command(["bites", "bite"], ".") & filters.me)
async def give_bite(bot: Client, message: Message):
    URL = "https://api.waifu.pics/sfw/bite"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no reaction for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )

@Client.on_message(filters.command(["nom", "noms"], ".") & filters.me)
async def give_nom(bot: Client, message: Message):
    URL = "https://api.waifu.pics/sfw/nom"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no reaction for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )

@Client.on_message(filters.command(["wink", "winks"], ".") & filters.me)
async def give_wink(bot: Client, message: Message):
    URL = "https://api.waifu.pics/sfw/wink"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no reaction for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )

@Client.on_message(filters.command(["happy", "happys"], ".") & filters.me)
async def give_happy(bot: Client, message: Message):
    URL = "https://api.waifu.pics/sfw/happy"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no reaction for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )

@Client.on_message(filters.command(["kill", "kills"], ".") & filters.me)
async def give_kill(bot: Client, message: Message):
    URL = "https://api.waifu.pics/sfw/kill"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no reaction for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )

@Client.on_message(filters.command(["slap", "slaps"], ".") & filters.me)
async def give_slap(bot: Client, message: Message):
    URL = "https://api.waifu.pics/sfw/slap"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no reaction for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )

@Client.on_message(filters.command(["poke", "pokes"], ".") & filters.me)
async def give_poke(bot: Client, message: Message):
    URL = "https://api.waifu.pics/sfw/poke"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no reaction for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )

@Client.on_message(filters.command(["dance", "dances"], ".") & filters.me)
async def give_dance(bot: Client, message: Message):
    URL = "https://api.waifu.pics/sfw/dance"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no reaction for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )

@Client.on_message(filters.command(["cringe", "cringeg"], ".") & filters.me)
async def give_cringe(bot: Client, message: Message):
    URL = "https://api.waifu.pics/sfw/cringe"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no reaction for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )

add_command_help(
    "•─╼⃝𖠁 ʀᴇᴀᴄᴛɪᴏɴ",
    [
       ["pat", "Gɪᴠᴇ ᴘᴀᴛꜱ."],
       ["bully", "Gɪᴠᴇ ʙᴜʟʟʏ ᴀɴɪᴍᴀᴛɪᴏɴ."],
       ["cuddle", "Gɪᴠᴇ ᴄᴜᴅᴅʟᴇ ᴀɴɪᴍᴀᴛɪᴏɴ."],
       ["cry", "Gɪᴠᴇ ᴄʀʏ ᴀɴɪᴍᴀᴛɪᴏɴ."],
       ["hug", "Gɪᴠᴇ ʜᴜɢ ᴀɴɪᴍᴀᴛɪᴏɴ."],
       ["awoo", "Gɪᴠᴇ ᴀᴡᴏᴏ ᴀɴɪᴍᴀᴛɪᴏɴ."],
       ["kiss", "Gɪᴠᴇ ᴋɪꜱꜱ ᴀɴɪᴍᴀᴛɪᴏɴ."],
       ["lick", "Gɪᴠᴇ ʟɪᴄᴋ ᴀɴɪᴍᴀᴛɪᴏɴ."],
       ["smug", "Gɪᴠᴇ ꜱᴍᴜɢ ᴀɴɪᴍᴀᴛɪᴏɴ."],
       ["bonk", "Gɪᴠᴇ ʙᴏɴᴋ ᴀɴɪᴍᴀᴛɪᴏɴ."],
       ["yeet", "Gɪᴠᴇ ʏᴇᴇᴛ ᴀɴɪᴍᴀᴛɪᴏɴ."],
       ["blush", "Gɪᴠᴇ ʙʟᴜꜱʜ ᴀɴɪᴍᴀᴛɪᴏɴ."],
       ["smile", "Gɪᴠᴇ ꜱᴍɪʟᴇ ᴀɴɪᴍᴀᴛɪᴏɴ."],
       ["wave", "Gɪᴠᴇ ᴡᴀᴠᴇ ᴀɴɪᴍᴀᴛɪᴏɴ."],
       ["highfive", "Gɪᴠᴇ ʜɪɢʜғɪᴠᴇ ᴀɴɪᴍᴀᴛɪᴏɴ."],
       ["handhold", "Gɪᴠᴇ ʜᴀɴᴅʜᴏʟᴅ ᴀɴɪᴍᴀᴛɪᴏɴ."],
       ["nom", "Gɪᴠᴇ ɴᴏᴍ ᴀɴɪᴍᴀᴛɪᴏɴ."],
       ["bite", "Gɪᴠᴇ ʙɪᴛᴇ ᴀɴɪᴍᴀᴛɪᴏɴ."],
       ["glomp", "Gɪᴠᴇ ɢʟᴏᴍᴘ ᴀɴɪᴍᴀᴛɪᴏɴ."],
       ["slap", "Gɪᴠᴇ ꜱʟᴀᴘ ᴀɴɪᴍᴀᴛɪᴏɴ."],
       ["kill", "Gɪᴠᴇ ᴋɪʟʟ ᴀɴɪᴍᴀᴛɪᴏɴ."],
       ["happy", "Gɪᴠᴇ ʜᴀᴘᴘʏ ᴀɴɪᴍᴀᴛɪᴏɴ."],
       ["wink", "Gɪᴠᴇ ᴡɪɴᴋ ᴀɴɪᴍᴀᴛɪᴏɴ."],
       ["poke", "Gɪᴠᴇ ᴘᴏᴋᴇ ᴀɴɪᴍᴀᴛɪᴏɴ."],
       ["dance", "Gɪᴠᴇ ᴅᴀɴᴄᴇ ᴀɴɪᴍᴀᴛɪᴏɴ."],
       ["cringe", "Gɪᴠᴇ ᴄʀɪɴɢᴇ ᴀɴɪᴍᴀᴛɪᴏɴ."],
    ],
          )
