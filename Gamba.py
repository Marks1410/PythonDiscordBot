import os
# import config
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


Client = discord.Client()
client = commands.Bot(command_prefix = "!")


@client.event
async def on_ready():
    print("It's time to Gamba")

# "<@" + message.author.id + "">
@client.event
async def on_message(message):
    if message.content == "<@528043536210198558> Fuck you":
        await client.send_message(message.channel, "<@" + message.author.id + "> fuck you and <@528024262058180608> too")
    if message.content == "Are you ready?":
        await client.send_message(message.channel, "Adrenaline is pumping")
    if message.content == "Generator. Automatic lover":
        await client.send_message(message.channel, "Atomic. Atomic. Overdrive")
    if message.content == "Blockbuster. Brain power":
        await client.send_message(message.channel, "Call me a leader. Cocaine")
    if message.content == "Don't you try it, don't you try it":
        await client.send_message(message.channel, "Innovator. Killer machine")
    if message.content == "There's no fate. Take control":
        await client.send_message(message.channel, "Brain power")
    if message.content == "Let the bass kick":
        await client.send_message(message.channel, "O-oooooooooo AAAAE-A-A-I-A-U- JO-oooooooooooo AAE-O-A-A-U-U-A- E-eee-ee-eee AAAAE-A-E-I-E-A- JO-ooo-oo-oo-oo EEEEO-A-AAA-AAAA")
    if message.content == "O-oooooooooo AAAAE-A-A-I-A-U- JO-oooooooooooo AAE-O-A-A-U-U-A- E-eee-ee-eee AAAAE-A-E-I-E-A- JO-ooo-oo-oo-oo EEEEO-A-AAA-AAAA":
        await client.send_message(message.channel, "O-ooooooooo AAAAE-A-A-I-A-U- JO-oooooooooooo AAE-O-A-A-U-U-A- E-eee-ee-eee AAAAE-A-E-I-E-A- JO-ooo-oo-oo-oo EEEEO-A-AAA-AAAA")
    if message.content == "O-ooooooooo AAAAE-A-A-I-A-U- JO-oooooooooooo AAE-O-A-A-U-U-A- E-eee-ee-eee AAAAE-A-E-I-E-A- JO-ooo-oo-oo-oo EEEEO-A-AAA-AAAA":
        await client.send_message(message.channel, "O-oooooooo AAAAE-A-A-I-A-U- JO-oooooooooooo AAE-O-A-A-U-U-A- E-eee-ee-eee AAAAE-A-E-I-E-A- JO-ooo-oo-oo-oo EEEEO-A-AAA-AAAA")
    if message.content == "!Current":
        await client.send_message(message.channel, "https://cdn.discordapp.com/attachments/293757180161556480/525755441746149376/unknown.png")
    if message.content == "<a:hyperclap:528313470077108253>":
        await client.send_message(message.channel, "<:roonya:528310915951624193>" + " " + "<a:hyperclap:528313470077108253>")

# Token for local development
# client.run(config.token)

# Token for Heroku
client.run(os.getenv('TOKEN'))