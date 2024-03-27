from aiohttp.client_exceptions import ClientError
from pyrogram import filters, Client 
from pyrogram.types import Message


from X.helpers.aiohttp_helper import AioHttp
from .help import *

cf_api_data = {
    "bikini": {
        "url": "https://fantox-apis.vercel.app/bikini",
        "help": ".",
    },
    "swimsuit": {
        "url": "https://fantox-apis.vercel.app/swimsuit",
        "help": " ",
    },
    "schoolswimsuit": {
        "url": "https://fantox-apis.vercel.app/schoolswimsuit",
        "help": ".",
    },
    "white": {
        "url": "https://fantox-apis.vercel.app/white",
        "help": ".",
    },
    "barefoot": {
        "url": "https://fantox-apis.vercel.app/barefoot",
        "help": ".",
    },
    "touhou": {
        "url": "https://fantox-apis.vercel.app/touhou",
        "help": ".",
    },
    "gamecg": {
        "url": "https://fantox-apis.vercel.app/gamecg",
        "help": ".",
    },
    "uncensored": {
        "url": "https://fantox-apis.vercel.app/uncensored",
        "help": "!",
    },
    "sunglasses": {
        "url": "https://fantox-apis.vercel.app/sunglasses",
        "help": "!",
    },
    "glasses": {
        "url": "https://fantox-apis.vercel.app/glasses",
        "help": "!",
    },
    "weapon": {
        "url": "https://fantox-apis.vercel.app/weapon",
        "help": "!",
    },
    "shirtlift": {
        "url": "https://fantox-apis.vercel.app/shirtlift",
        "help": "!",
    },
    "chain": {
        "url": "https://fantox-apis.vercel.app/chain",
        "help": "!",
    },
    "fingering": {
        "url": "https://fantox-apis.vercel.app/fingering",
        "help": "!",
    },
    "flatchest": {
        "url": "https://fantox-apis.vercel.app/flatchest",
        "help": "!",
    },
    "torncloth": {
        "url": "https://fantox-apis.vercel.app/torncloth",
        "help": "!",
    },
    "bondage": {
        "url": "https://fantox-apis.vercel.app/bondage",
        "help": ".",
    },
    "demon": {
        "url": "https://fantox-apis.vercel.app/demon",
        "help": ".",
    },
    "wet": {
        "url": "https://fantox-apis.vercel.app/wet",
        "help": ".",
    },
    "pantypull": {
        "url": "https://fantox-apis.vercel.app/pantypull",
        "help": ".",
    },
    "headdress": {
        "url": "https://fantox-apis.vercel.app/headdress",
        "help": ".",
    },
    "headphone": {
        "url": "https://fantox-apis.vercel.app/headphone",
        "help": "!",
    },
    "tie": {
        "url": "https://fantox-apis.vercel.app/tie",
        "help": "!",
    },
    "anusview": {
        "url": "https://fantox-apis.vercel.app/anusview",
        "help": "!",
    },
    "shorts": {
        "url": "https://fantox-apis.vercel.app/shorts",
        "help": "!",
    },
    "stokings": {
        "url": "https://fantox-apis.vercel.app/stokings",
        "help": "!",
    },
    "topless": {
        "url": "https://fantox-apis.vercel.app/topless",
        "help": "!",
    },
    "beach": {
        "url": "https://fantox-apis.vercel.app/beach",
        "help": "!",
    },
    "bunnygirl": {
        "url": "https://fantox-apis.vercel.app/bunnygirl",
        "help": "!",
    },
    "bunnyear": {
        "url": "https://fantox-apis.vercel.app/bunnyear",
        "help": "!",
    },
    "idol": {
        "url": "https://fantox-apis.vercel.app/idol",
        "help": "!",
    },
    "vampire": {
        "url": "https://fantox-apis.vercel.app/vampire",
        "help": "!",
    },
    "gun": {
        "url": "https://fantox-apis.vercel.app/gun",
        "help": "!",
    },
    "maid": {
        "url": "https://fantox-apis.vercel.app/maid",
        "help": "",
    },
    "hololive": {
        "url": "https://fantox-apis.vercel.app/hololive",
        "help": "",
    },
    "bra": {
        "url": "https://fantox-apis.vercel.app/bra",
        "help": ".",
    },
    "nobra": {
        "url": "https://fantox-apis.vercel.app/nobra",
        "help": "!",
    },
    "whitehair": {
        "url": "https://fantox-apis.vercel.app/whitehair",
        "help": "!",
    },
    "blonde": {
        "url": "https://fantox-apis.vercel.app/blonde",
        "help": "!",
    },
    "pinkhair": {
        "url": "https://fantox-apis.vercel.app/pinkhair",
        "help": "!",
    },
    "nude": {
        "url": "https://fantox-apis.vercel.app/nude",
        "help": "!",
    },
    "ponytail": {
        "url": "https://fantox-apis.vercel.app/ponytail",
        "help": "!",
    },
    "pinkhair": {
        "url": "https://fantox-apis.vercel.app/pinkhair",
        "help": "!",
    },
    "foxgirl": {
        "url": "https://fantox-apis.vercel.app/foxgirl",
        "help": "!",
    },
    "underwear": {
        "url": "https://fantox-apis.vercel.app/underwear",
        "help": "!",
    },
    "dress": {
        "url": "https://fantox-apis.vercel.app/dress",
        "help": "!",
    },
    "sex": {
        "url": "https://fantox-apis.vercel.app/sex",
        "help": "!",
    },
    "skirt": {
        "url": "https://fantox-apis.vercel.app/skirt",
        "help": ".",
    },
    "uniform": {
        "url": "https://fantox-apis.vercel.app/uniform",
        "help": "!",
    },
    "sex3": {
        "url": "https://fantox-apis.vercel.app/sex3",
        "help": "!",
    },
    "sex2": {
        "url": "https://fantox-apis.vercel.app/sex2",
        "help": "!",
    },
    "breast": {
        "url": "https://fantox-apis.vercel.app/breast",
        "help": "!",
    },
    "spreadpussy": {
        "url": "https://fantox-apis.vercel.app/spreadpussy",
        "help": "!",
    },
    "twintail": {
        "url": "https://fantox-apis.vercel.app/twintail",
        "help": "!",
    },
    "drunk": {
        "url": "https://fantox-apis.vercel.app/drunk",
        "help": "!",
    },
    "tears": {
        "url": "https://fantox-apis.vercel.app/tears",
        "help": ".",
    },
    "seethrough": {
        "url": "https://fantox-apis.vercel.app/seethrough",
        "help": ".!",
    },
    "breasthold": {
        "url": "https://fantox-apis.vercel.app/breasthold",
        "help": ".",
    },
    "fateseries": {
        "url": "https://fantox-apis.vercel.app/fateseries",
        "help": "!",
    },
    "spreadlegs": {
        "url": "https://fantox-apis.vercel.app/spreadlegs",
        "help": ".",
    },
    "openshirt": {
        "url": "https://fantox-apis.vercel.app/openshirt",
        "help": "!",
    },
    "headband": {
        "url": "https://fantox-apis.vercel.app/headband",
        "help": "!",
    },
    "food": {
        "url": "https://fantox-apis.vercel.app/food",
        "help": "!",
    },
    "close": {
        "url": "https://fantox-apis.vercel.app/close",
        "help": "!",
    },
    "tree": {
        "url": "https://fantox-apis.vercel.app/tree",
        "help": "!",
    },
    "nipples": {
        "url": "https://fantox-apis.vercel.app/nipples",
        "help": "!",
    },
    "erectnipples": {
        "url": "https://fantox-apis.vercel.app/erectnipples",
        "help": "!",
    },
    "greenhair": {
        "url": "https://fantox-apis.vercel.app/greenhair",
        "help": "!",
    },
    "catgirl": {
        "url": "https://fantox-apis.vercel.app/catgirl",
        "help": "!",
    },
    "wolfgirl": {
        "url": "https://fantox-apis.vercel.app/wolfgirl",
        "help": "!",
    },
    "horns": {
        "url": "https://fantox-apis.vercel.app/horns",
        "help": "!",
    }
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
        "•─╼⃝𖠁 ɴꜱғᴡ",
        [
            [f".{x}", cf_api_data[x]["help"]],
        ],
    )
