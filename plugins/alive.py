import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("/start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/df6dd71fe22b4c51f8594.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
𝐈 𝐚𝐦 𝐭𝐡𝐞 𝐛𝐞𝐬𝐭 𝐌𝐮𝐬𝐢𝐜 𝐛𝐨𝐭🎵𝐨𝐟 𝐃𝐚𝐧𝐠𝐞𝐫𝐨𝐮𝐬𝐟𝐢𝐠𝐡𝐭𝐞𝐫𝐬💫

👉𝐃𝐚𝐧𝐠𝐞𝐫𝐨𝐮𝐬:[𝐌𝐀𝐈𝐍 𝐆𝐑𝐎𝐔𝐏](https://t.me/Dangerousfighters)
👉𝟖𝐱𝐨𝐟𝐟𝐢𝐜𝐢𝐚𝐥:[𝐃𝐔𝐒𝐑𝐀 𝐆𝐑𝐎𝐔𝐏](https://t.me/Clan8Xofficial)
👉𝐂𝐡𝐚𝐧𝐧𝐞𝐥:[𝐂𝐡𝐚𝐧𝐧𝐞𝐥](https://t.me/DANGEROUSFIGHTER)
👉𝐦𝐮𝐬𝐢𝐜 𝐰𝐨𝐫𝐥𝐝:[𝐂𝐡𝐚𝐭𝐭𝐢𝐧𝐠 𝐠𝐫𝐨𝐮𝐩](https://t.me/musicworld_ki_duniya)

𝐊𝐨𝐢 𝐢𝐬𝐬𝐮𝐞 𝐡𝐨 𝐭𝐨𝐡 𝐨𝐰𝐧𝐞𝐫 𝐤𝐨 𝐝𝐦 𝐤𝐚𝐫𝐢𝐲𝐨🤧 [𝐓𝐎𝐗𝐈𝐂](https://t.me/wtf_toxicop) ...
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "(𝐎𝐮𝐫 𝐂𝐡𝐚𝐧𝐧𝐞𝐥)😝", url=f"https://t.me/DANGEROUSFIGHTER")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "Toxic"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/df6dd71fe22b4c51f8594.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐒𝐔𝐏𝐏𝐎𝐑𝐓", url=f"https://t.me/Dangerousfighters")
                ]
            ]
        ),
    )


@Client.on_message(commandpro([ "/repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/df6dd71fe22b4c51f8594.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐎𝐖𝐍𝐄𝐑", url=f"https://t.me/wtf_toxicop")
                ]
            ]
        ),
    )
