import discord
from discord.ext import commands
from pdf2docx import Converter
import tkinter as tk
from tkinter import filedialog
from docx import Document
from docx.enum.section import WD_ORIENTATION

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='', intents=intents)
@bot.event
async def on_ready():
    print('бот запущен! ура!')
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'привет, {member.name}! добро пожаловать на сервер!')
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('команды'):
        try:
            await message.channel.send('команды бота:\n/ping: проверка работы бота\n/загрузить файл: выбрать файл pdf с вашего компьютера для конвертации в docx')
        except:
            await message.channel.send('ошибка... ошибка... ошибка...')
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('загрузить файл'):
        try:
            root = tk.Tk()
            root.withdraw()
            pdf = filedialog.askopenfilename()
            docx = 'C:/Users/motor/OneDrive/Рабочий стол/pythonProject1/converted_file.docx'
            cv = Converter(pdf)
            cv.convert(docx)
            doc = Document(docx)
            doc.sections[0].orientation = WD_ORIENTATION.PORTRAIT
            cv.close()
            await message.channel.send('вот ваш файл:')
            with open ('C:/Users/motor/OneDrive/Рабочий стол/pythonProject1/converted_file.docx', 'rb') as f:
                file = discord.File(f)
                await message.channel.send(file=file)
        except:
            await message.channel.send('ошибка... ошибка... ошибка...')

bot.run('')
