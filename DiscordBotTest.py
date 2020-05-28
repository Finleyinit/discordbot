import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('.yo'):
            await message.channel.send('Hello {0.author.mention} you lonely sack of shit'.format(message))

        if message.content.startswith('.keys'):
            await message.channel.send('{0.author.mention} These are all the RECOMENDED keys and average prices (around mid wipe)! https://imgur.com/a/hrheC1H/'.format(message))

        if message.content.startswith('.mapshoreline'):
            await message.channel.send('{0.author.mention} Here is a map of shoreline and its extracts ! https://imgur.com/a/wtwht5g'.format(message))

        if message.content.startswith('.mapcustoms'):
            await message.channel.send('{0.author.mention} Here is a map of customs and its extracts ! https://imgur.com/a/GZLmiqX'.format(message))

        if message.content.startswith('.mapfactory'):
            await message.channel.send('{0.author.mention} Here is a map of factory and its extracts ! https://imgur.com/a/c5zCkal'.format(message))

        if message.content.startswith('.mapinterchange'):
            await message.channel.send('{0.author.mention} Here is a map of interchange and its extracts ! https://imgur.com/a/2Qa5a7p'.format(message))

        if message.content.startswith('.maplabs'):
            await message.channel.send('{0.author.mention} Here is a map of Labs and its extracts ! Basement = https://imgur.com/a/SKabK2n Floor 1 = https://imgur.com/a/p98O0AV Floor 2 = https://imgur.com/a/tv5MNoG'.format(message))

        if message.content.startswith('.mapreserve'):
            await message.channel.send('{0.author.mention} Here is a map of reserve and its extracts ! https://imgur.com/a/Ad6iETT'.format(message))

        if message.content.startswith('.help'):
            await message.channel.send('{0.author.mention} - Here is all of the bots commands !  .keys     .mapshoreline     .mapcustoms     .mapfactory     .mapinterchange     .maplabs     .mapreserve'.format(message))









client = MyClient()
client.run('NzE1MzIxOTE3NjgyMzUyMTM4.Xs_rBw.hcxznK4gQtQZaqUqwkE-3XEtmi8')