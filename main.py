import discord
from discord import app_commands


class Aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
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


# plz work
client.run("MTE3NDcxMDA2Mzc2ODgwMTMxMA.Gt5ah8.ugW8zvVgnHQSkHAYUrQ3-mjpsrIiXLv3N0RlvE")
