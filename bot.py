import os
import discord
from discord.ext import commands

# 環境変数からトークンと対象ユーザーIDを取得
TOKEN = os.getenv("DISCORD_TOKEN")
TARGET_USER_ID = int(os.getenv("TARGET_USER_ID"))

# モールス変換辞書
MORSE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/', '.': '.-.-.-', '?': '..--..', '!': '-.-.--'
}

# モールス変換関数
def to_morse(text):
    return ' '.join(MORSE_DICT.get(c.upper(), '?') for c in text).replace('.', '・')

# BOTの初期化
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Botログイン完了: {bot.user.name}')

@bot.event
async def on_message(message):
    print(f"DEBUG: {message.author.id} - {message.author.display_name} said: {message.content}")
    if message.author.bot:
        return
    if message.author.id == TARGET_USER_ID:
        await message.delete()
        morse = to_morse(message.content)
        await message.channel.send(f"🔇 `{message.author.display_name}` の発言:\n`{morse}`")
    else:
        await bot.process_commands(message)

bot.run(TOKEN)
