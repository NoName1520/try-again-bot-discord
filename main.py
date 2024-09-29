import os
import discord
from discord.ext import commands, tasks

from myserver import server_on

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='/', intents=intents)
bot.remove_command('help')


channel_system = 1241660740109205596
channel_log =  1241636092126433353
#/========================================================/#

#--------------------------------------------------------
#คนเข้า
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(channel_log)
    text = f"ยินดีต้อนรับ {str(member)} สู่เชิฟ {member.guild.name} @everyone "
    embed = discord.Embed(title=f"{member.name}",
                           description=text,
                           color=0x00FF00,
                           timestamp=discord.utils.utcnow())
    await channel.send(embed=embed) 
#คนออก
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(channel_log)
    text = f"ลาก่อน {member.name} ได้ออกเชิฟ {member.guild.name} ไปแล้ว @everyone "
    embed = discord.Embed(title=f"{str(member)}",
                          description=text,
                          color=0xFF0000,
                          timestamp=discord.utils.utcnow())
    await channel.send(embed=embed)
#-------------------------------------------------------
#แก้ใข
@bot.event
async def on_member_update(before, after):
    channel = bot.get_channel(channel_system)
    text = f"@{after} has bee update"
    await channel.send(text)
#ลบข้อความ
@bot.event
async def on_message_delete(message):
    channel = bot.get_channel(channel_system)
    text = f"delete message >>**{message.content}**<<"
    embed = discord.Embed(title='***message deleete***',
                          description=text,
                          color=0xFF0000,
                          timestamp=discord.utils.utcnow())
    print(embed)
    await channel.send(embed=embed)
#---------------------------------------------------------------
#message ban
@bot.event
async def on_member_ban(guild, after):
     channel = bot.get_channel(channel_system)
     text = f"{after} ได้ถูกแบนจากเชิฟ {guild}"
     embed = discord.Embed(title=f'***Ban***',
                           description=text,
                           color=0xFF0000)
     print(embed)
     await channel.send(embed=embed)
#message UnBan
@bot.event
async def on_member_unban(guild, after):
     channel = bot.get_channel(channel_system)
     text = f"{after} ได้ถุกปลดแบนแล้วจากเชิฟ {guild}"
     embed = discord.Embed(title=f"***UnBan***",
                           description=text,    
                           color=0x00FF00)
     print(embed)
     await channel.send(embed=embed)
#------------------------------------------s--------------------------
#ห้องเสียง - beta
@bot.event
async def on_voice_state_update(member, before, after):
    channel = bot.get_channel(channel_system)
    text = f"{member.name} too {before} a {after}"
    print(text)

#--------------------------------------------------------------------
@tasks.loop(seconds=10)
async def status():
    await bot.change_presence(activity=discord.Game("กำลังทำลอง"))
@bot.event
async def on_ready():
    status.start()
    print('ready')
#--------------------------------------------------------------------
@bot.command()
async def help(ctx):
    embed = discord.Embed(title='text',
                          description='Text')
    embed.add_field(name='  ')
#/=======================================================/#

server_on

bot.run(os.getenv('TOKEN'))