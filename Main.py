import os
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))

intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


@bot.event
async def on_ready():
    print(f"Texas Civilian Operations Bot is online as {bot.user}")

    guild = discord.Object(id=GUILD_ID)

    try:
        synced = await bot.tree.sync(guild=guild)
        print(f"Synced {len(synced)} commands.")

    except Exception as error:
        print(error)


# =========================
# PING COMMAND
# =========================

@bot.tree.command(
    name="ping",
    description="Check if the bot is online",
    guild=discord.Object(id=GUILD_ID)
)
async def ping(interaction: discord.Interaction):

    await interaction.response.send_message(
        "🏓 Texas Civilian Operations Bot is online!",
        ephemeral=True
    )


# =========================
# MAIN PANEL
# =========================

class TexasPanel(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)


    @discord.ui.button(
        label="Civilian",
        emoji="🪪",
        style=discord.ButtonStyle.primary
    )
    async def civilian_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        await interaction.response.send_modal(
            CivilianModal()
        )


    @discord.ui.button(
        label="Vehicle",
        emoji="🚗",
        style=discord.ButtonStyle.primary
    )
    async def vehicle_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        await interaction.response.send_modal(
            VehicleModal()
        )


    @discord.ui.button(
        label="Housing",
        emoji="🏠",
        style=discord.ButtonStyle.primary
    )
    async def housing_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        await interaction.response.send_modal(
            HousingModal()
        )


    @discord.ui.button(
        label="Business",
        emoji="🏢",
        style=discord.ButtonStyle.primary
    )
    async def business_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        await interaction.response.send_modal(
            BusinessModal()
        )


    @discord.ui.button(
        label="Application",
        emoji="📋",
        style=discord.ButtonStyle.success
    )
    async def application_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        await interaction.response.send_modal(
            ApplicationModal()
        )


    @discord.ui.button(
        label="Support",
        emoji="🎟️",
        style=discord.ButtonStyle.danger
    )
    async def ticket_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        await create_ticket(interaction)


# =========================
# CIVILIAN MODAL
# =========================

class CivilianModal(discord.ui.Modal):

    def __init__(self):

        super().__init__(
            title="Texas Civilian Registration"
        )

        self.name = discord.ui.TextInput(
            label="Full Name",
            placeholder="Enter your civilian name",
            required=True
        )

        self.dob = discord.ui.TextInput(
            label="Date of Birth",
            placeholder="MM/DD/YYYY",
            required=True
        )

        self.occupation = discord.ui.TextInput(
            label="Occupation",
            placeholder="Enter occupation",
            required=True
        )

        self.add_item(self.name)
        self.add_item(self.dob)
        self.add_item(self.occupation)


    async def on_submit(
        self,
        interaction: discord.Interaction
    ):

        embed = discord.Embed(
            title="🪪 CIVILIAN REGISTERED",
            description="Your civilian registration has been submitted.",
            color=discord.Color.red()
        )

        embed.add_field(
            name="Full Name",
            value=self.name.value,
            inline=False
        )

        embed.add_field(
            name="Date of Birth",
            value=self.dob.value,
            inline=False
        )

        embed.add_field(
            name="Occupation",
            value=self.occupation.value,
            inline=False
        )

        embed.set_footer(
            text="Texas Civilian Operations"
        )

        await interaction.response.send_message(
            embed=embed,
            ephemeral=True
        )


# =========================
# VEHICLE MODAL
# =========================

class VehicleModal(discord.ui.Modal):

    def __init__(self):

        super().__init__(
            title="Vehicle Registration"
        )

        self.owner = discord.ui.TextInput(
            label="Owner Name",
            required=True
        )

        self.vehicle = discord.ui.TextInput(
            label="Vehicle Make and Model",
            required=True
        )

        self.plate = discord.ui.TextInput(
            label="License Plate",
            required=True
        )

        self.add_item(self.owner)
        self.add_item(self.vehicle)
        self.add_item(self.plate)


    async def on_submit(
        self,
        interaction: discord.Interaction
    ):

        embed = discord.Embed(
            title="🚗 VEHICLE REGISTERED",
            color=discord.Color.red()
        )

        embed.add_field(
            name="Owner",
            value=self.owner.value,
            inline=False
        )

        embed.add_field(
            name="Vehicle",
            value=self.vehicle.value,
            inline=False
        )

        embed.add_field(
            name="License Plate",
            value=self.plate.value,
            inline=False
        )

        await interaction.response.send_message(
            embed=embed,
            ephemeral=True
        )


# =========================
# HOUSING MODAL
# =========================

class HousingModal(discord.ui.Modal):

    def __init__(self):

        super().__init__(
            title="Housing Registration"
        )

        self.owner = discord.ui.TextInput(
            label="Owner Name",
            required=True
        )

        self.address = discord.ui.TextInput(
            label="Property Address",
            required=True
        )

        self.property_type = discord.ui.TextInput(
            label="Property Type",
            placeholder="House, Apartment, Condo, etc.",
            required=True
        )

        self.add_item(self.owner)
        self.add_item(self.address)
        self.add_item(self.property_type)


    async def on_submit(
        self,
        interaction: discord.Interaction
    ):

        embed = discord.Embed(
            title="🏠 PROPERTY REGISTERED",
            color=discord.Color.red()
        )

        embed.add_field(
            name="Owner",
            value=self.owner.value,
            inline=False
        )

        embed.add_field(
            name="Address",
            value=self.address.value,
            inline=False
        )

        embed.add_field(
            name="Property Type",
            value=self.property_type.value,
            inline=False
        )

        await interaction.response.send_message(
            embed=embed,
            ephemeral=True
        )


# =========================
# BUSINESS MODAL
# =========================

