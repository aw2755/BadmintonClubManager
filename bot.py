import discord
import os
from court import Court
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv('.env')
TOKEN = os.getenv("Token")

def run_bot():
    client = commands.Bot(command_prefix='-', intents=discord.Intents.all())
    client.remove_command('help')
    show = []
    court1 = Court(court_num=1)
    court2 = Court(court_num=2)
    court3 = Court(court_num=3)
    court4 = Court(court_num=4)
    courts = {1: court1,
              2: court2,
              3: court3,
              4: court4}
    

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

        try:
            court = courts.get(int(court_num))
            if court is None:
                raise ValueError
        except ValueError:
            await ctx.channel.send(f"<@{user_id}>** Court's number must be (1-4)**")
            return


        for cur_court in courts.values():
            if cur_court.has(player):
                await ctx.channel.send(f"<@{user_id}>you are already in Court {cur_court.court_num}. You can only join one court.")
                return

        success = court.add_player(player)
        if success:
            await ctx.channel.send(f"<@{user_id}>** has joined Court {court_num}**")
        else:
            await ctx.channel.send(f"<@{user_id}> you are already on Court {court_num}")

 
             
    @client.command(name="leave")
    async def _leave(ctx):
        user_id = ctx.message.author.id
        player = ctx.message.author
        
        player_court = None
        for court in courts.values():
            if court.has(player):
                player_court = court
                break
        if player_court is None:
            await ctx.message.channel.send(f"<@{user_id}>**, you are not in a court**")
        else:
            player_court.remove_player(player)
            await ctx.channel.send(f"<@{user_id}>** has left Court {player_court.court_num}**")


    @client.command(name="queue")
    async def _queue(ctx):
        for court in courts.values():
            embed = discord.Embed(colour=discord.Colour.orange())
            embed.set_author(name=f'__COURT {court.court_num}__')
            for num_player, player in enumerate(court.players):
                message = "currently playing" if num_player < 4 else "waiting in queue"
                name = player.name if player.nick is None else player.name
                embed.add_field(name=[num_player + 1, name], value=message, inline=False)
            await ctx.channel.send(embed=embed)


    @client.command(name="done")
    @commands.has_role('E-board')
    async def _done(ctx, court_num, player_count = 4):
        user_id = ctx.message.author.id
        court = courts.get(int(court_num))
        if court is None:
            await ctx.channel.send(f"<@{user_id}> **court_number must be (1-4)**")
        else:
            await ctx.channel.send(f"**Court {court_num} has finished playing**")
            for i in range(player_count):
                try:
                    court.players.pop()
                except IndexError:
                    await ctx.channel.send(f"<@{user_id}> **popped more players than there is on Court {court_num}**")
                    break
            for i in range(len(court.players)):
                if i < 4:
                    player = court.players[i]
                    await ctx.channel.send(f"<@{player.id}> get ready to play on Court {court_num}")


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

    client.run(TOKEN)


