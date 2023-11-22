import discord
from discord import app_commands
from discord.ui import Button
from dotenv import load_dotenv
import os

intents = discord.Intents.default()
intents.members = True
intents.reactions = True

NOT_STARTED = 0
NIGHT = 1
DAY = 2

Mafia = "Mafia"
Citizen = "Citizen"
Doctor = "Doctor"


class MafiaGame:
    def __init__(self, guild):
        self.guild = guild
        self.players = []  # List of Player objects
        self.state = NOT_STARTED
        self.day_number = 0

    async def start_game(self):
        # Start the game loop
        while True:
            await self.start_night()
            await asyncio.sleep(5)  # Adjust the delay between night and day

            await self.start_day()
            await asyncio.sleep(5)  # Adjust the delay between day and night

    async def assign_roles(self):
        member_list = [member for member in self.guild.members if not member.bot]
        num_mafia = len(member_list) // 4  # You can adjust this ratio
        mafia_members = random.sample(member_list, num_mafia)

        for member in member_list:
            if member in mafia_members:
                self.players.append(Player(member, Mafia))
            else:
                self.players.append(Player(member, Citizen))

    async def start_night(self):
        self.state = NIGHT
        self.day_number += 1
        # Send night start message
        await self.guild.send(f"Night {self.day_number} has begun!")

        # Allow Mafia to perform actions
        await self.mafia_night_actions()

    async def mafia_night_actions(self):
        mafia_players = [player for player in self.players if player.role == Mafia]
        # Implement logic for Mafia actions

    async def start_day(self):
        self.state = DAY
        # Send day start message
        await self.guild.send(f"Day {self.day_number} has begun!")

        # Allow players to discuss and vote
        await self.daytime_voting()

    async def daytime_voting(self):
        MAD = 1
        # Implement logic for player discussion and voting


class Player:
    def __init__(self, member, role):
        self.member = member
        self.role = role
        self.alive = True


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


@tree.command(guild=discord.Object(id=1174666167227531345), name='embedded',
              description='gives a very nice link')  # guild specific
async def embed(interaction: discord.Interaction):
    embedded = discord.Embed(title="Sample Embed",
                             url="https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUJcmljayByb2xs",
                             description="This is an embed that will show how to build an embed and the different "
                                         "components",
                             color=0x8f3f65)
    await interaction.response.send_message(embed=embedded)


@tree.command(guild=discord.Object(id=1174666167227531345), name='start',
              description='start the game')
async def game_start(interaction: discord.Interaction):
    game = get_game(interaction.guild)
    if game and game_state == NOT_STARTED:
        if interaction.user not in [player.member for player in game.players]:
            await interaction.send_message("You have joined the game :>")
            game.players.append(Player(interaction.user, None))
        else:
            await interaction.send_message("You are already in the game :<(((")



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
        mybutton = discord.ui.Button(style=discord.ButtonStyle.blurple, label="Hello")
        self.add_item(mybutton)

        async def buttoncallback(interaction: discord.Interaction):
            pass

        mybutton.callback = buttoncallback


@tree.command(name="button", description="Sends a hello message with buttons", guild=discord.Object(
    id=1174666167227531345))
async def button(interaction: discord.Interaction):
    view = ButtonView()
    await interaction.response.send_message("Click a button!", view=view)


# Utility function to get the game instance for a guild
def get_game(guild):
    for game in games:
        if game.guild == guild:
            return game
    return None


games = []

load_dotenv()
discordToken = os.getenv('DISCORD')
# plz work
client.run(discordToken)
