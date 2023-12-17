import os
import json
import ast
import shlex
import shutil
import discord
import crayons
import random
import discord
import utils
from datetime import datetime, timedelta
import pytz
from discord.ext import commands
from discord.utils import oauth_url
import asyncio
from asyncio import sleep
import psycopg2
from discord.utils import get
import requests

bot = commands.Bot(command_prefix='b!', case_insensitive=True)
bot.remove_command('help') 
bot.owner_id = '803388834506080277'

def owner_or_has_permissions(**perms):
    async def predicate(ctx):
        if await ctx.bot.is_owner(ctx.author):
            return True
        permissions = ctx.channel.permissions_for(ctx.author)
        missing = [perm for perm, value in perms.items(
        ) if getattr(permissions, perm, None) != value]
        if not missing:
            return True
        raise commands.MissingPermissions(missing)

    return commands.check(predicate)

@bot.command(pass_context=True, aliases=["announcement"])
@commands.has_any_role(1101908156474462318, 1041335333159194635, 1065304826214350951, 1143943100528607352, 1099769512120827934, 1087082481095815250, 1174653797142900786, 1155240198783914024, 1141977130696183929, 1143942881132937277)
async def announce(ctx,  *, message=""):
    try:
        channel_id = 1121900239746506822  # Replace with your specific channel ID
        channel = bot.get_channel(channel_id)
        await channel.send(message)
        await ctx.send(f'{ctx.message.author.mention} Announcement Has Been Sent :white_check_mark: ')
    except:
        await ctx.send(f'{ctx.message.author.mention} Failed Sending Announcement :x: ')


@announce.error
async def mop_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(":warning: Insufficent permissions ")


async def status_task():
    while True:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Elegance is a journey."))


def get_token(*, test=False):
    token = os.getenv(
        "")
    if token:
        return token
    path = ".token"
    if test:
        path += "-test"
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()


if __name__ == '__main__':
    import sys
    test = "--test" in sys.argv
    if test:
        bot.command_prefix = "-"
    bot.run(get_token(test=test))
