

import discord
import os
import json
import random
from discord.ext import commands, tasks
from discord import member
from itertools import cycle
import asyncio
import datetime
import sys
import sqlite3
import platform
from pathlib import Path
import logging

client = commands.Bot(command_prefix = 'yeet-')
client.remove_command('help')



##Yeetbot does not encourage any illegal activity and if you do get in trouble because u edited it to the way it breaks the guidelines, DO NOT CONTACT ME FOR IT,  YOU WILL TAKE FULL RESPONSIBILITY##
##discord.py##
##Download Python3 and do "py -m pip install -U discord.py"##
##Created by Dank Shawn1892#0001 on Visual Studio Code##



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=1, name='YEETBOT [yeet-]', url='https://twitch.tv/shawncsgo2 (Github Version)'))
    print('Yeetbot load successful')

@client.command()
async def prefix(ctx):
    await ctx.send(f'Hello {ctx.author.mention}. Prefix is `yeet-`.')

@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member):
    if not member:
        await ctx.send("Please mention a user to use the mute function!")
        return
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
    await ctx.send(f'I have successfully muted {member.mention}')
    await member.send(f'You have been muted in {ctx.guild}')

@client.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Please mention a user to unmute!")
        return
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(role)
    await ctx.send(f'I have successfully unmuted {member.mention}')
    await member.send(f'You have been unmuted in {ctx.guild}')  

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=50):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'{ctx.author.mention} has deleted {amount} messages')

@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.send(f'Damn, {ctx.author.mention} kicked you from the server: "***{ctx.guild}***" for "***{reason}***"')
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')

@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.send(f'Damn, {ctx.author.mention} banned you from the server: "***{ctx.guild}***" for reason:  "***{reason}***"')
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention} for {reason} (Dms have been sent out :rofl:)')

@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
     user = ban_entry.user

    if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

##Information##

