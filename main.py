import random,discord,os,time
from discord.ext import commands
from modules import phSearch as ph
from modules import saveData as SaDa

token = 'YOUR_TOKEN'
prefijo = '**'
adminUser = "Demon slayer"

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix=prefijo, intents=intents)
client.remove_command('help')
SaDa.save_json(0)


# -----------Bot--------------------------------
@client.event
async def on_ready() :
	print('Iniciando...')
	print("Username: ", end='')
	print(client.user.name)
	print("Userid: ", end='')
	print(client.user.id)
	game = discord.Game(f'{prefijo}help')
	await client.change_presence(status=discord.Status.idle, activity=game)


@client.listen()
async def on_message(message) :
	try:
		if not (prefijo in message.content.lower()) and message.author.mention != '<@768647113458319390>' :
			for x in range(len(SaDa.command_key)) :
				if SaDa.command_key[x] in message.content.lower() :
					try :
						await message.channel.send(SaDa.dic.get(SaDa.command_key[x]),
																		file=discord.File(f"{SaDa.CWD}//media//{SaDa.command_key[x]}.jpg"))
					except :
						await message.channel.send(SaDa.dic.get(SaDa.command_key[x]))
	except Exception :
		pass


@client.command()
async def clear(ctx, limit) :
	try :
		role = discord.utils.get(ctx.guild.roles, name=adminUser)
		if role in ctx.author.roles :
			await ctx.channel.purge(limit=int(limit))
		else :
			await ctx.send("No puedes usar  este comando")
	except Exception as e :
		await ctx.trigger_typing()
		await ctx.send("Oops algo paso! %s" % str(e))



async def add_com(ctx, comando, say) :
	if comando in SaDa.command_key :
		await ctx.send("Este comando ya existe")
	else :
		SaDa.command_key.append(comando.lower())
		SaDa.dic[comando.lower()] = say
		SaDa.save_json(1)
		await ctx.send(f"'{comando}' Guardado")
		try :
			await ctx.message.attachments[0].save(f'{SaDa.CWD}//media//{comando.lower()}.jpg')
		except :
			pass


@client.command()
async def remove(ctx, command) :
	try :
		SaDa.command_key.remove(command)
		del SaDa.dic[command]
		SaDa.save_json(1)
		os.remove(f"{command}.jpg")
		await ctx.send(f"'{command}'Borrado")
	except :
		await ctx.send("Error")


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None) :
	# role = discord.utils.get(ctx.guild.roles, name="stand user")
	admin = ctx.author.top_role.permissions.administrator
	# if role in ctx.author.roles:
	if admin :
		print(f"{member._user} fue eliminado")
		await ctx.send(f"{ctx.author.mention} Ha baneado a {member._user}")
		await member.kick(reason=reason)
	else :
		await ctx.send("No tienes permiso para usar este  comando")


@client.command()
async def dickmeter(ctx) :
	embed = discord.Embed(colour=discord.Colour.red(), title="Dickmeter")
	largo = random.randint(0, 25)
	largo = "=" * largo
	largo = f"8{largo}D"
	embed.add_field(name=f"{ctx.author}'s dick ",
	                value=largo)
	await ctx.send(embed=embed)


@client.command()
async def hub(ctx, *args) :
    x = 10
    cont = None
    await ctx.channel.trigger_typing()
    if len(args) > 0 :
        try :
            if int(args[1]) > 0 :
                x = int(args[1])
            try :
                if int(args[2]) > 0 :
                    cont = ph.video_hub(args[0], args[2])
            except Exception :
                cont = ph.video_hub(args[0], 1)
        except Exception :
            cont = ph.video_hub(args[0], 1)
        for x in range(x):
            await ctx.send(cont[0][x] + '\n' + ph.url_key + cont[1][x])
            time.sleep(0.3)
        await ctx.send("Here is your search,{0.author.mention}".format(ctx))
    else :
        await ctx.send('Please write something,{0.author.mention}'.format(ctx))

@client.command()
async def hub_random(ctx) :
    await ctx.channel.trigger_typing()
    cont = ph.hub_video_rand()
    await ctx.send(cont[0][0]+'\n'+cont[1][0])

@client.command(pass_context=True)
async def help(ctx) :
	embed = discord.Embed(
		colour=discord.Colour.green())
	embed.set_author(name='Help : command list')
	embed.add_field(name='#dickmeter',
	                value="Medir tu pito",
	                inline=True)
	embed.add_field(name='#add_com',
	                value='añadir un comando de texto',
	                inline=False)
	embed.add_field(name='#clear',
	                value='Limpir el chat',
	                inline=False)
	await ctx.send(embed=embed)


client.run(token)
