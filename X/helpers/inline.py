from math import ceil
from traceback import format_exc

from pyrogram.errors import MessageNotModified
from pyrogram.types import (
    InlineKeyboardButton,
    InlineQueryResultArticle,
    InputTextMessageContent,
)

from X import ids as list_users

looters = None


def paginate_help(page_number, loaded_modules, prefix):
    number_of_rows = 4
    number_of_cols = 2
    global looters
    looters = page_number
    helpable_modules = [p for p in loaded_modules if not p.startswith("_")]
    helpable_modules = sorted(helpable_modules)
    modules = [
        InlineKeyboardButton(
            text="{}".format(x),
            callback_data=f"ub_modul_{x}",
        )
        for x in helpable_modules
    ]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                InlineKeyboardButton(
                    text="•─╼⃝𖠁 ᴘʀᴇᴠɪᴏᴜꜱ", callback_data=f"{prefix}_prev({modulo_page})"
                ),
                InlineKeyboardButton(text="╼⃝𖠁 ᴄʟᴏꜱᴇ 𖠁⃝╾", callback_data="close_help"),
                InlineKeyboardButton(
                    text=" ɴᴇxᴛ 𖠁⃝╾─•", callback_data=f"{prefix}_next({modulo_page})"
                ),
            )
        ]
    return pairs


def cb_wrapper(func):
    async def wrapper(client, cb):
        users = list_users
        if cb.from_user.id not in users:
            await cb.answer(
                "𝐘𝐚𝐡𝐚𝐡𝐚𝐡𝐚 𝐘𝐨𝐮 𝐜𝐚𝐧'𝐭 𝐝𝐨 𝐢𝐭 𝐢𝐟 𝐲𝐨𝐮 𝐰𝐚𝐧𝐭 𝐭𝐨 𝐬𝐞𝐞 𝐢𝐭 𝐚𝐧𝐝 𝐦𝐚𝐤𝐞 𝐢𝐭 𝐲𝐨𝐮𝐫𝐬𝐞𝐥𝐟 𝐉𝐀𝐏𝐀𝐍𝐄𝐒𝐄 𝐗 𝐔𝐒𝐄𝐑𝐁𝐎𝐓",
                cache_time=0,
                show_alert=True,
            )
        else:
            try:
                await func(client, cb)
            except MessageNotModified:
                await cb.answer("🤔🧐")
            except Exception:
                print(format_exc())
                await cb.answer(
                    f"𝐎𝐡 𝐍𝐨, 𝐈𝐭 𝐋𝐨𝐨𝐤𝐬 𝐋𝐢𝐤𝐞 𝐓𝐡𝐞𝐫𝐞'𝐬 𝐀 𝐏𝐫𝐨𝐛𝐥𝐞𝐦 𝐆𝐨𝐢𝐧𝐠 𝐎𝐧 𝐍𝐨𝐰. 𝐏𝐥𝐞𝐚𝐬𝐞 𝐜𝐡𝐞𝐜𝐤 𝐭𝐡𝐞 𝐥𝐨𝐠𝐬!",
                    cache_time=0,
                    show_alert=True,
                )

    return wrapper


def inline_wrapper(func):
    async def wrapper(client, inline_query):
        users = list_users
        if inline_query.from_user.id not in users:
            await client.answer_inline_query(
                inline_query.id,
                cache_time=1,
                results=[
                    (
                        InlineQueryResultArticle(
                            title="𝐒𝐨𝐫𝐫𝐲, 𝐘𝐨𝐮 𝐌𝐮𝐬𝐭 𝐁𝐞 𝐀 𝐒𝐮𝐝𝐨 𝐔𝐬𝐞𝐫 𝐓𝐨 𝐔𝐬𝐞 𝐌𝐞!",
                            input_message_content=InputTextMessageContent(
                                "𝐎𝐫 𝐲𝐨𝐮 𝐜𝐚𝐧 𝐦𝐚𝐤𝐞 𝐢𝐭 𝐲𝐨𝐮𝐫𝐬𝐞𝐥𝐟 𝐚𝐭 @Japanese_Userbot"
                            ),
                        )
                    )
                ],
            )
        else:
            await func(client, inline_query)

    return wrapper
