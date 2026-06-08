# Don't Remove Credit Tg - @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "22983444"))
  API_HASH = os.environ.get("API_HASH", "12411a021f7efe77f9af8d6ed16b7b9b")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "8939436581:AAFtmpQchAFXJnVuyQrsebfUFtox8AAtZW4")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "WaguriFileBot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1003990627290"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "gplinks.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "540e6d65d2851a9c645d0eafb573535af3d33943")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "6341576569"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://botuser:ShadowNode_2026@cluster0.gcku8pz.mongodb.net/?appName=Cluster0")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1003971704016")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1003981196985"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [VJ](https://telegram.me/KingVj01)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/KingVj01)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
# --- GLOBAL AESTHETIC BYPASS ---
ANIME_IMAGES = [
    "https://images2.imgbox.com/39/fa/yK9I7Gcl_o.jpg",  # IMAGE_1
    "https://images2.imgbox.com/a9/63/0O7Gk5Z0_o.jpg",  # IMAGE_2
    "https://images2.imgbox.com/74/61/89WzZg0y_o.jpg"   # IMAGE_3
]

def global_font_bypass(text):
    if not text:
        return text
    normal_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small_caps   = "ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ"
    mapping = str.maketrans(normal_chars, small_caps)
    return text.translate(mapping)
  
