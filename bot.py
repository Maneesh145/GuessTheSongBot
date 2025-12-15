import json
import logging
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

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


@bot.event
async def on_ready():
    logger.info("Bot is ready")
    await bot.tree.sync()


@bot.tree.command(
    name="guess",
    description="Guess the song from the lyrics. Requires spotify oauth connection.",
)
async def guess(interaction: discord.Interaction, source: str):
    logger.info(f"/guess called by user {interaction.user.id} with input: {source}")

    # Handle invalid playlist or album input (Issue #25)
    if "spotify.com/playlist" not in source and "spotify.com/album" not in source:
        logger.warning(f"Invalid playlist or album input: {source}")
        await interaction.response.send_message(
            "❌ Invalid playlist or album link. Please provide a valid Spotify playlist or album URL.",
            ephemeral=True
        )
        return

    # Valid input (actual game logic to be implemented later)
    await interaction.response.send_message(
        "Playlist/album accepted. Guess feature is under development."
    )

bot.run(TOKEN)
