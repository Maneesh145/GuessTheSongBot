import json

import discord
from discord.ext import commands

with open("config.json") as f:
    config = json.load(f)

TOKEN = config["DISCORD_TOKEN"]
BOT_ID = config["DISCORD_BOT_ID"]

bot = commands.Bot(
    command_prefix=None,
    help_command=None,
    is_case_insensitive=True,
    intents=discord.Intents.all(),
)


@bot.event
async def on_ready():
    print("Ready!")
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} commands")
guess_count = {}

@bot.tree.command(
    name="guess",
    description="Guess the song from the lyrics. Requires spotify oauth connection.",
)
async def guess(interaction: discord.Interaction):
    user_id = interaction.user.id
    guess_count[user_id] = guess_count.get(user_id, 0) + 1

    await interaction.response.send_message(
        f"You have made {guess_count[user_id]} guesses so far."
    )
    


bot.run(TOKEN)
