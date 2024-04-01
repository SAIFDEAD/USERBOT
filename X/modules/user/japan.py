from aiohttp.client_exceptions import ClientError
from pyrogram import filters, Client 
from pyrogram.types import Message


from X.helpers.aiohttp_helper import AioHttp
from .help import * 

cf_apii_data = {
  "japan": {
        "url": "https://fantox-apis.vercel.app/horns",
        "help": "see my country's beauty !",
    }
}

texit_api_commands = []
for x in cf_apii_data:
    texit_api_commands.append(x)
    if "alts" in cf_apii_data[x]:
        for y in cf_apii_data[x]["alts"]:
            texit_api_commands.append(y)


@Client.on_message(
    filters.command(texit_api_commands, ".") & filters.me
)
async def japan_api(bot: Client, message: Message):
    cmd = message.command
    api_key = cmd[0]
    api = cf_apii_data[api_key]

    try:
        data = await AioHttp().get_json(api["url"])
        content_url: str = data['url']
        await bot.send_photo(message.chat.id, content_url)
    except ClientError as e:
        print(e)

    await message.delete()



for x in cf_apii_data:
    add_command_help(
        "•─╼⃝𖠁 ɴꜱғᴡ",
        [
            [f".{x}", cf_apii_data[x]["help"]],
        ],
    )
