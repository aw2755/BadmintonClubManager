import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv('.env')
TOKEN = os.environ.get("Token")

def run_bot():
    client = commands.Bot(command_prefix='!', intents=discord.Intents.all())
    client.remove_command('help')
    queue = []
    court1 = []
    court2 = []
    court3 = []
    court4 = []
    

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.command(name="help")
    async def _help(ctx):

        embed = discord.Embed(colour=discord.Colour.orange())
        embed.set_author(name='Help')
        embed.add_field(name='!help', value="Shows all commands", inline=False)
        embed.add_field(name='!join <num>', value="Joins the queue", inline=False)
        embed.add_field(name='!leave', value="Leaves the queue", inline=False)
        embed.add_field(name='!show', value="Shows the queue", inline=False)
        await ctx.message.author.send(embed=embed)
    
    @client.command(name="join")
    async def _join(ctx, court_num):
        player = ctx.message.author
        if queue.__contains__(player):
            await ctx.message.author.send("```ansi\n\u001b[1;0;35myou are already in a queue =]```")
        else:
            match court_num:
                case "1":
                    queue.append(player)
                    court1.append(player)
                    await ctx.message.author.send("```ansi\n\u001b[1;0;35myou have **joined** the queue for court 1```")
                case "2":
                    queue.append(player)
                    court2.append(player)
                    await ctx.message.author.send("```ansi\n\u001b[1;0;35myou have **joined** the queue for court 2```")
                case "3":
                    queue.append(player)
                    court3.append(player)
                    await ctx.message.author.send("```ansi\n\u001b[1;0;35myou have **joined** the queue for court 3```")
                case "4":
                    queue.append(player)
                    court4.append(player)
                    await ctx.message.author.send("```ansi\n\u001b[1;0;35myou have **joined** the queue for court 4```")
                case _: 
                    user_id = ctx.message.author.id
                    await ctx.channel.send(f"<@{user_id}>** court_number must be (1-4)**")
            
    @client.command(name="leave")
    async def _leave(ctx):
        player = ctx.message.author
        if queue.__contains__(player):
            queue.remove(player)
            if court1.__contains__(player):
                court1.remove(player)
                await ctx.message.author.send("```ansi\n\u001b[1;0;35myou have **left** the queue for court 1```")
            elif court2.__contains__(player):
                court2.remove(player)
                await ctx.message.author.send("```ansi\n\u001b[1;0;35myou have **left** the queue for court 2```")
            elif court3.__contains__(player):
                court3.remove(player)
                await ctx.message.author.send("```ansi\n\u001b[1;0;35myou have **left** the queue for court 3```")
            elif court4.__contains__(player):
                court4.remove(player)
                await ctx.message.author.send("```ansi\n\u001b[1;0;35myou have **left** the queue for court 4```")
        else:
            await ctx.message.author.send("```ansi\n\u001b[1;0;35myou are not in the queue, feel free to join =]```")

    @client.command(name="show")
    async def _show(ctx):

        embed1 = discord.Embed(colour=discord.Colour.orange())
        embed1.set_author(name='COURT 1')

        embed2 = discord.Embed(colour=discord.Colour.orange())
        embed2.set_author(name='COURT 2')

        embed3 = discord.Embed(colour=discord.Colour.orange())
        embed3.set_author(name='COURT 3')

        embed4 = discord.Embed(colour=discord.Colour.orange())
        embed4.set_author(name='COURT 4')

        for x in range(len(court1)):
            if court1[x].nick is None:
                embed1.add_field(name=[x + 1, court1[x].name], value="", inline=False)
            else:
                embed1.add_field(name=[x + 1, court1[x].nick], value="", inline=False)

        for x in range(len(court2)):
            if court2[x].nick is None:
                embed2.add_field(name=[x + 1, court2[x].name], value="", inline=False)
            else:
                embed2.add_field(name=[x + 1, court2[x].nick], value="", inline=False)

        for x in range(len(court3)):
            if court3[x].nick is None:
                embed3.add_field(name=[x + 1, court3[x].name], value="", inline=False)
            else:
                embed3.add_field(name=[x + 1, court3[x].nick], value="", inline=False)

        for x in range(len(court4)):
            if court4[x].nick is None:
                embed4.add_field(name=[x + 1, court4[x].name], value="", inline=False)
            else:
                embed4.add_field(name=[x + 1, court4[x].nick], value="", inline=False)        

        await ctx.message.author.send(embed=embed1)
        await ctx.message.author.send(embed=embed2)
        await ctx.message.author.send(embed=embed3)
        await ctx.message.author.send(embed=embed4)

    @client.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            user_id = ctx.message.author.id
            await ctx.send(f"**Please pass in all required argumenets <@{user_id}>. Type !help for list of commands**")

    client.run(str(TOKEN))
