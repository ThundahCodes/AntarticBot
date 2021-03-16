import discord
import json
import random
import os 
from discord.ext import commands 
from discord.ext import tasks
import datetime
import asyncio


def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


client = commands.Bot(command_prefix = get_prefix, case_insensitive=True)
intents = discord.Intents.default()
intents.members = True

@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
       prefixes = json.load(f)

    prefixes[str(guild.id)] = '>'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
       prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.command()
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
       prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

        await ctx.send(f'Prefix changed to: {prefix}')


@client.event #When it's ready it does bla bla 
async def on_ready(): 
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Screaming at >help'))
    print('Bot are ready. ')

@client.command()
async def ping(ctx):    #when >ping says Pong! and  shows ms
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command() #magic 8 ball (aliases say that it can use these commands)
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes - definitely.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 "Don't count on it.",
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command()
async def customrules(ctx):
    embed = discord.Embed(
        title="Rules",
        colour = ctx.author.colour
    )
    embed.add_field(name=":one:", value="Streamer Mode / Anonymous Mode is not allowed.", inline = True)
    embed.add_field(name=":two:", value="Teaming/Stream Sniping is prohibited.", inline=True)
    embed.add_field(name=":three:", value="Fighting off spawn till 80 players is allowed, you may finish the ongoing fight till 75 players alive.", inline=True)
    embed.add_field(name=":four:", value="Fighting is allowed after 3rd zone is closed.", inline=True)
    embed.add_field(name=":five:", value="In event of a storm surge, you may kill where necessary.", inline=True)
    embed.set_thumbnail(url = str(ctx.guild.icon_url))
    await ctx.send(embed=embed)


@client.command()
async def topic(ctx):
    questions = ['If you could make up a school subject, what would it be?',
                 'Who makes you laugh the most?',
                 'What is your favorite part about school/work? Your least favorite?',
                 'What are the top three things on your bucket list?',
                 'What has been the lowest point of your life?',
                 'What would your ideal life look like?',
                 'What is the most memorable lesson you learned from your parents?',
                 'What scares you most about your future?',
                 'What keeps you up at night?',
                 'What is the best or worst trait you inherited from your parents?',
                 'What motivates you most in life?',
                 'What makes you feel discouraged?',
                 'What is a significant event that has changed you?',
                 'Who do you text the most?',
                 'What was your favorite thing to do as a kid?',
                 'What makes you laugh out loud?',
                 'What are you most passionate about?',
                 'What did you want to be growing up?',
                 'What is the best pickup line you’ve ever used? Heard?',
                 'Do you have any nicknames?',
                 'What is your favorite weekend activity?',
                 'Where do you see yourself living when you retire?',
                 'Who was your favorite teacher and why?',
                 'What is the silliest thing you’ve posted online?',
                 'Are you a cat person or a dog person?',
                 'What’s one movie you could watch over and over?',
                 'If you won the lottery, what would be your first big spend?',
                 'Where’s the most exotic place you’ve ever been?',
                 'Would you rather be invisible or have X-ray vision?',
                 'If you could have picked your own name, what would it be?',
                 'What time period would you travel to?',
                 'What is your least favorite chore?',
                 'What is one thing you can’t live without?',
                 'Who are you most thankful for and why?',
                 'Where do you want to go on the next family vacation?',
                 'What makes you most proud?',
                 'What would be your ideal day?',
                 'What did you think was the most challenging part of being a kid?',
                 'What’s one thing you’ve won and how did you win it?',
                 'What fun plans do you have for the weekend?',
                 'How old were you when you had your first job(freelance or normal job)?',
                 'How long can you go without checking your phone?',
                 'Have you ever really kept a New Year’s resolution?',
                 'What bad habits do you wish you could stop?',
                 'Are you a jealous person?',
                 'If someone offered to tell you your future, would you accept it?',
                 'Who’s your biggest hero?',
                 'If you were on death row, what would your last meal be?',
                 'What makes you really angry?',
                 'What is your spirit animal?',
                 'What’s your guilty pleasure?',
                 'What would you do if you were home alone and the power went out?',
                 'What would your rock band group be called?',
                 'Batman or Superman, who would win?',
                 'What’s the worst thing one can say on a first date?',
                 'What do you do to get rid of stress?',
                 'What three words best describe you?',
                 'What’s your favorite number? Why?',
                 'What’s your favorite way to waste time?',
                 'Do you have any pets? What are their names?',
                 'What is something popular now that annoys you?',
                 'Are you very active, or do you prefer to just relax in your free time?',
                 'How did you meet your best friend?',
                 'If you opened a business, what kind of business would it be?',
                 'Are you a very organized person?',
                 'How often do you stay up past 3 a.m.?',
                 'What do you bring with you everywhere you go?',
                 'Has anyone ever saved your life?',
                 'What do you think/fear is hiding in the dark?',
                 'What is the silliest fear you have?',
                 'What smell brings back great memories?',
                 'What outdoor activity haven’t you tried, but would like to?',
                 'What’s the best sitcom past or present?',
                 'What’s your favorite genre of movie?',
                 'What’s the worst movie you have seen recently?',
                 'What was the last song you listened to?',
                 'What is your favorite game soundtrack?',
                 'What is your favorite movie soundtrack?',
                 'What song always puts you in a good mood?',
                 'Are there any songs that always give you goosebumps?',
                 'What is the most useful app on your phone?',
                 'How often do you check your phone?',
                 'What is the most annoying thing about your phone?',
                 'What was your first smartphone? How did you feel when you got it?',
                 'What is the strangest themed restaurant you have heard of?',
                 'What’s the best way to travel? (Plane, car, train, etc.)',
                 'What is your favorite piece of technology that you own?',
                 'What is your favorite shirt?',
                 'What are your goals for the next two years?',
                 'How much do you plan for the future?',
                 'What is the best way to stay motivated and complete goals?',
                 'What do you want to do when you retire?',
                 'Do you prefer summer or winter activities?',
                 'What do you think of online education?',
                 'What is the spiciest thing you have ever eaten?',
                 'What food do you know you shouldn’t eat but can’t stop yourself?',
                 'What food looks disgusting but tastes delicious?',
                 'What do you think of homeschooling?',
                 'What will the future of education be?',
                 'What is your favorite holiday?',
                 'What bands or types of music do you listen to when you exercise(if you do)?']
    await ctx.send(f'{random.choice(questions)}')


