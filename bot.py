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

@bot.tree.command(name="guess")
async def guess(interaction: discord.Interaction):
    logger.info(f"/guess called by {interaction.user.id}")
    await interaction.response.send_message("Guess feature is under development.")

bot.run(TOKEN)
