# Discord Self-Bot - Mass Deleter & Spam Bot

## WARNING ⚠️
**Self-bots are against Discord's Terms of Service (ToS)!**  
Using this bot could lead to a permanent ban from Discord. **Use at your own risk!**  
This bot is designed for educational purposes only. Proceed with caution!

## Features
- **Mass Deleter**: Deletes all your messages in a specific channel.
- **Mass Spammer**: Spam a message to a specified server.
- **Mass Ban**: Ban a specified number of users from a server.
- **Mass Channel Creation**: Create a specified number of text channels in a server.
- **Mass Channel Deletion**: Delete a specified number of text channels in a server.
- **Mass Role Deletion**: Delete a specified number of roles in a server.
- **Modular Cogs**: The bot is organized into cogs for better scalability.

## Prerequisites
Before running the bot, you need the following installed:
- **Python 3.8+** (Ensure it's added to your system's PATH)
- **Git** (If you're cloning from GitHub)
- **pip** (Python package installer)

## Installation

### 1. Clone the Repository (Optional)
`git clone https://github.com/KeiraOMG/discord-self-bot.git`

cd discord-self-bot

### 2. Install Dependencies
Run the start.bat file to automatically install all required dependencies and set up the virtual environment.

### 3. Token Configuration
The bot will ask for your Discord token on the first run if config.json doesn't exist. Enter the token to allow the bot to log in and begin interacting with Discord.

### 4. Running the Bot
After installing dependencies and setting the token, you can run the bot using the following command:

`start.bat`

## How to Use the Bot
### Commands
Here are the available commands:

1. **!delete <channel_id> <limit>**
Deletes messages in the specified channel.

`channel_id`: The ID of the channel where you want to delete messages.  
`limit`: The number of messages to delete.

Example:
`!delete 123456789012345678 50`

2. **!spam <server_id> <message> <amount>**
Spams a message in the specified server.

`server_id`: The ID of the server where you want to send the message.  
`message`: The message you want to spam.  
`amount`: The amount of times you want to spam.

Commas will break the spam command.

Example:
`!spam 123456789012345678 Hello world! 10`

3. **!mass_ban <server_id> <num_bans>**
Bans a specified number of users from the specified server.

`server_id`: The ID of the server where you want to ban users.  
`num_bans`: The number of users to ban.

Example:
`!mass_ban 123456789012345678 5`

4. **!mass_channel_create <server_id> <num_channels>**
Creates a specified number of text channels in the specified server.

`server_id`: The ID of the server where you want to create channels.  
`num_channels`: The number of channels to create.

Example:
`!mass_channel_create 123456789012345678 3`

5. **!mass_channel_delete <server_id> <num_channels>**
Deletes a specified number of channels in the specified server.

`server_id`: The ID of the server where you want to delete channels.  
`num_channels`: The number of channels to delete.

Example:
`!mass_channel_delete 123456789012345678 3`

6. **!mass_role_delete <server_id> <num_roles>**
Deletes a specified number of custom roles in the specified server.

`server_id`: The ID of the server where you want to delete roles.  
`num_roles`: The number of roles to delete.

Example:
`!mass_role_delete 123456789012345678 3`

## Risk Warning ⚠️
Both the !delete, !spam, and mass commands are powerful and can result in your account being banned or disabled if overused or abused. Please use them responsibly and ensure you fully understand the potential consequences of using a self-bot.
