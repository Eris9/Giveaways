#!/usr/bin/python3
import discord
from discord.ext import commands
import os
import asyncpg

bot = commands.Bot(command_prefix="g?", help_command = None, status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name= "g?help"))

for filename in os.listdir("./cogs"):
		if filename.endswith(".py"):
			bot.load_extension(f"cogs.{filename[:-3]}")

bot.run("")
