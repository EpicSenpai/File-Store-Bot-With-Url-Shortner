import datetime
import random
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import enums
from configs import Config
from handlers.database import Database

# Hamara font function import ya define kar lete hain
def global_font_bypass(text):
    # Agar bot.py mein function hai toh wahan se call ho raha hai, nahi toh normal text bypass na ho isliye ek safe fallback lagaya hai
    try:
        from bot import global_font_bypass as gfb
        return gfb(text)
    except:
        # Agar kisi wajah se import na ho toh small caps character mapping manually trigger ho jaye
        fonts = {"a": "ᴀ", "b": "ʙ", "c": "ᴄ", "d": "ᴅ", "e": "ᴇ", "f": "ꜰ", "g": "ɢ", "h": "ʜ", "i": "ɪ", "j": "ᴊ", "k": "ᴋ", "l": "ʟ", "m": "ᴍ", "n": "ɴ", "o": "ᴏ", "p": "ᴘ", "q": "ǫ", "r": "ʀ", "s": "s", "t": "ᴛ", "u": "ᴜ", "v": "ᴠ", "w": "ᴡ", "x": "x", "y": "ʏ", "z": "ᴢ"}
        return "".join([fonts.get(c.lower(), c) for c in text])

db = Database(Config.DATABASE_URL, Config.BOT_USERNAME)

async def handle_user_status(bot, cmd):
    chat_id = cmd.from_user.id
    if not await db.is_user_exist(chat_id):
        await db.add_user(chat_id)
        await bot.send_message(
            Config.LOG_CHANNEL,
            f"#NEW_USER: \n\nNew User [{cmd.from_user.first_name}](tg://user?id={chat_id}) started the bot!"
        )

    ban_status = await db.get_ban_status(chat_id)
    if ban_status["is_banned"]:
        if (datetime.date.today() - datetime.date.fromisoformat(ban_status["ban_date"])).days > ban_status["ban_duration"]:
            await db.remove_ban(chat_id)
        else:
            await cmd.reply_text("You R Banned!.. Contact @VJ_Botz 😂", quote=True)
            return

    # 🎯 AB YAHAN SE SAB KUCH BADAL DIYA HAI - NO AD, DIRECT LAYOUT!
    if cmd.text and (cmd.text == "/start" or cmd.text.strip().endswith("/start")):
        if getattr(Config, 'DYNAMIC_PICS', []):
            random_pic = random.choice(Config.DYNAMIC_PICS)
        elif getattr(Config, 'ANIME_IMAGES', []):
            random_pic = random.choice(Config.ANIME_IMAGES)
        else:
            random_pic = "AgACAgUAAxkBAAIBCmomuMz6BwjDucugc9M-qaPWrd2mAAKYEGsbwmI5VdvqQMJXubX0AAgBAAMCAAN4AAMeBA"

        raw_mention = f"hey!!, {cmd.from_user.first_name}"
        quote1 = f"**» {global_font_bypass(raw_mention)} ~ ❞**"
        
        raw_bio = "every light has its shadow, but every shadow can be turned into light..."
        quote2 = global_font_bypass(raw_bio)
        
        beautiful_caption = f"<blockquote>{quote1}</blockquote>\n\n<blockquote>{quote2}</blockquote>"
        
        await bot.send_photo(
            chat_id=cmd.chat.id,
            photo=random_pic,
            caption=beautiful_caption,
            parse_mode=enums.ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("• ꜰᴏʀ ᴍᴏʀᴇ •", url="https://t.me/+W0znQsN7HyAzNzUl")],
                [InlineKeyboardButton("• ᴀʙᴏᴜᴛ •", callback_data="aboutbot"), InlineKeyboardButton("• ᴄᴏᴍᴍᴀɴᴅꜱ •", callback_data="aboutdevs")]
            ])
        )
        return  # ⛔ Aage propagation ko yahin stop kar diya taaki ad trigger na ho sake!

    await cmd.continue_propagation()
    
