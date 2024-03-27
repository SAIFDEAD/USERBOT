from aiohttp.client_exceptions import ClientError
from pyrogram import filters, Client 
from pyrogram.types import Message


from X.helpers.aiohttp_helper import AioHttp
from .help import *

cf_api_data = {
    "bikini": {
        "url": "https://fantox-apis.vercel.app/bikini",
        "help": "It works on my machine!",
    },
    "hentai": {
        "url": "https://fantox-apis.vercel.app/catgirl",
        "help": "Sends a nice compliment.",
    },
    "yuri": {
        "url": "https://fantox-apis.vercel.app/yuri",
        "help": "Affirmative messages",
    },
    "dva": {
        "url": "https://fantox-apis.vercel.app/dva",
        "help": "Affirmative messages",
    },
    "trap": {
        "url": "https://fantox-apis.vercel.app/trap",
        "help": "Affirmative messages",
    },
    "hug": {
        "url": "https://fantox-apis.vercel.app/hug",
        "help": "Give it a guess dumbass!",
    },
    "neko": {
        "url": "https://fantox-apis.vercel.app/neko",
        "format": "Kanye once said:\n`{}`",
        "help": "Kanye used to say",
    },
    "nsfwneko": {
        "url": "https://fantox-apis.vercel.app/nsfwneko",
        "help": "Programmers be like.",
    },
    "baguette": {
        "url": "https://fantox-apis.vercel.app/baguette",
        "help": "Affirmative messages",
    },
}

text_api_commands = []
for x in cf_api_data:
    text_api_commands.append(x)
    if "alts" in cf_api_data[x]:
        for y in cf_api_data[x]["alts"]:
            text_api_commands.append(y)


@Client.on_message(
    filters.command(text_api_commands, ".") & filters.me
)
async def hentai_api(bot: Client, message: Message):
    cmd = message.command
    api_key = cmd[0]
    api = cf_api_data[api_key]

    try:
        data = await AioHttp().get_json(api["url"])
        content_url: str = data['url']
        await bot.send_photo(message.chat.id, content_url)
    except ClientError as e:
        print(e)

    await message.delete()



for x in cf_api_data:
    add_command_help(
        "anime_cf",
        [
            [f".{x}", cf_api_data[x]["help"]],
        ],
    )
