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
    "swimsuit": {
        "url": "https://fantox-apis.vercel.app/swimsuit",
        "help": "It works on my machine!",
    },
    "schoolswimsuit": {
        "url": "https://fantox-apis.vercel.app/schoolswimsuit",
        "help": "It works on my machine!",
    },
    "white": {
        "url": "https://fantox-apis.vercel.app/white",
        "help": "It works on my machine!",
    },
    "barefoot": {
        "url": "https://fantox-apis.vercel.app/barefoot",
        "help": "It works on my machine!",
    },
    "touhou": {
        "url": "https://fantox-apis.vercel.app/touhou",
        "help": "It works on my machine!",
    },
    "gamecg": {
        "url": "https://fantox-apis.vercel.app/gamecg",
        "help": "It works on my machine!",
    },
    "uncensored": {
        "url": "https://fantox-apis.vercel.app/uncensored",
        "help": "It works on my machine!",
    },
    "sunglasses": {
        "url": "https://fantox-apis.vercel.app/sunglasses",
        "help": "It works on my machine!",
    },
    "glasses": {
        "url": "https://fantox-apis.vercel.app/glasses",
        "help": "It works on my machine!",
    },
    "weapon": {
        "url": "https://fantox-apis.vercel.app/weapon",
        "help": "It works on my machine!",
    },
    "shirtlift": {
        "url": "https://fantox-apis.vercel.app/shirtlift",
        "help": "It works on my machine!",
    },
    "chain": {
        "url": "https://fantox-apis.vercel.app/chain",
        "help": "It works on my machine!",
    },
    "fingering": {
        "url": "https://fantox-apis.vercel.app/fingering",
        "help": "It works on my machine!",
    },
    "flatchest": {
        "url": "https://fantox-apis.vercel.app/flatchest",
        "help": "It works on my machine!",
    },
    "torncloth": {
        "url": "https://fantox-apis.vercel.app/torncloth",
        "help": "It works on my machine!",
    },
    "bondage": {
        "url": "https://fantox-apis.vercel.app/bondage",
        "help": "It works on my machine!",
    },
    "demon": {
        "url": "https://fantox-apis.vercel.app/demon",
        "help": "It works on my machine!",
    },
    "wet": {
        "url": "https://fantox-apis.vercel.app/wet",
        "help": "It works on my machine!",
    },
    "pantypull": {
        "url": "https://fantox-apis.vercel.app/pantypull",
        "help": "It works on my machine!",
    },
    "headdress": {
        "url": "https://fantox-apis.vercel.app/headdress",
        "help": "It works on my machine!",
    },
    "headphone": {
        "url": "https://fantox-apis.vercel.app/headphone",
        "help": "It works on my machine!",
    },
    "tie": {
        "url": "https://fantox-apis.vercel.app/tie",
        "help": "It works on my machine!",
    },
    "anusview": {
        "url": "https://fantox-apis.vercel.app/anusview",
        "help": "It works on my machine!",
    },
    "shorts": {
        "url": "https://fantox-apis.vercel.app/shorts",
        "help": "It works on my machine!",
    },
    "stokings": {
        "url": "https://fantox-apis.vercel.app/stokings",
        "help": "It works on my machine!",
    },
    "topless": {
        "url": "https://fantox-apis.vercel.app/topless",
        "help": "It works on my machine!",
    },
    "beach": {
        "url": "https://fantox-apis.vercel.app/beach",
        "help": "It works on my machine!",
    },
    "bunnygirl": {
        "url": "https://fantox-apis.vercel.app/bunnygirl",
        "help": "It works on my machine!",
    },
    "bunnyear": {
        "url": "https://fantox-apis.vercel.app/bunnyear",
        "help": "It works on my machine!",
    },
    "idol": {
        "url": "https://fantox-apis.vercel.app/idol",
        "help": "It works on my machine!",
    },
    "vampire": {
        "url": "https://fantox-apis.vercel.app/vampire",
        "help": "It works on my machine!",
    },
    "gun": {
        "url": "https://fantox-apis.vercel.app/gun",
        "help": "It works on my machine!",
    },
    "maid": {
        "url": "https://fantox-apis.vercel.app/maid",
        "help": "It works on my machine!",
    },
    "hololive": {
        "url": "https://fantox-apis.vercel.app/hololive",
        "help": "It works on my machine!",
    },
    "bra": {
        "url": "https://fantox-apis.vercel.app/bra",
        "help": "It works on my machine!",
    },
    "nobra": {
        "url": "https://fantox-apis.vercel.app/nobra",
        "help": "It works on my machine!",
    },
    "whitehair": {
        "url": "https://fantox-apis.vercel.app/whitehair",
        "help": "It works on my machine!",
    },
    "blonde": {
        "url": "https://fantox-apis.vercel.app/blonde",
        "help": "It works on my machine!",
    },
    "pinkhair": {
        "url": "https://fantox-apis.vercel.app/pinkhair",
        "help": "It works on my machine!",
    },
    "nude": {
        "url": "https://fantox-apis.vercel.app/nude",
        "help": "It works on my machine!",
    },
    "ponytail": {
        "url": "https://fantox-apis.vercel.app/ponytail",
        "help": "It works on my machine!",
    },
    "pinkhair": {
        "url": "https://fantox-apis.vercel.app/pinkhair",
        "help": "It works on my machine!",
    },
    "foxgirl": {
        "url": "https://fantox-apis.vercel.app/foxgirl",
        "help": "It works on my machine!",
    },
    "underwear": {
        "url": "https://fantox-apis.vercel.app/underwear",
        "help": "It works on my machine!",
    },
    "dress": {
        "url": "https://fantox-apis.vercel.app/dress",
        "help": "It works on my machine!",
    },
    "sex": {
        "url": "https://fantox-apis.vercel.app/sex",
        "help": "It works on my machine!",
    },
    "skirt": {
        "url": "https://fantox-apis.vercel.app/skirt",
        "help": "It works on my machine!",
    },
    "uniform": {
        "url": "https://fantox-apis.vercel.app/uniform",
        "help": "It works on my machine!",
    },
    "sex3": {
        "url": "https://fantox-apis.vercel.app/sex3",
        "help": "It works on my machine!",
    },
    "sex2": {
        "url": "https://fantox-apis.vercel.app/sex2",
        "help": "It works on my machine!",
    },
    "breast": {
        "url": "https://fantox-apis.vercel.app/breast",
        "help": "It works on my machine!",
    },
    "spreadpussy": {
        "url": "https://fantox-apis.vercel.app/spreadpussy",
        "help": "It works on my machine!",
    },
    "twintail": {
        "url": "https://fantox-apis.vercel.app/twintail",
        "help": "It works on my machine!",
    },
    "drunk": {
        "url": "https://fantox-apis.vercel.app/drunk",
        "help": "It works on my machine!",
    },
    "tears": {
        "url": "https://fantox-apis.vercel.app/tears",
        "help": "It works on my machine!",
    },
    "seethrough": {
        "url": "https://fantox-apis.vercel.app/seethrough",
        "help": "It works on my machine!",
    },
    "breasthold": {
        "url": "https://fantox-apis.vercel.app/breasthold",
        "help": "It works on my machine!",
    },
    "fateseries": {
        "url": "https://fantox-apis.vercel.app/fateseries",
        "help": "It works on my machine!",
    },
    "spreadlegs": {
        "url": "https://fantox-apis.vercel.app/spreadlegs",
        "help": "It works on my machine!",
    },
    "openshirt": {
        "url": "https://fantox-apis.vercel.app/openshirt",
        "help": "It works on my machine!",
    },
    "headband": {
        "url": "https://fantox-apis.vercel.app/headband",
        "help": "It works on my machine!",
    },
    "food": {
        "url": "https://fantox-apis.vercel.app/food",
        "help": "It works on my machine!",
    },
    "close": {
        "url": "https://fantox-apis.vercel.app/close",
        "help": "It works on my machine!",
    },
    "tree": {
        "url": "https://fantox-apis.vercel.app/tree",
        "help": "It works on my machine!",
    },
    "nipples": {
        "url": "https://fantox-apis.vercel.app/nipples",
        "help": "It works on my machine!",
    },
    "erectnipples": {
        "url": "https://fantox-apis.vercel.app/erectnipples",
        "help": "It works on my machine!",
    },
    "greenhair": {
        "url": "https://fantox-apis.vercel.app/greenhair",
        "help": "It works on my machine!",
    },
    "catgirl": {
        "url": "https://fantox-apis.vercel.app/catgirl",
        "help": "It works on my machine!",
    },
    "wolfgirl": {
        "url": "https://fantox-apis.vercel.app/wolfgirl",
        "help": "It works on my machine!",
    },
    "horns": {
        "url": "https://fantox-apis.vercel.app/horns",
        "help": "It works on my machine!",
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
            ["`.genshin` `.swimsuit` `.schoolswimsuit` `.white` `.barefoot` `.touhou` `.gamecg` `.hololive` `.uncensored` `.sunglasses` `.glasses` `.weapon` `.shirtlift` `.chain` `.fingering` `.flatchest` `.torncloth` `.bondage` `.demon` `.wet` `.pantypull` `.headdress` `.headphone` `.tie` `.anusview` `.shorts` `.stokings` `.topless` `.beach` `.bunnygirl` `.bunnyear` `.idol` `.vampire` `.gun` `.maid` `.bra` `.nobra` `.bikini` `.whitehair` `.blonde` `.pinkhair` `.bed` `.ponytail` `.nude` `.dress` `.underwear` `.foxgirl` `.uniform` `.skirt` `.sex` `.sex2` `.sex3` `.breast` `.twintail` `.spreadpussy` `.tears` `.seethrough` `.breasthold` `.drunk` `.fateseries` `.spreadlegs` `.openshirt` `.headband` `.food` `.close` `.tree` `.nipples` `.erectnipples` `.horns` `.greenhair` `.wolfgirl` `.catgirl`"],
        ],
    )
