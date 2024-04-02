import json
from aiohttp.client_exceptions import ClientError
from pyrogram import filters, Client
from pyrogram.types import Message
from X.helpers.aiohttp_helper import AioHttp
from .help import *

cf_apii_data = {
    "japan": {
        "url": "https://expressional-leaper.000webhostapp.com/image.php?random-data",
        "help": "see my country's beauty !",
    }
}

texit_api_commands = []
for x in cf_apii_data:
    texit_api_commands.append(x)
    if "alts" in cf_apii_data[x]:
        for y in cf_apii_data[x]["alts"]:
            texit_api_commands.append(y)

@Client.on_message(filters.command(texit_api_commands, ".") & filters.me)
async def japan_api(bot: Client, message: Message):
    cmd = message.command
    api_key = cmd[0]
    api = cf_apii_data.get(api_key)

    if not api:
        await message.reply("Invalid command")
        return

    try:
        data = await AioHttp().get_json(api["url"])

        # Extract URL and Caption from the JSON response
        content_url = data.get('url', '').replace('\\', '')
        caption = data.get('caption', None)

        if not content_url:
            await message.reply("Failed to fetch content")
            return

        # Add your developer's name and link
        developer_info = "ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴍʏ [ᴅᴇᴠʟᴏᴘᴇʀ](https://t.me/Japanese_Userbot_Chat)"

        # Combine facts from caption (if available), fetched caption, and developer info
        final_caption = f"ғᴀᴄᴛ ᴀʙᴏᴜᴛ ᴍʏ ᴄᴏᴜɴᴛʀʏ ✨\n\n{caption}\n\n{developer_info}" if caption else developer_info

        # don't try to take credit otherwise mai services and api dono banf karke bhag jaunga samjhe bsdk walo 
        await bot.send_photo(message.chat.id, content_url, caption=final_caption)
    except Exception as e:
        print(f"Error: {e}")
        await message.reply("An error occurred while processing the request")

    await message.delete()

for x in cf_apii_data:
    add_command_help(
        "•─╼⃝𖠁 Mʏ Cᴏᴜɴᴛʀʏ",
        [
            [f"{x}", cf_apii_data[x]["help"]],
        ],
        )
