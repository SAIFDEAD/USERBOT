from pyrogram import Client, enums, filters
from pyrogram.types import Message
from sqlalchemy.exc import IntegrityError

from config import CMD_HANDLER
from X import TEMP_SETTINGS
from X.helpers.adminHelpers import DEVS
from X.helpers.basic import edit_or_reply
from X.helpers.SQL.globals import addgvar, gvarstatus
from X.helpers.tools import get_arg

from .help import *

DEF_UNAPPROVED_MSG =  (
    """
╔═════════════════════╗
│✥Hᴇʟʟᴏ sɪʀ ᴍʏsᴇʟғ Jᴀᴘᴀɴᴇsᴇ-X-Usᴇʀʙᴏᴛ✥ㅤ  ㅤ   
╚═════════════════════╝
⍟ Dᴏɴ'ᴛ Uɴᴅᴇʀ Esᴛɪᴍᴀᴛᴇ ᴍᴇ
⍟ Mʏ Mᴀsᴛᴇʀ ɪs ʙᴜsʏ ʀɪɢʜᴛ ɴᴏᴡ
⍟ Mʏ Mᴀsᴛᴇʀ ʜᴀs ᴀssɪɢɴᴇᴅ ᴍᴇ ᴛʜᴇ ᴅᴜᴛʏ ᴛᴏ ᴋᴇᴇᴘ ᴀ ᴄʜᴇᴄᴋ ᴏɴ ʜɪs PM
⍟ Iғ ᴜ Sᴘᴀᴍ, ᴏʀ ᴛʀɪᴇᴅ ᴀɴʏᴛʜɪɴɢ ғᴜɴɴʏ, I'ᴠᴇ ғᴜʟʟ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ Bʟᴏᴄᴋ + Rᴇᴘᴏʀᴛ ʏᴏᴜ ᴀs Sᴘᴀᴍ ɪɴ Tᴇʟᴇɢʀᴀᴍ's sᴇʀᴠᴇʀ
⍟ Sᴏ ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ᴅɪsᴛᴜʀʙ ʜɪᴍ
⍟ Bᴇᴛᴛᴇʀ ʙᴇ ᴄᴀʀᴇғᴜʟ
╔═════════════════════╗
│ㅤㅤ✥ Pᴏᴡᴇʀᴇᴅ ʙʏ ✥ㅤ      
│ㅤㅤ✥ Jᴀᴘᴀɴᴇsᴇ-X-Usᴇʀʙᴏᴛ ✥ 
╚═════════════════════╝
"""
)


@Client.on_message(
    ~filters.me & filters.private & ~filters.bot & filters.incoming, group=69
)
async def incomingpm(client: Client, message: Message):
    try:
        from X.helpers.SQL.globals import gvarstatus
        from X.helpers.SQL.pm_permit_sql import is_approved
    except BaseException:
        pass

    if gvarstatus("PMPERMIT") and gvarstatus("PMPERMIT") == "false":
        return
    if await auto_accept(client, message) or message.from_user.is_self:
        message.continue_propagation()
    if message.chat.id != 777000:
        PM_LIMIT = gvarstatus("PM_LIMIT") or 5
        getmsg = gvarstatus("unapproved_msg")
        if getmsg is not None:
            UNAPPROVED_MSG = getmsg
        else:
            UNAPPROVED_MSG = DEF_UNAPPROVED_MSG

        apprv = is_approved(message.chat.id)
        if not apprv and message.text != UNAPPROVED_MSG:
            if message.chat.id in TEMP_SETTINGS["PM_LAST_MSG"]:
                prevmsg = TEMP_SETTINGS["PM_LAST_MSG"][message.chat.id]
                if message.text != prevmsg:
                    async for message in client.search_messages(
                        message.chat.id,
                        from_user="me",
                        limit=10,
                        query=UNAPPROVED_MSG,
                    ):
                        await message.delete()
                    if TEMP_SETTINGS["PM_COUNT"][message.chat.id] < (int(PM_LIMIT) - 1):
                        ret = await message.reply_text(UNAPPROVED_MSG)
                        TEMP_SETTINGS["PM_LAST_MSG"][message.chat.id] = ret.text
            else:
                ret = await message.reply_text(UNAPPROVED_MSG)
                if ret.text:
                    TEMP_SETTINGS["PM_LAST_MSG"][message.chat.id] = ret.text
            if message.chat.id not in TEMP_SETTINGS["PM_COUNT"]:
                TEMP_SETTINGS["PM_COUNT"][message.chat.id] = 1
            else:
                TEMP_SETTINGS["PM_COUNT"][message.chat.id] = (
                    TEMP_SETTINGS["PM_COUNT"][message.chat.id] + 1
                )
            if TEMP_SETTINGS["PM_COUNT"][message.chat.id] > (int(PM_LIMIT) - 1):
                await message.reply("**Sorry, you have been blocked due to spam chat**")
                try:
                    del TEMP_SETTINGS["PM_COUNT"][message.chat.id]
                    del TEMP_SETTINGS["PM_LAST_MSG"][message.chat.id]
                except BaseException:
                    pass

                await client.block_user(message.chat.id)

    message.continue_propagation()