@client.command(aliases=['ui'])
async def userinfo(ctx, member: discord.Member):

    roles = [role for role in member.roles]

    embed = discord.Embed(
        colour=discord.Colour.dark_red()
    )

    embed.set_author(name=f'User Info - {member}')
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)

    embed.add_field(name='ID:', value=member.id)
    embed.add_field(name='Guild name:', value=member.display_name)

    embed.add_field(name='Created at;', value=member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'))
    embed.add_field(name='Joined at;', value=member.joined_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'))

    embed.add_field(name=f'Roles ({len(roles)})', value=' '.join([role.mention for role in roles]))
    embed.add_field(name='Top role:', value=member.top_role.mention)

    embed.add_field(name='Bot?', value=member.bot)

    await ctx.send(embed=embed)

##Help##

@client.command()
async def help(ctx):

    embed = discord.Embed(
        colour = discord.Colour.dark_red()
    )

    embed.set_author(name='Help')
    embed.add_field(name='License (YB™)', value='***yeet-license***')
    embed.add_field(name='Moderation', value='***yeet-moderation***')
    embed.add_field(name='Info', value='***yeet-info***')
    embed.add_field(name='More to be added!', value='|| Yeetbot™️ 2020')

    await ctx.send(embed=embed)

##Social Media Platforms (Avtenz/Shawn)##

@client.command(aliases=['sm'])
async def socialmedia(ctx):

    embed = discord.Embed(
        colour = discord.Colour.dark_red()
    )

    embed.set_author(name='Avtenz SM')
    embed.add_field(name='Avtenz Youtube', value='https://www.youtube.com/channel/UCjwHpMkqIk06TTYN5dXQzEw?view_as=subscriber')
    embed.add_field(name='Avtenz Twitter', value='NOT AVAILABLE')
    embed.add_field(name='Avtenz Twitch', value='https://twitch.tv/avtenz')
    embed.set_author(name='Shawn1892 SM')
    embed.add_field(name='Shawn1892 YT', value='NOT AVAILABLE')
    embed.add_field(name='Shawn1892 Twitter', value='NOT AVAILABLE')
    embed.add_field(name='Shawn1892 Twitch', value='https://twitch.tv/shawncsgo2')
    await ctx.send(embed=embed)

##Servers##

@client.command()
@commands.has_role('YB Server Viewer')
async def server(ctx):

    embed = discord.Embed( 
        colour=discord.Colour.dark_red()
    )

    embed.add_field(name='Avtenz Bot Testing', value='https://discord.gg/aTBNWQZ')
    embed.add_field(name='REEEEEEE server g (my alt)', value='https://discord.gg/fZjzhmP')
    embed.add_field(name='Fadeaway Gamers (Avtenz)', value='https://discord.gg/xKb8XHV')

    await ctx.send(embed=embed)

##Fun Commands##

@client.command()
async def dm(ctx):
    await ctx.send('dms')
    await ctx.author.send('Well shit! We have come to the end of the dm process! Have fun enjoying ***1*** more dm in your discord account :rofl:')

@client.command()
async def creator(ctx):
    await ctx.send('Creator of Yeetbot: <@522888094454644737> (Dank Shawn1892), dm him if u want to put a cmd there and what should it respond with')

@client.command()
async def echo(ctx, *, message=None):
    message = message
    await ctx.message.delete()
    await ctx.send(message)

@client.command()
async def bot(ctx):
    await ctx.send(f'{ctx.author.mention} you are using ***YeetBot***')

@client.command(aliases=['yeetstatus'])
async def status(ctx):
    await ctx.send('Status: Working Properly ; Streaming **YEETBOT [yeet-]** ; Twitch: https://www.twitch.tv/shawncsgo2')

@client.command()
async def version(ctx):
    await ctx.send(f'{ctx.author.mention}, the bot version is in Version Alpha 0.1.1 (Updated 5/20/20)')

##Help Commands##

@client.command()
async def moderation(ctx):

    embed = discord.Embed( 
        colour=discord.Colour.dark_red()
    )

    embed.set_author(name='Moderation Cmds')
    embed.add_field(name='Mute', value='Mutes a person {"yeet-mute @{whoever you want}"}')
    embed.add_field(name='Unmute', value='The Reversal to the Mute Cmd, again like the mute cmd, you gotta specify a person')
    embed.add_field(name='Kick', value='Kick a person in the server {yeet-kick @{Whoever you want} {reason}')
    embed.add_field(name='Ban', value='Ban a person in the server {yeet-ban @{whoever you want} {reason}}')
    embed.add_field(name='Unban', value='The Reversal to the Ban Cmd')

    await ctx.send(embed=embed)

##License (Part of the embed in yeet-help)##
@client.command()
async def license(ctx):
    
    embed = discord.Embed(
        colour=discord.Colour.dark_red()
    )

    embed.set_author(name='License Section I')
    embed.add_field(name='Section I - Bot Statement to TOS and Guidelines', value='YeetBot™️ is a bot that serves as a (to be) fun and enjoyful bot while keeping the moderation aspect safe, secure, and pretty easy to use')
    embed.set_author(name='License Section II')
    embed.add_field(name='Section II - Rules', value='YeetBot™️ like everyone else, has to follow the Discord TOS, and Guidelines. We and nobody should use the bot as: encouragement for harrasement, jokes about suicide/murder, NSFW, Gore, or anything else that VIOLATES the Discord User TOS and Guidelines. Using the bot only to manipulate and control peoples feelings will get you banned from: Every server the bot is in, the bot itself, and the Support Server (https://discord.gg/fZjzhmP)')
    
##End of License##

##Info##

@client.command()
async def info(ctx):
    
    embed = discord.Embed(
        colour=discord.Colour.dark_red()
    )

    embed.set_author(name='Info Cmds 1')
    embed.add_field(name='***yeet-userinfo/yeet-ui @(mention a user)***', value='Yeet')
    embed.add_field(name='***yeet-socialmedia***', value='Bot!')
    embed.add_field(name='***yeet-help***', value=':robot: ™')

    await ctx.send(embed=embed)

@client.command()
async def helpfun(ctx):
    
    embed = discord.Embed(
        colour=discord.Colour.dark_red()
    )
    
    embed.set_author(name='Fun Cmds')
    embed.add_field(name='Cmds: yeet-echo', value='Sends back a message you previously put')
    embed.add_field(name='Cmds: yeet-dm', value='DMs you a message')

    await ctx.send(embed=embed)

@client.command()
async def info2(ctx):
    
    embed = discord.Embed(
        colour=discord.Colour.dark_red()
    )

    embed.set_author(name='Info Cmds 2')
    embed.add_field(name='***yeet-status***', value='Yeet')
    embed.add_field(name='***yeet-status***', value='Bot!')
    embed.add_field(name='***yeet-bot***', value=':robot: ™')

    await ctx.send(embed=embed)

##Actual fucking help cmds xD)##
@client.command(aliases=['uihelp'])
async def userinfohelp(ctx):

    embed = discord.Embed(
        colour=discord.Colour.dark_red()
    )

    embed.set_author(name='UserInfo Help')
    embed.add_field(name='Cmds: yeet-userinfo, yeet-ui', value='Userinfo/UI: Find the info of a user inside a server, this includes, roles, top role, UserID, account creation, and when they joined the server')

    await ctx.send(embed=embed)

@client.command(aliases=['lhelp'])
async def licensehelp(ctx):
    
    embed = discord.Embed(
        colour=discord.Colour.dark_red()
    )

    embed.set_author(name='lhelp')
    embed.add_field(name='Cmds: yeet-license', value='Shows the License, Bot Statement, etc.')

    await ctx.send(embed=embed)

##errors##

@prefix.error
async def prefix_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('Command Fucked up')

@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention}, you are missing the following permissions: `Administrator`, please come back with these enabled")
    if isinstance(error, commands.CheckFailure):
        await ctx.send('User not in server/already muted')

@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author.mention}, you are missing the following permissions: `Administrator`, please come back with these enabled')
    if isinstance(error, commands.CheckFailure):
        await ctx.send('Command Failed: User is already muted or not in the server.')
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Mention a user to mute!')

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention}, you are missing the following permissions: `Manage Messages`, please come back with these enabled")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Specify how many messages you want to delete (1-50)')
    if isinstance(error, commands.CheckFailure):
        await ctx.send(f'I could not delete the messages, big oof')

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author.mention}, you are missing the following permissions: `Administrator`, please come back with these enabled')
    if isinstance(error, commands.CheckFailure):
        await ctx.send('Command Failed: User not in the Server')
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Mention a User to kick!')

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author.mention}, you are missing the following permissions: `Administrator`, please come back with these enabled')
    if isinstance(error, commands.CheckFailure):
        await ctx.send('Command Failed: User not in the Server or already banned. (If the user is not banned by anyone or anything, just manually ban them :/')
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Mention a User to kick!')

