import os, discord, json, random 

with open("token.json") as token:
    token = json.load(token)

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'oi':
        await message.channel.send('tudo beleza? meow, você gostaria de aprender Python?')
        return
    if message.content == 'sim':
        await message.channel.send("escreva 'links' para voce ver alguns lugares por onder podera aprender")

    links_for_python= [
        'https://www.python.org/about/gettingstarted/',
        'https://www.codecademy.com/catalog/language/python',
        'https://www.learnpython.org/',
        'https://realpython.com/',
        ]

    if message.content == 'links':
        response = random.choice(links_for_python)
        await message.channel.send(response)
    
    if 'happy birthday' in message.content.lower():
        await message.channel.send('Happy Birthday! 🎈🎉')


client.run(token)

