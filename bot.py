import discord
import random
import os 
from discord.ext import commands 
from discord.ext import tasks

client = commands.Bot(command_prefix = '>', case_insensitive=True)

@client.event #When it's ready it does bla bla 
async def on_ready(): 
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Screaming at >help'))
    print('Bot are ready. ')

@client.command()
async def ping(ctx):    #when >ping says Pong! and  shows ms
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball', 'test']) #magic 8 ball (aliases say that it can use these commands)
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

f = open("rules.txt", "r")
rules = f.readlines()

@client.command(aliases=['rules'])
async def rule(ctx, *, number):
    await ctx.send(rules[int(number)-1])

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



@client.event
async def on_message(message):

    await client.process_commands(message)
      
    empty_array = []
    modmail_channel = discord.utils.get(client.get_all_channels(), name="║🎫║mod-mail")
    if message.author == client.user:
        return 
    if str(message.channel.type) == "private":
        if message.attachments != empty_array:
            files = message.attachments
            await modmail_channel.send("[" + message.author.display_name + "]")
            for file in files:
                 await modmail_channel.send(file.url)
        else:
            await modmail_channel.send("[" + message.author.display_name + "] " + message.content)
    elif str(message.channel) == "mod-mail" and message.content.startswith("<"):
        member_object = message.mentions[0]
        if message.attachments != empty_array:
            files = message.attachments
            await member_object.send("[" + message.author.display_name + "]")
            for file in files:
               await member_object.send(file.url)
        else: 
            index = message.content.index(" ")
            string = message.content
            mod_message = string[index:]

        await member_object.send("[" + message.author.display_name + "]" + mod_message)




client.run('heh')

