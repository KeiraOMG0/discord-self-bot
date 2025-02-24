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

@commands.command()
@commands.has_permissions(ban_members=True)
async def mass_ban(self, ctx, server_id: int, num_bans: int):
    """Bans a number of users from the specified server."""
    print(f"[INFO] Starting mass ban in server: {server_id}, banning {num_bans} users...")
    
    server = ctx.bot.get_guild(server_id)

    if server is None:
        await ctx.send(f"{Fore.RED}Invalid server ID! Make sure the bot has access to the server.{Fore.RESET}")
        print("[ERROR] Invalid server ID!")
        return

    if not ctx.guild.me.guild_permissions.ban_members:
        await ctx.send(f"{Fore.RED}I don't have permission to ban members in this server.{Fore.RESET}")
        print("[ERROR] Missing ban permissions.")
        return

    await ctx.message.delete()
    banned_count = 0

    for member in server.members:
        if banned_count >= num_bans:
            break

        try:
            if not member.bot and not member.guild_permissions.administrator:
                await member.ban(reason="Mass banning", delete_message_days=0)
                banned_count += 1
                print(f"[INFO] Banned {member.name}")
                await asyncio.sleep(1)
        except discord.Forbidden:
            print(f"[ERROR] Forbidden to ban {member.name}")
            continue

    await ctx.send(f"{Fore.GREEN}✔ Banned {banned_count} users in {server.name}.{Fore.RESET}")
    print(f"[INFO] Completed mass ban: {banned_count} users banned.")

@commands.command()
@commands.has_permissions(manage_channels=True)
async def mass_channel_create(self, ctx, server_id: int, num_channels: int):
    """Creates a number of text channels in the specified server."""
    print(f"[INFO] Starting mass channel creation in server: {server_id}, creating {num_channels} channels...")
    
    server = ctx.bot.get_guild(server_id)

    if server is None:
        await ctx.send(f"{Fore.RED}Invalid server ID! Make sure the bot has access to the server.{Fore.RESET}")
        print("[ERROR] Invalid server ID!")
        return

    if not ctx.guild.me.guild_permissions.manage_channels:
        await ctx.send(f"{Fore.RED}I don't have permission to create channels in this server.{Fore.RESET}")
        print("[ERROR] Missing manage channels permissions.")
        return

    await ctx.message.delete()
    created_count = 0

    for _ in range(num_channels):
        try:
            await server.create_text_channel('nuked-channel')
            created_count += 1
            print(f"[INFO] Created channel {created_count}")
            await asyncio.sleep(1)
        except discord.Forbidden:
            print("[ERROR] Forbidden to create channel.")
            break

    await ctx.send(f"{Fore.GREEN}✔ Created {created_count} channels in {server.name}.{Fore.RESET}")
    print(f"[INFO] Completed mass channel creation: {created_count} channels created.")



@commands.command()
@commands.has_permissions(manage_channels=True)
async def mass_channel_delete(self, ctx, server_id: int, num_channels: int):
    """Deletes a number of channels in the specified server."""
    print(f"[INFO] Starting mass channel deletion in server: {server_id}, deleting {num_channels} channels...")
    
    server = ctx.bot.get_guild(server_id)

    if server is None:
        await ctx.send(f"{Fore.RED}Invalid server ID! Make sure the bot has access to the server.{Fore.RESET}")
        print("[ERROR] Invalid server ID!")
        return

    if not ctx.guild.me.guild_permissions.manage_channels:
        await ctx.send(f"{Fore.RED}I don't have permission to delete channels in this server.{Fore.RESET}")
        print("[ERROR] Missing manage channels permissions.")
        return

    await ctx.message.delete()
    deleted_count = 0

    for channel in server.text_channels:
        if deleted_count >= num_channels:
            break
        try:
            await channel.delete()
            deleted_count += 1
            print(f"[INFO] Deleted channel {channel.name}")
            await asyncio.sleep(1)
        except discord.Forbidden:
            print(f"[ERROR] Forbidden to delete channel {channel.name}")
            continue

    await ctx.send(f"{Fore.GREEN}✔ Deleted {deleted_count} channels in {server.name}.{Fore.RESET}")
    print(f"[INFO] Completed mass channel deletion: {deleted_count} channels deleted.")


@commands.command()
@commands.has_permissions(manage_roles=True)
async def mass_role_delete(self, ctx, server_id: int, num_roles: int):
    """Deletes a number of custom roles in the specified server."""
    print(f"[INFO] Starting mass role deletion in server: {server_id}, deleting {num_roles} roles...")
    
    server = ctx.bot.get_guild(server_id)

    if server is None:
        await ctx.send(f"{Fore.RED}Invalid server ID! Make sure the bot has access to the server.{Fore.RESET}")
        print("[ERROR] Invalid server ID!")
        return

    if not ctx.guild.me.guild_permissions.manage_roles:
        await ctx.send(f"{Fore.RED}I don't have permission to delete roles in this server.{Fore.RESET}")
        print("[ERROR] Missing manage roles permissions.")
        return

    await ctx.message.delete()
    deleted_count = 0

    for role in server.roles:
        if deleted_count >= num_roles:
            break
        if role.name != "@everyone":  # Skip the default everyone role
            try:
                await role.delete()
                deleted_count += 1
                print(f"[INFO] Deleted role {role.name}")
                await asyncio.sleep(1)
            except discord.Forbidden:
                print(f"[ERROR] Forbidden to delete role {role.name}")
                continue

    await ctx.send(f"{Fore.GREEN}✔ Deleted {deleted_count} roles in {server.name}.{Fore.RESET}")
    print(f"[INFO] Completed mass role deletion: {deleted_count} roles deleted.")




def setup(bot):
    bot.add_cog(CommandsCog(bot))
