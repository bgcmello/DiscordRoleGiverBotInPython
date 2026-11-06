import asyncio
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.command()
@commands.has_permissions(administrator=True)
async def give(ctx, member: discord.Member, role: discord.Role, minutes: int):
  await member.add_roles(role)
  await ctx.send(
      f"✅ Given **{role.name}** to {member.mention} for **{minutes}** minutes."
  )

  await asyncio.sleep(minutes * 60)

  await member.remove_roles(role)
  await ctx.send(
      f"⏰ Time's up! **{role.name}** has been removed from {member.mention}."
  )


bot.run()