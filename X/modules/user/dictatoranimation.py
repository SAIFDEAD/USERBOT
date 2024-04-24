import asyncio
import random

import requests
from pyrogram import *
from pyrogram import Client, filters
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram.types import *
from pyrogram.types import Message

from config import CMD_HANDLER
from X.helpers.basic import edit_or_reply, get_text
from X.helpers.constants import MEMES

from .help import * 


Client.on_message(filters.command(["demon"], cmd) & filters.me)
async def demon(client: Client, message: Message):
    await edit_or_reply(
        message,
       "⠛⠛⣿⣿⣿⣿⣿⡷⢶⣦⣶⣶⣤⣤⣤⣀\n"⠀⠀
 ⠀    ⠀"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷\n"⠀⠀
   ⠀⠀⠀"⠉⠉⠉⠙⠻⣿⣿⠿⠿⠛⠛⠛⠻⣿⣿⣇\n"⠀⠀
 ⠀   ⠀"⢤⣀⣀⣀⠀⠀⢸⣷⡄⠀⣁⣀⣤⣴⣿⣿⣿⣆\n"⠀⠀
 ⠀⠀⠀  ⠀"⠹⠏⠀⠀⠀⣿⣧⠀⠹⣿⣿⣿⣿⣿⡿⣿\n"⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀"⠛⠿⠇⢀⣼⣿⣿⠛⢯⡿⡟\n"⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"⠦⠴⢿⢿⣿⡿⠷⠀⣿\n"⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀"⠙⣷⣶⣶⣤⣤⣤⣤⣤⣶⣦⠃\n"⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⢐⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿\n"⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀\n"⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⠟⠁\n"⠀⠀
    )


@Client.on_message(filters.command(["sad"], cmd) & filters.me)
async def sad(client: Client, message: Message):
    await edit_or_reply(
        message,
      "  ⡏⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿\n"⠀⠀
       " ⣿⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⠀⣿\n"⠀⠀
       " ⁣⣿⣧⡀⠀⠀⠀⠀⠙⠿⠿⠿⠻⠿⠿⠟⠿⠛⠉⠀⠀⠀⠀⠀⣸⣿\n"⠀⠀
       " ⁣⣿⣿⣷⣄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿\n"⠀⠀
        ⁣"⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣴⣿⣿⣿⣿\n"⠀⠀
        ⁣"⣿⣿⣿⡟⠀⠀⢰⣹⡆⠀⠀⠀⠀⠀⠀⣭⣷⠀⠀⠀⠸⣿⣿⣿⣿\n"⠀⠀
       " ⁣⣿⣿⣿⠃⠀⠀⠈⠉⠀⠀⠤⠄⠀⠀⠀⠉⠁⠀⠀⠀⠀⢿⣿⣿⣿\n"⠀⠀
        "⁣⣿⣿⣿⢾⣿⣷⠀⠀⠀⠀⡠⠤⢄⠀⠀⠀⠠⣿⣿⣷⠀⢸⣿⣿⣿\n"⠀⠀
       " ⁣⣿⣿⣿⡀⠉⠀⠀⠀⠀⠀⢄⠀⢀⠀⠀⠀⠀⠉⠉⠁⠀⠀⣿⣿⣿\n"⠀⠀
       " ⁣⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿\n"⠀⠀
        "⁣⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿\n"⠀
        ⠀
        )


    

      