@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=100):  
    await ctx.channel.purge(limit=amount)
    await ctx.send(f":white_check_mark: {amount} messages cleared.")

@client.command()
@commands.has_permissions(kick_members=True) 
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason) 
    await ctx.send(f'Banned {member.mention}')

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
         user = ban_entry.user 

         if (user.name, user.discriminator) == (member_name, member_discriminator):
             await ctx.guild.unban(user)
             await ctx.send(f'Unbanned {user.mention}')
             return 

@client.command()
@commands.has_permissions(kick_members=True)
async def mute(ctx, member : discord.Member):
    muted_role = ctx.guild.get_role(818565352782823445)

    await member.add_roles(muted_role)

    await ctx.send(member.mention + " has been muted")

@client.command()
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member : discord.Member):
    muted_role = ctx.guild.get_role(818565352782823445)

    await member.remove_roles(muted_role)

    await ctx.send(member.mention + " has been unmuted")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.command()
async def beer(ctx): 
    await ctx.send("Cheers :beers:")

@client.command()
@commands.has_permissions(kick_members=True)
async def whois(ctx, member : discord.Member):
    embed = discord.Embed(title = member.name , description = member.mention , color = discord.Colour.blue())
    embed.add_field(name = "ID", value = member.id , inline = True )
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)
    

@client.command()
async def membercount(ctx):
    a=ctx.guild.member_count
    b=discord.Embed(title=f"Members in {ctx.guild.name}",description=a,color=discord.Color((0xffff00)))
    await ctx.send(embed=b)

@client.command()
async def serverinfo(ctx):
    role_count = len(ctx.guild.roles)
    count = ctx.guild.member_count
    icon = str(ctx.guild.icon_url)
    embed = discord.Embed(title="Server Info", color = ctx.author.colour)
    embed.add_field(name = "Members", value = count)
    embed.add_field(name = "Region", value = "Europe")
    embed.add_field(name = "Roles", value = role_count)
    embed.set_thumbnail(url = icon)
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def tournament(ctx, date, time):
    embed = discord.Embed(title="Tournament", color = discord.Colour.blue())
    embed.add_field(name = "Tourney Date", value = date)
    embed.add_field(name = "Time", value = time)
    embed.set_thumbnail(url = 'https://estnn.com/wp-content/uploads/2019/09/Fortnite-Solos-Cash-Cup-September-11-Recap-and-Results.jpg')
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Hosted by {ctx.author.name}")
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def giveaway(ctx):
    await ctx.send("Let's start with the giveaway! Answer these question within 15 seconds!")

    questions = ["Which channel should it be hosted in?",
                 "What should be the duration of the giveaway? (s|m|h|d)",
                 "What is the prize?"
                ]
    
    answers = []

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    for i in questions:
        await ctx.send(i)

        try:
            msg = await client.wait_for('message', timeout=15.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send("You didn't answer in time, please be quicker next time!")
            return
        else:
            answers.append(msg.content)

    try:
        c_id = int(answers[0][2: -1])
    except:
        await ctx.send(f"You didn't mention a channel properly. Do it like this {ctx.channel.mention} next time")
        return

    channel = client.get_channel(c_id)

    time = convert(answers[1])
    if time == -1:
        await ctx.send(f"You didn't answer with a proper unit!")
        return
    elif time == -2:
        await ctx.send(f"Please enter an integer!")
        return
    prize = answers[2]

    await ctx.send(f"The Giveaway will be in {channel.mention} and will last {answers[1]}")

    embed = discord.Embed(title = 'Giveaway!', description = f"{prize}", color = ctx.author.color)

    embed.add_field(name="Hosted by:", value = ctx.author.mention)

    embed.set_footer(text=f"Ends {answers[1]} from now!")

    my_msg = await channel.send(embed=embed)

    await my_msg.add_reaction("🎉")

    await asyncio.sleep(time)

    new_msg = await channel.fetch_message(my_msg.id)

    users = await new_msg.reactions[0].users().flatten()
    
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await channel.send(f"Congratulations! {winner.mention} won {prize}!")


def convert(time):
    pos = ["s", "m", "h", "d"]

    time_dict = {"s" : 1, "m" : 60, "h" : 3600, "d" : 3600*24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]

client.run('heh')

