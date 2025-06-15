import discord
from discord.ext import commands

TOKEN = ''# ここにbotのトークンを記入してください
TARGET_USER_ID = 1155009122924761140  # ← この値は18桁以内にしてください

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

def to_morse(text):
    return ' '.join(MORSE_DICT.get(c.upper(), '?') for c in text).replace('.', '・')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'\u2705 Bot\u30ed\u30b0\u30a4\u30f3\u5b8c\u4e86: {bot.user.name}')

@bot.event
async def on_message(message):
    print(f"DEBUG: {message.author.id} - {message.author.display_name} said: {message.content}")
    if message.author.bot:
        return
    if message.author.id == TARGET_USER_ID:
        await message.delete()
        morse = to_morse(message.content)
        await message.channel.send(f"\ud83d\udd07 `{message.author.display_name}` の発言:\n`{morse}`")
    else:
        await bot.process_commands(message)

bot.run(TOKEN)
