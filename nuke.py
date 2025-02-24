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

    # Mass spammer for a server
    @commands.command()
    async def spam(self, ctx, server_id: int, message: str, times: int = 10):
        """Spam a message in a server."""
        server = ctx.bot.get_guild(server_id)

        if server is None:
            await ctx.send(f"{Fore.RED}Invalid server! Make sure it's accessible.{Fore.RESET}")
            return

        await ctx.message.delete()  # Delete the command message
        sent_count = 0
        for _ in range(times):
            try:
                await server.text_channels[0].send(message)
                sent_count += 1
                await asyncio.sleep(0.5)  # ⏳ Prevent API spamming rate limit
            except discord.HTTPException:
                continue

        await ctx.send(f"{Fore.GREEN}✔ Sent {sent_count} spam messages in {server.name}.{Fore.RESET}")

def setup(bot):
    await bot.add_cog(CommandsCog(bot))
