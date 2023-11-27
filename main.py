import discord
from discord import app_commands
from discord.ui import Button
from dotenv import load_dotenv
import asyncio
import os

intents = discord.Intents.default()
intents.members = True
intents.reactions = True

NOT_STARTED = 0
NIGHT = 1
DAY = 2

Mafia = "mafia"
Citizen = "citizen"
Dead = "dead"
Doctor = "doctor"
power_roles = ['mafia', 'doctor']


class Player:
    def __init__(self, id, server):
        self.id = id
        self.alive = 1
        self.role = None
        self.vote = None
        self.server = server
        self.ingame = 1  # changes to 0 upon m!leave, will be removed from server.players upon game end
        self.options = []  # nighttime options for power role
        self.action = 0  # if a power role, if has performed night action or not
        self.cur_choice = None  # if a power role, their choice for the night
        self.lst_choice = None  # if parity cop, last choice


async def death(channel, player, server):
    server.players[player].alive = 0


async def game_end(channel, winner, server):  # end of game message (role reveal, congratulation of winners)
    server.running = 0
    await channel.send('\n'.join([end_text[winner]] + ['The roles were as follows:'] + ['<@%s> : `%s`' % (player.id, player.role) for player in server.players.values()]))
    for key in server.players:
        if not server.players[key].ingame:
            server.players.pop(key)


async def check_end(channel, server):
    if not sum([player.role == 'mafia' for player in server.players.values() if player.alive]):  # no mafia remaining
        await game_end(channel, 'Town', server)
        return 1
    elif sum([player.role == 'mafia' for player in server.players.values() if player.alive]) >= sum(
            [player.role != 'mafia' for player in server.players.values() if player.alive]):
        await game_end(channel, 'Mafia', server)
        return 1
    return 0


async def check_votes(channel, server):
    for player in server.players.values():
        if player.alive and player.vote == None:
            return 0
    return 1


class MafiaGame:
    def __init__(self, guild):
        self.guild = guild
        self.players = []  # List of Player objects
        self.state = NOT_STARTED
        self.day_number = 0

        class Server:
            def __init__(self):
                self.players = {}  # dictionary mapping player IDs to a Player class
                self.running = 0
                self.phase = 0  # 0 for night, 1 for day
                self.actions = 0  # how many actions remain during nighttime
                self.time = 0  # how much time remains in the phase
                self.round = 0  # what day/night of the game it is (e.g. day 1, night 2, etc)
                self.saves = []  # list of doctor saves (by ID)
                self.settings = {
                    'selfsave': 0,  # doctor can save themselves
                    'conssave': 0,  # doctor can save the same person in consecutive turns
                    'continue': 0,  # continue playing even if a player leaves
                    'reveal': 0,  # reveal role of player upon death
                }
                self.setup = {
                    'Citizen': 0,
                    'doctor': 0,
                    'mafia': 0
                }

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
        channel = client.get_channel(1178635785612824626)

        await channel.send(f"Night {self.day_number} has begun!")

        # Allow Mafia to perform actions
        await self.mafia_night_actions()

    async def mafia_night_actions(self):
        mafia_players = [player for player in self.players if player.role == Mafia]
        # Implement logic for Mafia actions

    async def start_day(self):
        self.state = DAY
        # Send day start message
        channel = client.get_channel(1178635785612824626)

        await channel.send(f"Day {self.day_number} has begun!")

        # Allow players to discuss and vote
        await self.daytime_voting()

    async def daytime_voting(self):
        MAD = 1
        # Implement logic for player discussion and voting


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
async def start_game(interaction: discord.Interaction):
    guild = discord.Object(id=1174666167227531345)

    mafia_instance = MafiaGame(interaction)
    await mafia_instance.start_game()
    # await game_instance.start_game()


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
client.run(discordToken)
