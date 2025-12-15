import json
import discord
from discord.ext import commands

# Load config
with open("config.json") as f:
    config = json.load(f)

TOKEN = config["DISCORD_TOKEN"]

# Create bot
bot = commands.Bot(
    command_prefix=None,
    help_command=None,
    intents=discord.Intents.all(),
)

# Store attempts per user
MAX_ATTEMPTS = 3
attempts_left = {}

@bot.event
async def on_ready():
    print("Ready!")
    await bot.tree.sync()


@bot.tree.command(
    name="guess",
    description="Guess the song from the lyrics.",
)
async def guess(interaction: discord.Interaction):
    user_id = interaction.user.id

    # Initialize attempts if user is new
    if user_id not in attempts_left:
        attempts_left[user_id] = MAX_ATTEMPTS

    # Check attempts
    if attempts_left[user_id] <= 0:
        await interaction.response.send_message(
            "❌ No attempts left for this track.",
            ephemeral=True
        )
        return

    # Reduce attempt count
    attempts_left[user_id] -= 1

    await interaction.response.send_message(
        f"❗ Incorrect guess. Attempts left: {attempts_left[user_id]}"
    )


bot.run(TOKEN)
