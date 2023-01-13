import discord
from discord.ext import commands


def run_bot():
    TOKEN = 'MTA2MzI4OTk3MzU2ODE4NDMyMA.GBIajJ.cWE2WNaDEJEo-Ys86sn6dCkppB-bhqYV6YMa1c'
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
        embed.add_field(name='!join', value="Joins the queue", inline=False)
        embed.add_field(name='!leave', value="Leaves the queue", inline=False)
        embed.add_field(name='!show', value="Shows the queue", inline=False)
        await ctx.message.author.send(embed=embed)
    
    @client.command(name="join")
    async def _join(ctx, court_num):
        player = ctx.message.author
        if queue.__contains__(player):
            await ctx.message.author.send("`you are already in a queue =]`")
        else:
            queue.append(player)
            match court_num:
                case "1":
                    court1.append(player)
                    await ctx.message.author.send("`you have joined the queue for court 1`")
                case "2":
                    court2.append(player)
                    await ctx.message.author.send("`you have joined the queue for court 2`")
                case "3":
                    court3.append(player)
                    await ctx.message.author.send("`you have joined the queue for court 3`")
                case "4":
                    court4.append(player)
                    await ctx.message.author.send("`you have joined the queue for court 4`")
                case _: 
                    await ctx.channel.send("court_number must be (1-4)")
            
    @client.command(name="leave")
    async def _leave(ctx, court_num):
        player = ctx.message.author
        if queue.__contains__(player):
            queue.remove(player)
            match court_num:
                    case "1":
                        court1.remove(player)
                        await ctx.message.author.send("`you have left the queue for court 1`")
                    case "2":
                        court2.remove(player)
                        await ctx.message.author.send("`you have left the queue for court 2`")
                    case "3":
                        court3.remove(player)
                        await ctx.message.author.send("`you have left the queue for court 3`")
                    case "4":
                        court4.remove(player)
                        await ctx.message.author.send("`you have left the queue for court 4`")
                    case _: 
                        ctx.channel.send("court_number must be (1-4)")
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

    @client.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**Please pass in all requirements.**')

    client.run(TOKEN)
