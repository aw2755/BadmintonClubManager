import discord
from discord.ext import commands


def run_bot():
    TOKEN = 'MTA2MzI4OTk3MzU2ODE4NDMyMA.GBIajJ.cWE2WNaDEJEo-Ys86sn6dCkppB-bhqYV6YMa1c'
    client = commands.Bot(command_prefix='!', intents=discord.Intents.all())
    client.remove_command('help')
    queue = []

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.command(name="help")
    async def _help(ctx):

        embed = discord.Embed(colour=discord.Colour.orange())
        embed.set_author(name='Help')
        embed.add_field(name='!help', value="Shows all commands", inline=False)
        embed.add_field(name='!join', value="Joins the queue", inline=False)
        embed.add_field(name='!leave', value="Leaves the queue", inline=False)
        embed.add_field(name='!show', value="Shows the queue", inline=False)
        await ctx.message.author.send(embed=embed)

    @client.command(name="join")
    async def _join(ctx):
        player = ctx.message.author
        if queue.__contains__(player):
            await ctx.message.author.send("`you are already in the queue =]`")
        else:
            queue.append(player)
            await ctx.message.author.send("`you have joined the queue`")

    @client.command(name="leave")
    async def _leave(ctx):
        player = ctx.message.author
        if queue.__contains__(player):
            queue.remove(player)
            await ctx.message.author.send("`you have left the queue`")
        else:
            await ctx.message.author.send("`you are not in the queue, feel free to join =]`")

    @client.command(name="show")
    async def _show(ctx):

        embed = discord.Embed(colour=discord.Colour.orange())
        embed.set_author(name='Current Queue')

        for x in range(len(queue)):
            if queue[x].nick is None:
                embed.add_field(name=[x + 1, queue[x].name], value="", inline=False)
            else:
                embed.add_field(name=[x + 1, queue[x].nick], value="", inline=False)

        await ctx.channel.send(embed=embed)
        print("hi")

    client.run(TOKEN)
