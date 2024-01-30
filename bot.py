from nextcord import Interaction, SlashOption
from nextcord.ext import commands
from data import math_data
from token_1 import token
from function import math_decide_function
import nextcord

bot = commands.Bot()
guild_id_ = 1011627983410303046 # Сюда надо ввести id дс сервера
@bot.event

async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})') # Дает понять что бот заработал 
    print('------')


@bot.slash_command(name = 'kus_math' , description="Решает кусостанцкие примеры по математике",guild_ids=[guild_id_ ]) # создания слешь команды kus_math

async def kus_math(interaction: Interaction,task: str): # создания функцию которая принимает аргумент task из kus_math
    global math_data 
    try:
        await interaction.response.send_message(math_decide_function(task)) # Вызываю функцию math_decide_function из function.py 
    except KeyError:
        await interaction.response.send_message('Ты ввел что-то не так. Чтобы посмотреть таблицу введи /table')


@bot.slash_command(name = 'table' , description="Показывет таблицу",guild_ids=[guild_id_ ]) # table

async def table(interaction: Interaction):
    await interaction.response.defer()
    message = await interaction.channel.fetch_message(int(interaction.channel.last_message_id)) # ввыводит table.png 
    await interaction.channel.send(files=[nextcord.File('table.png')])
    await message.delete()
    




bot.run(token)