from discord.ext import commands

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    # current_channel = bot.get_channel('387039977495855106')
    # await bot.send_message(current_channel, 'TACOBOT ONLINE')
    # await bot.send_message(current_channel, 'Type !List for a list of commands')
    print("Taco Bot Online")
    
@bot.event    
async def on_message(message):
    # current_channel = bot.get_channel('385661961175564291')
    current_channel = message.channel
    command_list = ['!weebs' , '!powerup', '!author', '!watergame']
    command_dict = {'!weebs':'FUDGING WEEBS' , '!powerup':'Power Up is not a Water Game!', '!author':'My creator is SuperTaco9Million', '!watergame':'2018 WATER GAME CONFIRMED'}
    # print(message.content)   
    content = message.content
    content = content.lower()    
    if message.author != bot.user:
        if content.startswith('!') == True:
            if content.startswith('!List') == True:
                await bot.send_message(current_channel, command_list)
            elif content not in command_list:
                await bot.send_message(current_channel, 'That command was invalid. Type !List for a list of commands')
            else:
                for x in command_list:
                    if content.startswith(x) == True:           
                        await bot.send_message(current_channel, command_dict.get(x))
        # elif 'nek' in message.content:
        #     await bot.send_message(current_channel, 'kyfs amit')                    
bot.run('Mzg1NjYyNTc1MTkyNDQwODYz.DQTsjw.ghiTnbA_WulCX082ewYCnVrs8Oo')