import discord
from PIL import Image
from io import BytesIO
from discord.ext import commands
import youtube_dl
import datetime
import json
import random
import aiohttp
import asyncio
from random import choice
from discord.ext import tasks
import os
import psutil
from discord.ext.commands import Cog
import traceback
import sys


class fun(commands.Cog):
    def __init__(self, bot):
        self.client = bot


    @commands.command()
    async def slap(self, ctx, user: discord.Member):
        gifs = ["https://media1.tenor.com/images/b6d8a83eb652a30b95e87cf96a21e007/tenor.gif?itemid=10426943",
           "https://media1.tenor.com/images/e8f880b13c17d61810ac381b2f6a93c3/tenor.gif?itemid=17897236"]
        embed = discord.Embed(description=f"Woa {ctx.author.mention} chill bro... You slapped {user.mention} so hard he/she is now in hospital...",color=random.randint(0x000000, 0xFFFFFF))
        embed.set_image(url=f"{random.choice(gifs)}")
        if user == ctx.author:
            embed = discord.Embed(description=f"{ctx.author.mention} You wont slap yourself hard enough come HERE!",color=random.randint(0x000000, 0xFFFFFF))
            embed.set_image(url=f"{random.choice(gifs)}")
        await ctx.send(embed=embed)
        

    @commands.command()
    async def hug(self, ctx, user: discord.Member):
        gifs = ["https://cdn.weeb.sh/images/H1ui__XDW.gif", "https://cdn.weeb.sh/images/B11CDkhqM.gif", "https://cdn.weeb.sh/images/rJv2H5adf.gif", "https://cdn.weeb.sh/images/SywetdQvZ.gif", "https://cdn.weeb.sh/images/BJCCd_7Pb.gif", "https://cdn.weeb.sh/images/Bk5haAocG.gif"]
        embed = discord.Embed(description=f"{ctx.author.mention} hugs {user.mention} ",
                              color=random.randint(0x000000, 0xFFFFFF))
        embed.set_image(url=f"{random.choice(gifs)}")
        if user == ctx.author:
            embed = discord.Embed(description=f"{ctx.author.mention} Why you hugging yourself come here lemme hug you!",color=random.randint(0x000000, 0xFFFFFF))
            embed.set_image(url=f"{random.choice(gifs)}")
        await ctx.send(embed=embed)





     
    @commands.command()
    async def kiss(self, ctx, user: discord.Member):
        gifs = ["https://media1.tenor.com/images/558f63303a303abfdddaa71dc7b3d6ae/tenor.gif?itemid=12879850",
                "https://i.gifer.com/PCUi.gif", "https://cdn.weeb.sh/images/B13D2aOwW.gif","https://cdn.weeb.sh/images/B1yv36_PZ.gif", "https://cdn.weeb.sh/images/Sk5P2adDb.gif", "https://media.discordyui.net/reactions/kiss/234082934.gif"]
        embed = discord.Embed(description=f"Woah {ctx.author.mention} stop kissing {user.mention} so passionately ...",
                              color=random.randint(0x000000, 0xFFFFFF))
        embed.set_image(url=f"{random.choice(gifs)}")
        if user == ctx.author:
            embed = discord.Embed(description=f"{ctx.author.mention} Why you kissing yourself come here lemme kiss you!",color=random.randint(0x000000, 0xFFFFFF))
            embed.set_image(url=f"{random.choice(gifs)}")
        await ctx.send(embed=embed)



    
    @commands.command()
    async def pat(self, ctx, user: discord.Member):
        gifs = ["https://i1.wp.com/gifimage.net/wp-content/uploads/2017/07/head-pat-gif-9.gif?fit=800,450", 
                 "https://media1.tenor.com/images/6ee188a109975a825f53e0dfa56d497d/tenor.gif?itemid=17747839"
                 "https://64.media.tumblr.com/cadf248febe96afdd6869b7a95600abb/tumblr_onjo4cGrZE1vhnny1o1_500.gifv"]
        embed = discord.Embed(description=f"{ctx.author.mention} pats {user.mention}", color=random.randint(0x000000, 0xFFFFFF))
        embed.set_image(url=f"{random.choice(gifs)}")
        if user == ctx.author:
            embed = discord.Embed(description=f"{ctx.author.mention} Why you patting yourself come here lemme pat you!",color=random.randint(0x000000, 0xFFFFFF))
            embed.set_image(url=f"{random.choice(gifs)}")
        await ctx.send(embed=embed)    







    @commands.command()
    async def lick(self, ctx, user: discord.Member):
        gifs = ["https://images-ext-2.discordapp.net/external/AqmvPrnwsYvvxn5kgJH9Bd-J7mKkl3ka-jpVCwOiMyQ/https/cdn.weeb.sh/images/Sk15iVlOf.gif",
                "https://media1.tenor.com/images/6b701503b0e5ea725b0b3fdf6824d390/tenor.gif?itemid=12141727", "https://cdn.weeb.sh/images/ryGpGsnAZ.gif"]
        embed = discord.Embed(description=f"Woah {ctx.author.mention} stop licking {user.mention} like he/she is icecream ...",
                              color=discord.Color.blue())
        embed.set_image(url=f"{random.choice(gifs)}")
        if user == ctx.author:
            embed = discord.Embed(description=f"{ctx.author.mention} Licks himself. ||How do you even lick yourself?||",color=random.randint(0x000000, 0xFFFFFF))
            embed.set_image(url=f"{random.choice(gifs)}")
        await ctx.send(embed=embed)           





    @commands.command()
    async def kill(self, ctx, user: discord.Member):
        gifs = ["https://cdn.weeb.sh/images/r11as1tvZ.gif", "https://cdn.weeb.sh/images/BJO2j1Fv-.gif", ]
        embed = discord.Embed(description=f" {ctx.author.mention} brutally kills {user.mention} oooof...", color=random.randint(0x000000, 0xFFFFFF))
        embed.set_image(url=f"{random.choice(gifs)}")
        if user == ctx.author:
            embed = discord.Embed(description=f"{ctx.author.mention} You dumb why you wanna kill yourslf. ||If your feeling sad you can always DM Crepco#3057 :pleading_face:||",
            color=random.randint(0x000000, 0xFFFFFF))
            embed.set_image(url=f"{random.choice(gifs)}")
        await ctx.send(embed=embed)         




    @commands.command(name='cry')
    async def cry(self, ctx, member:discord.Member=None): 
        gifs = ["https://media1.tenor.com/images/98466bf4ae57b70548f19863ca7ea2b4/tenor.gif?itemid=14682297", "https://media1.tenor.com/images/e69ebde3631408c200777ebe10f84367/tenor.gif?itemid=5081296", "https://media1.tenor.com/images/b88fa314f0f172832a5f41fce111f359/tenor.gif?itemid=13356071", "https://media1.tenor.com/images/26e7564bfb4408f9f7ff9518d4f87308/tenor.gif?itemid=8199739", "https://media1.tenor.com/images/ce52606293142a2bd11cda1d3f0dc12c/tenor.gif?itemid=5184314"]
        if member == None:
            embed = discord.Embed(description=f"{ctx.author.mention} is crying. But why you crying ||If your feeling sad you can always DM Crepco#3057 :pleading_face:||", color=random.randint(0x000000, 0xFFFFFF))
            a = random.choice(gifs)
            embed.set_image(url=a)
        else:  
            embed = discord.Embed(description=f"{ctx.author.mention} cries cause of  {member.mention}", color=random.randint(0x000000, 0xFFFFFF))
            embed.set_image(url=f"{random.choice(gifs)}")
        await ctx.send(embed=embed)
    