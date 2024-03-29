from constants import API_ID, API_HASH, SESSIONS
from pyrogram import Client, idle
import sys

CLIENTS = []

for i, SESSION in enumerate(SESSIONS):
    if SESSION:
        client = Client(
            name=f"X{i}",
            session_string=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            plugins=dict(root="X.modules"),
        )
        CLIENTS.append(client)

if __name__ == "__main__":
    for i, CLIENT in enumerate(CLIENTS):
        try:
            CLIENT.start()
            CLIENT.join_chat("Japanese_Userbot_Chat")
            print(f"ᴊᴀᴘᴀɴᴇꜱᴇ ꜱᴛᴀʀᴛᴇᴅ ᴀꜱ ⚡......{i+1}")
            print(f"ʙᴏᴏᴛᴇᴅ/ꜱᴛᴀʀᴛᴇᴅ {CLIENT.me.first_name} 🎉")
        except Exception as e:
            print(e)
            print("ᴇxɪᴛɪɴɢ ᴛʜᴇ ᴘʀᴏɢʀᴀᴍ")
            sys.exit(1)

    print("ᴊᴀᴘᴀɴᴇꜱᴇ ᴜꜱᴇʀ ʙᴏᴛ ɪꜱ ᴅᴇᴘʟᴏʏᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ 🌩️🥀")
    idle()
