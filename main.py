import discord
from discord.ext import commands
import json
import os
from colorama import init, Fore

# import the commands 
import nuke 

init(autoreset=True)  # Auto-reset color after each print

CONFIG_FILE = 'config.json'

# 🎨 ASCII ART - Branding
ASCII_ART = f"""{Fore.GREEN}
██╗  ██╗███████╗██╗██████╗  █████╗      ██████╗ ███╗   ███╗ ██████╗  ██████╗ 
██║ ██╔╝██╔════╝██║██╔══██╗██╔══██╗    ██╔═══██╗████╗ ████║██╔════╝ ██╔═══██╗
█████╔╝ █████╗  ██║██║  ██║███████║    ██║   ██║██╔████╔██║██║  ███╗██║   ██║
██╔═██╗ ██╔══╝  ██║██║  ██║██╔══██║    ██║   ██║██║╚██╔╝██║██║   ██║██║   ██║
██║  ██╗███████╗██║██████╔╝██║  ██║    ╚██████╔╝██║ ╚═╝ ██║╚██████╔╝╚██████╔╝
╚═╝  ╚═╝╚══════╝╚═╝╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚═╝     ╚═╝ ╚═════╝  ╚═════╝ 

                  {Fore.GREEN}⚠️  WARNING: Self-bots are against Discord's ToS! ⚠️
          {Fore.YELLOW}Use at your own risk! You may get banned if you spam the API.
{Fore.RESET}"""

print(ASCII_ART)

# 🔥 Ask for token on first run
if not os.path.exists(CONFIG_FILE):
    user_token = input(f"{Fore.CYAN}Enter your Discord token: {Fore.RESET}")
    with open(CONFIG_FILE, "w") as f:
        json.dump({"token": user_token}, f, indent=4)
    print(f"{Fore.GREEN}✅ Token saved to {CONFIG_FILE}{Fore.RESET}")

# Function to load token from config.json
def load_token():
    with open(CONFIG_FILE, "r") as f:
        config = json.load(f)
        return config["token"]

token = load_token()

bot = commands.Bot(command_prefix="!", self_bot=True)

@bot.event
async def on_ready():
    print(f"{Fore.GREEN}Welcome {bot.user}! Mass message deleter is ready!{Fore.RESET}")
    input(f"{Fore.RED}⚠️  Press ENTER to confirm you understand the risk before proceeding...{Fore.RESET}")
    bot.add_cog(nuke.CommandsCog(bot))


bot.run(token)
