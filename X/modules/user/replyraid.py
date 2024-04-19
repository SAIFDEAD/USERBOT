from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from XDB.data import MASTERS, SDICTATOR
from config import OWNER_ID
from config import CMD_HANDLER as cmd
from .help import *
import asyncio
