import discord
import requests

client = discord.Client()

# add coins here
crypto_list = ["bitcoin", "ethereum", "litecoin"]

@client.event
async def on_ready():
    print('Bot is ready!')

@client.event
async def on_message(message):
    if message.content.startswith("!price"):
        # create the menu as an embed
        menu = discord.Embed(title="Crypto Price Menu", description="Select a cryptocurrency to view its price.")

        # add the options to the menu
        for i, crypto in enumerate(crypto_list):
            menu.add_field(name=str(i+1), value=crypto, inline=True)

        # send the menu to the user
        await message.channel.send(embed=menu)

        # wait for the user's response
        def check(m):
            return m.author == message.author and m.channel == message.channel

        response = await client.wait_for('message', check=check)

        # extract the user's choice
        choice = int(response.content) - 1
        crypto = crypto_list[choice]

        # make a request to the CoinGecko API
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()

        # extract the price of the cryptocurrency in USD
        price = data[crypto]["usd"]

        # send the price back to the user
        await message.channel.send(f"{crypto} is currently trading at ${price}")
      
      # place the discord bot token in (here)
client.run("")