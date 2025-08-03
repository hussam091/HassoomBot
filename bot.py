from pyrogram import Client, filters
from pyrogram.types import Message
import random

API_ID = 22663587
API_HASH = "f260cacdecbf1c5a241d068a734c3b69"
BOT_TOKEN = "8427928027:AAErywytpNELFkGIICFUf92fLC9ymb3Efo4"

app = Client("hassoom_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

replies = {
    "مرحبا": ["هلا نورت", "أهلين بالغالي", "مرحبتين بحسوم"],
    "شلونك": ["تمام وانت؟", "بخير اذا انت بخير", "منور يا طيب"],
    "هاا": ["هااا وينك", "هاا شتسوي؟"],
    "احبك": ["اني اكثر", "حبك مدمر", "احبك موت"],
}

@app.on_message(filters.command("كت") & filters.group)
def game_ktk(client, message: Message):
    words = ["شمس", "قمر", "نجمة", "نهر", "ورد", "فرح", "حياة"]
    word = random.choice(words)
    message.reply_text(f"اكتب الكلمة التالية بسرعة:\n`{word}`")

@app.on_message(filters.command("الفلوس") & filters.group)
def money_game(client, message: Message):
    amount = random.randint(100, 10000)
    message.reply_text(f"ربحت 💰 {amount}$ !")

@app.on_message(filters.command("اكس") & filters.group)
def xo_game(client, message: Message):
    message.reply_text("❌ ⭕ لعبة إكس أو غير متوفرة حالياً، قريباً!")

@app.on_message(filters.command("همسة") & filters.group)
def whisper(client, message: Message):
    if message.reply_to_message:
        message.reply_to_message.reply_text("🔇 همسة: " + " ".join(message.command[1:]))
    else:
        message.reply("يجب الرد على رسالة لعمل الهمسة.")

@app.on_message(filters.text & filters.group)
def auto_reply(client, message: Message):
    text = message.text.lower()
    for key in replies:
        if key in text:
            message.reply_text(random.choice(replies[key]))
            break

@app.on_message(filters.command("طرد", prefixes="/") & filters.group)
def kick_member(client, message: Message):
    if message.reply_to_message:
        user_id = message.reply