async def auto_accept(client, message):
    try:
        from X.helpers.SQL.pm_permit_sql import approve, is_approved
    except BaseException:
        pass

    if message.chat.id in DEVS:
        try:
            approve(message.chat.id)
            await client.send_message(
                message.chat.id,
                f"<b>Receiving Messages!!!</b>\n{message.from_user.mention} <b>Developer Detected Japanese-X-Userbot🔥</b>",
                parse_mode=enums.ParseMode.HTML,
            )
        except IntegrityError:
            pass
    if message.chat.id not in [client.me.id, 777000]:
        if is_approved(message.chat.id):
            return True

        async for msg in client.get_chat_history(message.chat.id, limit=1):
            if msg.from_user.id == client.me.id:
                try:
                    del TEMP_SETTINGS["PM_COUNT"][message.chat.id]
                    del TEMP_SETTINGS["PM_LAST_MSG"][message.chat.id]
                except BaseException:
                    pass

                try:
                    approve(chat.id)
                    async for message in client.search_messages(
                        message.chat.id,
                        from_user="me",
                        limit=10,
                        query=UNAPPROVED_MSG,
                    ):
                        await message.delete()
                    return True
                except BaseException:
                    pass

    return False


@Client.on_message(
    filters.command(["ok", "setuju", "approve"], cmd) & filters.me & filters.private
)
async def approvepm(client: Client, message: Message):
    try:
        from X.helpers.SQL.pm_permit_sql import approve
    except BaseException:
        await message.edit("Running on Non-SQL mode!")
        return

    if message.reply_to_message:
        reply = message.reply_to_message
        replied_user = reply.from_user
        if replied_user.is_self:
            await message.edit("You can't approve of yourself.")
            return
        aname = replied_user.id
        name0 = str(replied_user.first_name)
        uid = replied_user.id
    else:
        aname = message.chat
        if not aname.type == enums.ChatType.PRIVATE:
            await message.edit(
                "You're not currently in PM and you haven't replied to someone's message."
            )
            return
        name0 = aname.first_name
        uid = aname.id

    try:
        approve(uid)
        await message.edit(f"**Receiving Messages From** [{name0}](tg://user?id={uid})!")
    except IntegrityError:
        await message.edit(
            f"[{name0}](tg://user?id={uid}) may have been approved for PM."
        )
        return


