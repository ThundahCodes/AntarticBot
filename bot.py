import discord
import json
import random
import os 
from discord.ext import commands 
from discord.ext import tasks
import datetime
import asyncio
import aiofiles

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = get_prefix, case_insensitive=True)
intents = discord.Intents.default()
intents.members = True
client.ticket_configs = {}


@client.event
async def on_guild_join(guild):
    client.warnings[guild.id] = {}
   
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
    print('Bot is ready. ')
    for file in ["ticket_configs.txt"]:
        async with aiofiles.open(file, mode="a") as temp:
            pass
    
    for guild in client.guilds:
        async with aiofiles.open(f"{guild.id}.txt", mode="a") as temp:
            pass

        client.warnings[guild.id] = {}
            
    for guild in client.guilds:
        async with aiofiles.open(f"{guild.id}.txt", mode="r") as file:
            lines = await file.readlines()

            for line in lines:
                data = line.split(" ")
                member_id = int(data[0])
                admin_id = int(data[1])
                reason = " ".join(data[2:]).strip("\n")

                try:
                    client.warnings[guild.id][member_id][0] += 1
                    client.warnings[guild.id][member_id][1].append((admin_id, reason))

                except KeyError:
                    client.warnings[guild.id][member_id] = [1, [(admin_id, reason)]]



    async with aiofiles.open("ticket_configs.txt", mode="r") as file:
        lines = await file.readlines()
        for line in lines:
            data = line.split(' ')
            client.ticket_configs[int(data[0])] = [int(data[1]), int(data[2]), int(data[3])]

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

@client.command()
async def configure_ticket(ctx, msg: discord.Message=None, category: discord.CategoryChannel=None):
    if msg is None or category is None:
        await ctx.channel.send("Failed to configure the ticket as an argument was not given or was invalid")
        return

    client.ticket_configs[ctx.guild.id] = [msg.id, msg.channel.id, category.id] # this resets the config 

    async with aiofiles.open("ticket_configs.txt", mode="r") as file:
        data = await file.readlines()

    async with aiofiles.open("ticket_configs.txt", mode="w") as file:
        await file.write(f"{ctx.guild.id} {msg.id} {msg.channel.id} {category.id}\n")
        
        for line in data:
            if int(line.split(" ")[0]) != ctx.guild.id:
                await file.write(line)
                

        await msg.add_reaction(u"\U0001F3AB")
        await ctx.channel.send("Succesfully configured the ticket system.")

@client.event
async def on_raw_reaction_add(payload):
    if payload.member.id != client.user.id and str(payload.emoji) == u"\U0001F3AB":
        msg_id, channel_id, category_id = client.ticket_configs[payload.guild_id]

        if payload.message_id == msg_id:
            guild = client.get_guild(payload.guild_id)

            for category in guild.categories:
                if category.id == category_id:
                    break

            channel = guild.get_channel(channel_id)

            ticket_num = 1 if len(category.channels) == 0 else int(category.channels[-1].name.split("-")[-1]) + 1
            ticket_channel = await category.create_text_channel(f"ticket: {ticket_num}", topic=f"A channel for ticket number {ticket_num}.", permission_synced=True)

            await ticket_channel.set_permissions(payload.member, read_messages=True, send_messages=True)

            message = await channel.fetch_message(msg_id)
            await message.remove_reaction(payload.emoji, payload.member)

            

            await ticket_channel.send(f"{payload.member.mention} Thank you for creating a ticket! Use **>close** to close your ticket")
            
            try:
                await client.wait_for("message", check=lambda m: m.channel == ticket_channel and m.author == payload.member and m.content == ">close", timeout=3600)

            except asyncio.TimeoutError:
                await ticket_channel.delete()


            else:
                await ticket_channel.delete()
                
@client.command()
async def ticket_config(ctx):
    try:
        msg_id, channel_id, category_id = client.ticket_configs[ctx.guild.id]

    except KeyError:
        await ctx.channel.send("You have not configured the ticket system yet.")

    else:
        embed = discord.Embed(title="Ticket System Configuration", color=discord.Color.green())
        embed.description = f"**Reaction Message ID** : {msg_id}\n"
        embed.description += f"**Ticket Category ID** : {category_id}\n\n"

        await ctx.channel.send(embed=embed)

@client.event
async def on_member_join(member):
    embed = discord.Embed(colour=0x95efcc ,description=f"Welcome the discord server! You are the {len(list(member.guild.members))} member!")
    embed.set_thumbnail(url=f"{member.avatar_url}")
    embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
    embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
    embed.timestamp = datetime.datetime.utcnow()

    channel = await client.get_channel(id=822876236203425857)

    await channel.send(embed=embed)

client.warnings = {}

@client.command()
@commands.has_permissions(administrator=True)
async def warn(ctx, member : discord.Member=None, *, reason=None):
    if member is None:
        return await ctx.send("The provided member could not be found or you forgot to provide one.")

    if reason is None:
        return await ctx.send("Please provide a reason for warning this user.")

    try:
        first_warning = False
        client.warnings[ctx.guild.id][member.id][0] += 1
        client.warnings[ctx.guild.id][member.id][1].append((ctx.author.id, reason))

    except KeyError:
        first_warning = True
        client.warnings[ctx.guild.id][member.id] = [1, [(ctx.author.id, reason)]]

    count = client.warnings[ctx.guild.id][member.id][0]

    async with aiofiles.open(f"{ctx.guild.id}.txt", mode="a") as file:
        await file.write(f"{member.id} {ctx.author.id} {reason}\n")
    
    await ctx.send(f"{member.mention} has {count} {'warning' if first_warning else 'warnings'}.")

@client.command()
@commands.has_permissions(administrator=True)
async def warnings(ctx, member : discord.Member=None):
    if member is None:
        return await ctx.send("The provided member could not be found or you forgot to provide one.")

    embed = discord.Embed(title=f"Displaying warnings for {member.name}", description="", colour=discord.Colour.red())
    try:
        i = 1
        for admin_id, reason in client.warnings[ctx.guild.id][member.id][1]:
            admin = ctx.guild.get_member(admin_id)
            embed.description += f"**Warning {i}** given by: {admin.mention} for: *'{reason}'*.\n"
            i += 1

        await ctx.send(embed=embed)

    except KeyError:
        await ctx.send("This user has no warnings.")


gifs = ["https://media1.tenor.com/images/b6d8a83eb652a30b95e87cf96a21e007/tenor.gif?itemid=10426943", 
        "https://media1.tenor.com/images/e8f880b13c17d61810ac381b2f6a93c3/tenor.gif?itemid=17897236",
        "https://i.gifer.com/2eNz.gif",
        "https://i.gifer.com/RK9x.gif"]

@client.command()
async def slap(ctx, user, member : discord.Member=None):
    embed = discord.Embed(colour=discord.Colour.green(), description=f"{ctx.author.mention} slapped {member.mention}!")
    embed.set_image(url=f"{random.choice(gifs)}")
    if user == ctx.author:
        embed = discord.Embed(description=f"{ctx.author.mention} You wont slap yourself hard enough come here!", color = random.randint(0x000000, 0xFFFFFF))
        embed.set_image(url=f"{random.choice(gifs)}")    
    
    await ctx.send(embed=embed)


client.run('nt')
