import os
import random
from dotenv import load_dotenv

from discord.ext import commands
import discord

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
    if payload.message_id != 851685610925588490:
        return

    emoji_to_role = {
            discord.PartialEmoji(name='🔴'): 851685230477574165, # ID of the role associated with unicode emoji '🔴'.
    }

    guild = bot.get_guild(payload.guild_id)
    if guild is None:
        return

    try:
        role_id = emoji_to_role[payload.emoji]
    except KeyError:
        return

    role = guild.get_role(role_id)
    if role is None:
        return

    try:
        await payload.member.add_roles(role)
    except discord.HTTPException:
        pass

@bot.event
async def on_raw_reaction_remove(payload: discord.RawReactionActionEvent):
    if payload.message_id != 851685610925588490:
        return

    emoji_to_role = {
            discord.PartialEmoji(name='🔴'): 851685230477574165, # ID of the role associated with unicode emoji '🔴'.
    }

    guild = bot.get_guild(payload.guild_id)
    if guild is None:
        return

    try:
        role_id = emoji_to_role[payload.emoji]
    except KeyError:
        return

    role = guild.get_role(role_id)
    if role is None:
        return

    member = guild.get_member(payload.user_id)
    if member is None:
        return

    try:
        await member.remove_roles(role)
    except discord.HTTPException:
        pass


bot.run(TOKEN)
