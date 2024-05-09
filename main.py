import discord
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} is connected to the following server:\n')
    for server in client.guilds:
        print(f'{server.name}(id: {server.id})')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!add_role'):
        #Find role name
        role_name = message.content.split(' ')[1]
        #Search corresponding discord role
        role = discord.utils.get(message.guild.roles, name=role_name)
        #Check if role exists
        if role is None:
            await message.channel.send(f'Role "{role_name}" does not exist.')
            return
        #Role asingnment
        await message.author.add_roles(role)
        await message.channel.se