@Client.on_message(
    filters.command(["tolak", "nopm", "disapprove"], cmd) & filters.me & filters.private
)
async def disapprovepm(client: Client, message: Message):
    try:
        from Uputt.helpers.SQL.pm_permit_sql import dissprove
    except BaseException:
        await message.edit("Running on Non-SQL mode!")
        return

    if message.reply_to_message:
        reply = message.reply_to_message
        replied_user = reply.from_user
        if replied_user.is_self:
            await message.edit("You can't deny yourself.")
            return
        aname = replied_user.id
        name0 = str(replied_user.first_name)
        uid = replied_user.id
    else:
        aname = message.chat
        if not aname.type == enums.ChatType.PRIVATE:
            await message.edit(
                "You're not currently in PM and you haven't replied to someone's message."
            )
            return
        name0 = aname.first_name
        uid = aname.id

    dissprove(uid)

    await message.edit(
        f"**Message** [{name0}](tg://user?id={uid}) **Has been Rejected, Please Do Not Do It Spam Chat!**"
    )


@Client.on_message(filters.command("pmlimit", cmd) & filters.me)
async def setpm_limit(client: Client, cust_msg: Message):
    if gvarstatus("PMPERMIT") and gvarstatus("PMPERMIT") == "false":
        return await cust_msg.edit(
            f"**You Have To Set Var** `PM_AUTO_BAN` **When** `True`\n\n**If you want to activate PMPERMIT Please Type:** `{cmd}setvar PM_AUTO_BAN True`"
        )
    try:
        from X.helpers.SQL.globals import addgvar
    except AttributeError:
        await cust_msg.edit("**Running on Non-SQL mode!**")
        return
    input_str = (
        cust_msg.text.split(None, 1)[1]
        if len(
            cust_msg.command,
        )
        != 1
        else None
    )
    if not input_str:
        return await cust_msg.edit("**Please enter a number for PM_LIMIT.**")
    X = await cust_msg.edit("`Processing...`")
    if input_str and not input_str.isnumeric():
        return await X.edit("**Please enter a number for PM_LIMIT.**")
    addgvar("PM_LIMIT", input_str)
    await X.edit(f"**Set PM limit to** `{input_str}`")


@Client.on_message(filters.command(["pmpermit", "pmguard"], cmd) & filters.me)
async def onoff_pmpermit(client: Client, message: Message):
    input_str = get_arg(message)
    if input_str == "off":
        h_type = False
    elif input_str == "on":
        h_type = True
    if gvarstatus("PMPERMIT") and gvarstatus("PMPERMIT") == "false":
        PMPERMIT = False
    else:
        PMPERMIT = True
    if PMPERMIT:
        if h_type:
            await edit_or_reply(message, "**PMPERMIT Already Activated**")
        else:
            addgvar("PMPERMIT", h_type)
            await edit_or_reply(message, "**PMPERMIT Shutdown Successfully**")
    elif h_type:
        addgvar("PMPERMIT", h_type)
        await edit_or_reply(message, "**PMPERMIT Activated Successfully**")
    else:
        await edit_or_reply(message, "**PMPERMIT It's Turned Off**")


@Client.on_message(filters.command("setpmpermit", cmd) & filters.me)
async def stpmpt(client: Client, cust_msg: Message):
    """Set your own Unapproved message"""
    if gvarstatus("PMPERMIT") and gvarstatus("PMPERMIT") == "false":
        return await cust_msg.edit(
            "**You Have To Tune In Var** `PM_AUTO_BAN` **When** `True`\n\n**If you want to activate PMPERMIT Please Type:** `.setvar PM_AUTO_BAN True`"
        )
    try:
        import X.helpers.SQL.globals as sql
    except AttributeError:
        await cust_msg.edit("**Running on Non-SQL mode!**")
        return
    X = await cust_msg.edit("`Processing...`")
    custom_message = sql.gvarstatus("unapproved_msg")
    message = cust_msg.reply_to_message
    if custom_message is not None:
        sql.delgvar("unapproved_msg")
    if not message:
        return await X.edit("**Please reply to the message**")
    msg = message.text
    sql.addgvar("unapproved_msg", msg)
    await X.edit("**Message Successfully Saved to Chat Roomt**")


