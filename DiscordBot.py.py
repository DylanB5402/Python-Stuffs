from discord.ext import commands

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    current_channel = bot.get_channel('385616164816027651')
    await bot.send_message(current_channel, 'BOT ONLINE')
    await bot.send_message(current_channel, 'Type !List for a list of commands')
    
@bot.event    
async def on_message(message):
    current_channel = message.channel
    command_list = ['!Weebs' , '!PowerUp', '!Author', '!WaterGame']
    command_dict = {'!Weebs':'FUDGING WEEBS' , '!PowerUp':'Power Up is not a Water Game!', '!Author':'My creator is SuperTaco9Million', '!WaterGame':'2018 WATER GAME CONFIRMED'}
    print(message.content)       
    if message.author != bot.user:
        if message.content.startswith('!') == True:
            if message.content.startswith('!List') == True:
                await bot.send_message(current_channel, command_list)
            elif message.content not in command_list:
                await bot.send_message(current_channel, 'That command was invalid. Type !List for a list of commands')
            else:
                for x in command_list:
                    print(x)
                    if message.content.startswith(x) == True:           
                        await bot.send_message(current_channel, command_dict.get(x))
                    
bot.run('Mzg1NjYyNTc1MTkyNDQwODYz.DQTsjw.ghiTnbA_WulCX082ewYCnVrs8Oo')