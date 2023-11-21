import discord
from discord import app_commands
from discord.ui import Button


class Aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False  # we use this so the bot doesn't sync commands more than once

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:  # check if slash commands have been synced
            await tree.sync(guild=discord.Object(
                id=1174666167227531345))  # guild specific: leave blank if global (global registration can take 1-24
            # hours)
            self.synced = True
        print(f"We have logged in as {self.user}.")


# bob

client = Aclient()
tree = app_commands.CommandTree(client)


@tree.command(guild=discord.Object(id=1174666167227531345), name='start',
              description='start the game')  # guild specific
async def embed(interaction: discord.Interaction):
    embedded = discord.Embed(title="Sample Embed",
                             url="https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUJcmljayByb2xs",
                             description="This is an embed that will show how to build an embed and the different "
                                         "components",
                             color=0xFF5733)
    await interaction.response.send_message(embed=embedded)



@tree.command(guild=discord.Object(id=1174666167227531345), name='join', description='Enters a voice channel')
async def join_voice(interaction: discord.Interaction):
    # Check if the user is in a voice channel
    if interaction.user.voice:
        channel = interaction.user.voice.channel
        voice_channel = await channel.connect()
        await interaction.response.send_message(f"Joined {channel}")
    else:
        await interaction.response.send_message("You need to be in a voice channel to use this command.")


class ButtonView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_buttons()  # Remember to add this line to call the add_buttons() function

    def add_buttons(self):
        mybutton = discord.ui.Button(label="Hello")
        self.add_item(mybutton)

        async def buttoncallback(interaction: discord.Interaction):
            pass

        mybutton.callback = buttoncallback


@tree.command(name="button", description="Sends a hello message with buttons", guild=discord.Object(
    id=1174666167227531345))
async def button(interaction: discord.Interaction):
    view = ButtonView()
    await interaction.response.send_message("Click a button!", view=view)


# plz work
client.run("MTE3NDcxMDA2Mzc2ODgwMTMxMA.Gt5ah8.ugW8zvVgnHQSkHAYUrQ3-mjpsrIiXLv3N0RlvE")