class BusinessModal(discord.ui.Modal):

    def __init__(self):

        super().__init__(
            title="Business Registration"
        )

        self.business_name = discord.ui.TextInput(
            label="Business Name",
            required=True
        )

        self.owner = discord.ui.TextInput(
            label="Owner Name",
            required=True
        )

        self.business_type = discord.ui.TextInput(
            label="Business Type",
            required=True
        )

        self.add_item(self.business_name)
        self.add_item(self.owner)
        self.add_item(self.business_type)


    async def on_submit(
        self,
        interaction: discord.Interaction
    ):

        embed = discord.Embed(
            title="🏢 BUSINESS REGISTERED",
            color=discord.Color.red()
        )

        embed.add_field(
            name="Business",
            value=self.business_name.value,
            inline=False
        )

        embed.add_field(
            name="Owner",
            value=self.owner.value,
            inline=False
        )

        embed.add_field(
            name="Business Type",
            value=self.business_type.value,
            inline=False
        )

        await interaction.response.send_message(
            embed=embed,
            ephemeral=True
        )


# =========================
# APPLICATION MODAL
# =========================

class ApplicationModal(discord.ui.Modal):

    def __init__(self):

        super().__init__(
            title="Texas Civilian Operations Application"
        )

        self.name = discord.ui.TextInput(
            label="Full Name",
            required=True
        )

        self.application = discord.ui.TextInput(
            label="Application Type",
            placeholder="Civilian or Staff",
            required=True
        )

        self.reason = discord.ui.TextInput(
            label="Why should you be accepted?",
            style=discord.TextStyle.paragraph,
            required=True
        )

        self.add_item(self.name)
        self.add_item(self.application)
        self.add_item(self.reason)


    async def on_submit(
        self,
        interaction: discord.Interaction
    ):

        embed = discord.Embed(
            title="📋 APPLICATION SUBMITTED",
            color=discord.Color.green()
        )

        embed.add_field(
            name="Applicant",
            value=self.name.value,
            inline=False
        )

        embed.add_field(
            name="Application",
            value=self.application.value,
            inline=False
        )

        embed.add_field(
            name="Reason",
            value=self.reason.value,
            inline=False
        )

        await interaction.response.send_message(
            embed=embed,
            ephemeral=True
        )


# =========================
# PANEL COMMAND
# =========================

@bot.tree.command(
    name="panel",
    description="Open the Texas Civilian Operations panel",
    guild=discord.Object(id=GUILD_ID)
)
async def panel(interaction: discord.Interaction):

    embed = discord.Embed(
        title="🇺🇸 TEXAS CIVILIAN OPERATIONS",
        description=(
            "Welcome to the **Texas Civilian Operations System**.\n\n"
            "Please select an option below to get started."
        ),
        color=discord.Color.red()
    )

    embed.add_field(
        name="🪪 Civilian Registration",
        value="Create and register your civilian.",
        inline=False
    )

    embed.add_field(
        name="🚗 Vehicle Registration",
        value="Register your vehicle.",
        inline=False
    )

    embed.add_field(
        name="🏠 Housing Registration",
        value="Register your property.",
        inline=False
    )

    embed.add_field(
        name="🏢 Business Registration",
        value="Register your business.",
        inline=False
    )

    embed.add_field(
        name="📋 Applications",
        value="Submit an application.",
        inline=False
    )

    embed.add_field(
        name="🎟️ Support",
        value="Create a private support ticket.",
        inline=False
    )

    embed.set_footer(
        text="Texas Civilian Operations"
    )

    await interaction.response.send_message(
        embed=embed,
        view=TexasPanel()
    )


# =========================
# CREATE SUPPORT TICKET
# =========================

async def create_ticket(
    interaction: discord.Interaction
):

    guild = interaction.guild

    existing = discord.utils.get(
        guild.text_channels,
        name=f"ticket-{interaction.user.id}"
    )

    if existing:

        await interaction.response.send_message(
            f"❌ You already have an open ticket: {existing.mention}",
            ephemeral=True
        )

        return


    overwrites = {

        guild.default_role: discord.PermissionOverwrite(
            view_channel=False
        ),

        interaction.user: discord.PermissionOverwrite(
            view_channel=True,
            send_messages=True,
            read_message_history=True
        )

    }


    channel = await guild.create_text_channel(

        name=f"ticket-{interaction.user.id}",

        overwrites=overwrites

    )


    await channel.send(

        f"🎟️ {interaction.user.mention}\n\n"
        "**Welcome to your Texas Civilian Operations support ticket.**\n"
        "Please explain how we can assist you."

    )


    await interaction.response.send_message(

        f"🎟️ Your support ticket has been created: {channel.mention}",

        ephemeral=True

    )


# =========================
# ANNOUNCEMENT COMMAND
# =========================

@bot.tree.command(
    name="announce",
    description="Send an official announcement",
    guild=discord.Object(id=GUILD_ID)
)
@app_commands.checks.has_permissions(
    manage_messages=True
)
async def announce(

    interaction: discord.Interaction,

    message: str

):

    embed = discord.Embed(

        title="📢 TEXAS CIVILIAN OPERATIONS",

        description=message,

        color=discord.Color.red()

    )

    embed.set_footer(
        text=f"Announcement by {interaction.user}"
    )

    await interaction.response.send_message(
        embed=embed
    )


# =========================
# ERROR HANDLER
# =========================

@announce.error
async def announce_error(
    interaction: discord.Interaction,
    error
):

    if isinstance(
        error,
        app_commands.MissingPermissions
    ):

        await interaction.response.send_message(
            "❌ You do not have permission to use this command.",
            ephemeral=True
        )


# =========================
# START BOT
# =========================

bot.run(TOKEN)