@Client.on_message(filters.command("getpmpermit", cmd) & filters.me)
async def gtpmprmt(client: Client, cust_msg: Message):
    if gvarstatus("PMPERMIT") and gvarstatus("PMPERMIT") == "false":
        return await cust_msg.edit(
            "**You Have To Tune In Var** `PM_AUTO_BAN` **When** `True`\n\n**If you want to activate PMPERMIT Please Type:** `.setvar PM_AUTO_BAN True`"
        )
    try:
        import X.helpers.SQL.globals as sql
    except AttributeError:
        await cust_msg.edit("**Running on Non-SQL mode!**")
        return
    X = await cust_msg.edit("`Processing...`")
    custom_message = sql.gvarstatus("unapproved_msg")
    if custom_message is not None:
        await X.edit("**Order PMPERMIT Now:**" f"\n\n{custom_message}")
    else:
        await X.edit(
            "**You Have Not Set PMPERMIT Custom Message,**\n"
            f"**Still Using Default PM Message:**\n\n{DEF_UNAPPROVED_MSG}"
        )


@Client.on_message(filters.command("rtpprt", cmd) & filters.me)
async def gtpmprmt(client: Client, cust_msg: Message):
    if gvarstatus("PMPERMIT") and gvarstatus("PMPERMIT") == "false":
        return await cust_msg.edit(
            f"**You Have To Tune In Var** `PM_AUTO_BAN` **when** `True`\n\n**If you want to activate PMPERMIT, please type:** `{cmd}setvar PM_AUTO_BAN True`"
        )
    try:
        import X.helpers.SQL.globals as sql
    except AttributeError:
        await cust_msg.edit("**Running on Non-SQL mode!**")
        return
    X = await cust_msg.edit("`Processing...`")
    custom_message = sql.gvarstatus("unapproved_msg")

    if custom_message is None:
        await X.edit("**Your PMPERMIT message is already default**")
    else:
        sql.delgvar("unapproved_msg")
        await X.edit("**Successfully Changed PMPERMIT Custom Message to Default**")


add_command_help(
    "•─╼⃝𖠁 ᴘᴍᴘᴇʀᴍɪᴛ",
    [
        [
            f"ok ᴏʀ {cmd}setuju",
            "Rᴇᴄᴇɪᴠᴇ ꜱᴏᴍᴇᴏɴᴇ'ꜱ ᴍᴇꜱꜱᴀɢᴇ ʙʏ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴛʜᴇɪʀ ᴍᴇꜱꜱᴀɢᴇ ᴏʀ ᴛᴀɢꜱ ᴀɴᴅ ᴀʟꜱᴏ ᴛᴏ ᴅᴏ ɪɴ ᴘᴍ",
        ],
        [
            f"minus ᴏʀ {cmd}nopm",
            "Rᴇɪᴇᴄᴛ ꜱᴏᴍᴇᴏɴᴇ'ꜱ ᴍᴇꜱꜱᴀɢᴇ ʙʏ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ ᴏʀ ᴛᴀɢꜱ ᴀɴᴅ ᴀʟꜱᴏ ᴛᴏ ᴅᴏ ɪɴ ᴘᴍ",
        ],
        [
            "pmlimit <ɴᴜᴍʙᴇʀ>",
            "Tᴏ ᴄᴜꜱᴛᴏᴍɪᴢᴇ ᴛʜᴇ ᴀᴜᴛᴏ ʙʟᴏᴄᴋ ᴍᴇꜱꜱᴀɢᴇ ʟɪᴍɪᴛ ᴍᴇꜱꜱᴀɢᴇ",
        ],
        [
            "pmpermit ᴏɴ/ᴏғғ",
            "Tᴏ ᴇɴᴀʙʟᴇ ᴏʀ ᴅɪꜱᴀʙʟᴇ PMPERMIT",
        ],
    ],
)