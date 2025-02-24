# Discord Self-Bot - Mass Deleter & Spam Bot

## WARNING ⚠️
**Self-bots are against Discord's Terms of Service (ToS)!**  
Using this bot could lead to a permanent ban from Discord. **Use at your own risk!**  
This bot is designed for educational purposes only. Proceed with caution!

## Features
- **Mass Deleter**: Deletes all your messages in a specific channel.
- **Mass Spammer**: Spam a message to a specified server.
- **Modular Cogs**: The bot isa cogs for better organization and scalability.

## Prerequisites
Before running the bot, you need the following installed:
- **Python 3.8+** (Ensure it's added to your system's PATH)
- **Git** (If you're cloning from GitHub)
- **pip** (Python package installer)

## Installation

### 1. Clone the Repository (Optional)
git clone https://github.com/KeiraOMG/discord-self-bot.git

cd discord-self-bot

### 2. Install Dependencies
Run the start.bat file to automatically install all required dependencies and set up the virtual environment.

start.bat

### 3. Token Configuration
The bot will ask for your Discord token on the first run if config.json doesn't exist. Enter the token to allow the bot to log in and begin interacting with Discord.

### 4. Running the Bot
After installing dependencies and setting the token, you can run the bot using the following command:

start.bat

How to Use the Bot
Commands
Here are the available commands:

1. !delete <channel_id> <limit>
Deletes messages in the specified channel.

channel_id: The ID of the channel where you want to delete messages.
limit: The number of messages to delete.
Example:

!delete 123456789012345678 50

2. !spam <server_id> <message>
Spams a message in the specified server.

server_id: The ID of the server where you want to send the message.
message: The message you want to spam.
Example:


!spam 123456789012345678 Hello world! 10
For spam command it goes !spam {server id} {message} {amount} COMMAS WILL BREAK IT!
Risk Warning ⚠️
Both the !delete and !spam commands are powerful and can result in your account being banned or disabled if overused or abused. Please use them responsibly and ensure you fully understand the potential consequences of using a self-bot.
