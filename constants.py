import os
from dotenv import load_dotenv
from XDB.data import MASTERS

# Load environment variables from config.env file
load_dotenv("config.env")

# Bot configuration constants
ALIVE_EMOJI = os.getenv("ALIVE_EMOJI", "🥵")
ALIVE_LOGO = os.getenv("ALIVE_LOGO", "https://graph.org/file/ec99cb6dba229bd984537.jpg")
ALIVE_TEKS_CUSTOM = os.getenv("ALIVE_TEKS_CUSTOM", "Hey, I am alive.")
API_HASH = os.getenv("API_HASH", "34efb38c74d5e6b25d1bb6234396a8af")
API_ID = os.getenv("API_ID", "23129036")
BOTLOG_CHATID = int(os.getenv("BOTLOG_CHATID", 0))
BOT_VER = "3.0.0@main"
BRANCH = os.getenv("BRANCH", "main")  # Don't change this line
CMD_HNDLR = os.getenv("CMD_HANDLER", ".")
OWNER_ID = os.getenv("OWNER_ID", "6694740726")
BOT_TOKEN = os.getenv("BOT_TOKEN", "none")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
CHANNEL = os.getenv("CHANNEL", "Japanese_Userbot")
CMD_HANDLER = os.getenv("CMD_HANDLER", ".")
GIT_TOKEN = os.getenv("GIT_TOKEN", "")
GROUP = os.getenv("GROUP", "Japanese_Userbot_Chat")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
REPO_URL = os.getenv("REPO_URL", "https://github.com/Team-Japanese/Japanese-X-Userbot")

# String session constants
STRING_SESSION1 = os.getenv("STRING_SESSION1", "")
STRING_SESSION2 = os.getenv("STRING_SESSION2", "")
STRING_SESSION3 = os.getenv("STRING_SESSION3", "")
STRING_SESSION4 = os.getenv("STRING_SESSION4", "")
STRING_SESSION5 = os.getenv("STRING_SESSION5", "")
STRING_SESSION6 = os.getenv("STRING_SESSION6", "")
STRING_SESSION7 = os.getenv("STRING_SESSION7", "")
STRING_SESSION8 = os.getenv("STRING_SESSION8", "")
STRING_SESSION9 = os.getenv("STRING_SESSION9", "")
STRING_SESSION10 = os.getenv("STRING_SESSION10", "")

# List of string sessions
SESSIONS = [
    STRING_SESSION1,
    STRING_SESSION2,
    STRING_SESSION3,
    STRING_SESSION4,
    STRING_SESSION5,
    STRING_SESSION6,
    STRING_SESSION7,
    STRING_SESSION8,
    STRING_SESSION9,
    STRING_SESSION10
]

# Sudo users constants
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "").split()))
BLACKLIST_CHAT = os.getenv("BLACKLIST_CHAT", "-1001608701614 -1001675459127 -1001473548283 -1001608701614")
BLACKLIST_GCAST = set(map(int, os.getenv("BLACKLIST_GCAST", "").split()))

# Add OWNER_ID and MASTERS to SUDO_USERS list
SUDO_USERS.extend([int(OWNER_ID)] + [int(master) for master in os.getenv("MASTERS", "").split() if master])