@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention}, you are missing the following permissions: `Administrator`, please come back with these enabled ")
    if isinstance(error, commands.CheckFailure):
        await ctx.send('Command Failed: User not banned yet')
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Specify who to unban (yeet-unban (username)#(tag numbers)) (Ex: yeet-ban Dank Shawn1892#0001')

@userinfo.error
async def userinfo_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Mention a goddamn user')
    if isinstance(error, commands.CheckFailure):
        await ctx.send('Command Failed: Bot broken xD')

@help.error
async def help_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('Command Failed: Bot broken xD')

@socialmedia.error
async def socialmedia_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('Command Failed: Bot broken xD')

@dm.error
async def dm_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('DMS are turned off smh')

@server.error
async def server_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('Command Failed: Bot broken xD')
    if isinstance(error, commands.MissingRole):
        await ctx.send('You are missing the role "YB Server Viewer"')

@echo.error
async def echo_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please say a message after "yeet-echo"')
    else:
        await ctx.send('Command Failed: Bot broken xD')

@bot.error
async def bot_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('Command Failed: Bot broken xD')

@status.error
async def status_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('Command Failed: Bot broken xD')

@userinfohelp.error
async def userinfohelp_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send('Command Failed: Bot broken xD')

##End of Errors bitch ez

client.run('TOKEN HERE')