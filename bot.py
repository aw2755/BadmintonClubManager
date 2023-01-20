import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv('.env')
TOKEN = os.environ.get("Token")

def run_bot():
    client = commands.Bot(command_prefix='-', intents=discord.Intents.all())
    client.remove_command('help')
    show = []
    court1 = []
    court2 = []
    court3 = []
    court4 = []
    

    @client.event
    async def on_ready():
        print(f'{client.user.name} is now running')
        await client.change_presence(activity=discord.Game(name="-help"))
    
    @client.command(name="help")
    async def _help(ctx):
        embed = discord.Embed(colour=discord.Colour.orange())
        embed.set_author(name='__Command List__')
        embed.add_field(name='-help', value="Shows all the commands", inline=False)
        embed.add_field(name='-join <num>', value="Joins a queue for a court", inline=False)
        embed.add_field(name='-leave', value="Leaves a queue for a court", inline=False)
        embed.add_field(name='-queue', value="Shows the queues for all courts", inline=False)
        embed.add_field(name='-create <time>am/pm', value="Creates an event", inline=False)
        embed.add_field(name='-show', value="Shows everyone who is interested in going to the created event", inline=False)
        #embed.add_field(name='-done <num>', value="Clears everyone off a court **FOR E-board USE ONLY**", inline=False)
        await ctx.message.author.send(embed=embed)
    
    @client.command(name="join")
    async def _join(ctx, court_num):
        user_id = ctx.message.author.id
        player = ctx.message.author
        if (not court1.__contains__(player)) and (not court2.__contains__(player)) and (not court3.__contains__(player)) and (not court4.__contains__(player)):
            match court_num:
                case "1":
                    court1.append(player)
                    await ctx.channel.send(f"<@{user_id}>** has joined court 1**")
                case "2":
                    court2.append(player)
                    await ctx.channel.send(f"<@{user_id}>** has joined court 2**")
                case "3":
                    court3.append(player)
                    await ctx.channel.send(f"<@{user_id}>** has joined court 3**")
                case "4":
                    court4.append(player)
                    await ctx.channel.send(f"<@{user_id}>** has joined court 4**")
                case _: 
                    await ctx.channel.send(f"<@{user_id}>** court_number must be (1-4)**")
        else:
            await ctx.channel.send(f"<@{user_id}>you are already in a queue")
             
    @client.command(name="leave")
    async def _leave(ctx):
        user_id = ctx.message.author.id
        player = ctx.message.author
        if court1.__contains__(player):
            court1.remove(player)
            await ctx.channel.send(f"<@{user_id}>** has left court 1**")
        elif court2.__contains__(player):
            court2.remove(player)
            await ctx.channel.send(f"<@{user_id}>** has left court 2**")
        elif court3.__contains__(player):
            court3.remove(player)
            await ctx.channel.send(f"<@{user_id}>** has left court 3**")
        elif court4.__contains__(player):
            court4.remove(player)
            await ctx.channel.send(f"<@{user_id}>** has left court 4**")
        else:
            await ctx.message.channel.send(f"<@{user_id}>**, you are not in a queue**")

    @client.command(name="queue")
    async def _queue(ctx):
        embed1 = discord.Embed(colour=discord.Colour.orange())
        embed1.set_author(name='__COURT 1__')
        for x in range(len(court1)):
            if x < 4:
                if court1[x].nick is None:
                    embed1.add_field(name=[x + 1, court1[x].name], value="currently playing", inline=False)
                else:
                    embed1.add_field(name=[x + 1, court1[x].nick], value="currently playing", inline=False)
            else:
                if court1[x].nick is None:
                    embed1.add_field(name=[x + 1, court1[x].name], value="", inline=False)
                else:
                    embed1.add_field(name=[x + 1, court1[x].nick], value="", inline=False)

        embed2 = discord.Embed(colour=discord.Colour.orange())
        embed2.set_author(name='__COURT 2__')
        for x in range(len(court2)):
            if x < 4:
                if court2[x].nick is None:
                    embed2.add_field(name=[x + 1, court2[x].name], value="currently playing", inline=False)
                else:
                    embed2.add_field(name=[x + 1, court2[x].nick], value="currently playing", inline=False)
            else:
                if court2[x].nick is None:
                    embed2.add_field(name=[x + 1, court2[x].name], value="", inline=False)
                else:
                    embed2.add_field(name=[x + 1, court2[x].nick], value="", inline=False)

        embed3 = discord.Embed(colour=discord.Colour.orange())
        embed3.set_author(name='__COURT 3__')
        for x in range(len(court3)):
            if x < 4:
                if court3[x].nick is None:
                    embed3.add_field(name=[x + 1, court3[x].name], value="currently playing", inline=False)
                else:
                    embed3.add_field(name=[x + 1, court3[x].nick], value="currently playing", inline=False)
            else:
                if court3[x].nick is None:
                    embed3.add_field(name=[x + 1, court3[x].name], value="", inline=False)
                else:
                    embed3.add_field(name=[x + 1, court3[x].nick], value="", inline=False)
        
        embed4 = discord.Embed(colour=discord.Colour.orange())
        embed4.set_author(name='__COURT 4__')
        for x in range(len(court4)):
            if x < 4:
                if court4[x].nick is None:
                    embed4.add_field(name=[x + 1, court4[x].name], value="currently playing", inline=False)
                else:
                    embed4.add_field(name=[x + 1, court4[x].nick], value="currently playing", inline=False)    
            else:
                if court4[x].nick is None:
                    embed4.add_field(name=[x + 1, court4[x].name], value="", inline=False)
                else:
                    embed4.add_field(name=[x + 1, court4[x].nick], value="", inline=False)  

        await ctx.channel.send(embed=embed1)
        await ctx.channel.send(embed=embed2)
        await ctx.channel.send(embed=embed3)
        await ctx.channel.send(embed=embed4)

    @client.command(name="done")
    @commands.has_role('E-board')
    async def _done(ctx, num):
        match num:
            case "1":
                await ctx.channel.send("**court 1 has finished playing**")
                for x in range(len(court1)):
                    if x < 4:
                        court1.pop()
                for x in range(len(court1)):
                    if x < 4:
                        player_id = court1[x].id
                        await ctx.channel.send(f"<@{player_id}> ur up")

            case "2":
                for x in range(len(court2)):
                    if x < 4:
                        court2.pop()
                await ctx.channel.send("**court 2 has finished playing**")
                for x in range(len(court2)):
                    if x < 4:
                        player_id = court2[x].id
                        await ctx.channel.send(f"<@{player_id}> **get ready to play on court 1**")

            case "3":
                for x in range(len(court3)):
                    if x < 4:
                        court3.pop()
                await ctx.channel.send("**court 3 has finished playing**")
                for x in range(len(court3)):
                    if x < 4:
                        player_id = court3[x].id
                        await ctx.channel.send(f"<@{player_id}> **get ready to play on court 1**")

            case "4":
                for x in range(len(court4)):
                    if x < 4:
                        court4.pop()
                await ctx.channel.send("**court 4 has finished playing**")
                for x in range(len(court4)):
                    if x < 4:
                        player_id = court4[x].id
                        await ctx.channel.send(f"<@{player_id}> **get ready to play on court 1**")
            case _:
                user_id = ctx.message.author.id
                await ctx.channel.send(f"<@{user_id}> **court_number must be (1-4)**")

    @client.command(name="create")
    async def _create(ctx, time):
        user_id = ctx.message.author.id
        show.clear()
        author = ctx.message.author
        user_id = ctx.message.author.id
        await ctx.channel.send(f"**<@{user_id}> wants to play badminton at {time}**")
        message = await ctx.channel.send("react to this message with 🏸 if you would like to join")
        await message.add_reaction("🏸")
        if author.nick is None:
            show.append(author)
        else:
            show.append(author)

    @client.command(name="show")
    async def _show(ctx):
        embed = discord.Embed(colour=discord.Colour.orange())
        embed.set_author(name='__PEOPLE GOING__')
        embed.add_field(name=len(show), value="", inline=False)
        for x in range(len(show)):
            if show[x].nick is None:
                embed.add_field(name=show[x].name, value="", inline=False)
            else:
                embed.add_field(name=show[x].nick, value="", inline=False)
        await ctx.channel.send(embed=embed)

    @client.event
    async def on_reaction_add(reaction, user):
        message = "react to this message with 🏸 if you would like to join"
        for x in range(len(show)):
            if(show[x].name == user.name):
                return
        if reaction.message.content == message and reaction.emoji == '🏸' and user.name != "BadmintonClubManager":
                show.append(user)

    @client.event
    async def on_reaction_remove(reaction, user):
        message = "react to this message with 🏸 if you would like to join"
        for x in range(len(show)):
            if(show[x].name == user.name):
                return
        if reaction.message.content == message and reaction.emoji == '🏸' and user.name != "BadmintonClubManager":
            show.remove(user)

    @client.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            user_id = ctx.message.author.id
            await ctx.channel.send(f"**Please pass in all required argumenets <@{user_id}>. Type !help for list of commands**")


    client.run(str(TOKEN))
