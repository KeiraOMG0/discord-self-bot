import discord
from discord.ext import commands
import asyncio
from colorama import Fore

class CommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Mass channel message deleter
    @commands.command()
    async def delete(self, ctx, channel_id: int, limit: int = 100):
        """Mass delete messages in a channel."""
        await ctx.message.delete()
        channel = await ctx.bot.fetch_channel(channel_id)

        if channel is None:
            await ctx.send(f"{Fore.RED}Invalid channel! Make sure it's accessible.{Fore.RESET}")
            return
        if limit <= 0:
            await ctx.send(f"{Fore.RED}You must enter a number above 0.{Fore.RESET}")
            return

        deleted = 0
        async for msg in channel.history(limit=limit):
            if msg.author.id == ctx.bot.user.id:
                try:
                    await msg.delete()
                    deleted += 1
                    await asyncio.sleep(1)  # ⏳ Increased sleep time to prevent bans
                except discord.HTTPException:
                    continue

        await ctx.send(f"{Fore.GREEN}✔ Deleted {deleted} messages in {channel.name}.{Fore.RESET}")

    @commands.command()
    async def spam(self, ctx, server_id: int, *message_parts):
        """Spam a message in all text channels of a server."""
        # Join all parts of the message into a single string (ignoring the times argument)
        message = " ".join(message_parts[:-1])  # All parts except the last one
        times = int(message_parts[-1])  # The last part is the number of times

        server = ctx.bot.get_guild(server_id)

        if server is None:
            await ctx.send(f"{Fore.RED}Invalid server! Make sure it's accessible.{Fore.RESET}")
            return

        await ctx.message.delete()  # Delete the command message
        sent_count = 0
        for channel in server.text_channels:
            if isinstance(channel, discord.TextChannel):  # Ensure it's a text channel
                for _ in range(times):
                    try:
                        await channel.send(message)
                        sent_count += 1
                        await asyncio.sleep(0.5)  # ⏳ Prevent API spamming rate limit
                    except discord.HTTPException:
                        continue

        await ctx.send(f"{Fore.GREEN}✔ Sent {sent_count} spam messages across all channels in {server.name}.{Fore.RESET}")

def setup(bot):
    await bot.add_cog(CommandsCog(bot))
