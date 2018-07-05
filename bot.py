import discord
import json
import os.path
import random

client = discord.Client()
BOT_TOKEN = "BOT_TOKEN"


@client.event
async def on_ready():
    print(client.user.name)
    print("===================")


@client.event
async def on_message(message):

    if message.content.startswith("$rank help"):
        emb = (discord.Embed(title="Hatsune Miku Bot", url='http://bit.ly/2G7mB7Y', color=0x3f35f9))
        emb.add_field(name='Welcome to the help desk of the rankings', value='There is one way to rank and that is typing!!', inline=True)
        emb.add_field(name='How much xp can I get?', value="""This variates from:
100,
150,
200,
250,
300,
350,
400,
450,
500"", inline=True)
        emb.set_image(url='https://i.imgur.com/i8lO032.png')
        await client.send_message(message.channel, embed=emb)

    if message.content.lower().startswith('$profile'):
        await client.send_message(message.channel, "You have %s xp which makes you level %s %s"%(get_xp(message.author.id), get_level(message.author.id), message.author.mention))

    user_add_xp(message.author.id, random.choice ([100, 150, 200, 250, 300, 350, 400, 450, 500]))

    if get_xp(message.author.id) >= 100 and get_level(message.author.id) ==0:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 1"%(message.author.mention))

    if get_xp(message.author.id) >= 150 and get_level(message.author.id) ==1:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 2"%(message.author.mention))

    if get_xp(message.author.id) >= 225 and get_level(message.author.id) ==2:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 3"%(message.author.mention))

    if get_xp(message.author.id) >= 338 and get_level(message.author.id) ==3:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 4"%(message.author.mention))

    if get_xp(message.author.id) >= 507 and get_level(message.author.id) ==4:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 5"%(message.author.mention))

    if get_xp(message.author.id) >= 761 and get_level(message.author.id) ==5:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 6"%(message.author.mention))

    if get_xp(message.author.id) >= 1142 and get_level(message.author.id) ==6:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 7"%(message.author.mention))

    if get_xp(message.author.id) >= 1713 and get_level(message.author.id) ==7:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 8"%(message.author.mention))

    if get_xp(message.author.id) >= 2570 and get_level(message.author.id) ==8:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 9"%(message.author.mention))

    if get_xp(message.author.id) >= 3855 and get_level(message.author.id) ==9:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 10"%(message.author.mention))

    if get_xp(message.author.id) >= 5783 and get_level(message.author.id) ==10:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 11"%(message.author.mention))

    if get_xp(message.author.id) >= 8675 and get_level(message.author.id) ==11:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 12"%(message.author.mention))

    if get_xp(message.author.id) >= 13012 and get_level(message.author.id) ==12:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 13"%(message.author.mention))

    if get_xp(message.author.id) >= 19518 and get_level(message.author.id) ==13:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 14"%(message.author.mention))

    if get_xp(message.author.id) >= 29277 and get_level(message.author.id) ==14:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 15"%(message.author.mention))

    if get_xp(message.author.id) >= 43916 and get_level(message.author.id) ==15:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 16"%(message.author.mention))

    if get_xp(message.author.id) >= 65874 and get_level(message.author.id) ==16:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 17"%(message.author.mention))

    if get_xp(message.author.id) >= 98811 and get_level(message.author.id) ==17:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 18"%(message.author.mention))

    if get_xp(message.author.id) >= 148216 and get_level(message.author.id) ==18:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 19"%(message.author.mention))

    if get_xp(message.author.id) >= 222324 and get_level(message.author.id) ==19:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 20"%(message.author.mention))

    if get_xp(message.author.id) >= 333486 and get_level(message.author.id) ==20:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 21"%(message.author.mention))

    if get_xp(message.author.id) >= 500229 and get_level(message.author.id) ==21:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 22"%(message.author.mention))

    if get_xp(message.author.id) >= 750344 and get_level(message.author.id) ==22:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 23"%(message.author.mention))

    if get_xp(message.author.id) >= 1125516 and get_level(message.author.id) ==23:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 24"%(message.author.mention))

    if get_xp(message.author.id) >= 1688274 and get_level(message.author.id) ==24:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 25"%(message.author.mention))

    if get_xp(message.author.id) >= 1969653 and get_level(message.author.id) ==25:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 26"%(message.author.mention))

    if get_xp(message.author.id) >= 2954480 and get_level(message.author.id) ==26:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 27"%(message.author.mention))

    if get_xp(message.author.id) >= 4431270 and get_level(message.author.id) ==27:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 28"%(message.author.mention))

    if get_xp(message.author.id) >= 6647130 and get_level(message.author.id) ==28:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 29"%(message.author.mention))

    if get_xp(message.author.id) >= 9970695 and get_level(message.author.id) ==29:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 30"%(message.author.mention))

    if get_xp(message.author.id) >= 14956042 and get_level(message.author.id) ==30:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 31"%(message.author.mention))

    if get_xp(message.author.id) >= 22434063 and get_level(message.author.id) ==31:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 32"%(message.author.mention))

    if get_xp(message.author.id) >= 33651095 and get_level(message.author.id) ==32:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 33"%(message.author.mention))

    if get_xp(message.author.id) >= 50476642 and get_level(message.author.id) ==33:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 34"%(message.author.mention))

    if get_xp(message.author.id) >= 75714964 and get_level(message.author.id) ==34:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 35"%(message.author.mention))
                                  
    if get_xp(message.author.id) >= 94643705 and get_level(message.author.id) ==35:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 36"%(message.author.mention))
                                  
    if get_xp(message.author.id) >= 141965558 and get_level(message.author.id) ==36:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 37"%(message.author.mention))
                                  
    if get_xp(message.author.id) >= 212948337 and get_level(message.author.id) ==37:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 38"%(message.author.mention))
                                  
    if get_xp(message.author.id) >= 319422506 and get_level(message.author.id) ==38:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 39"%(message.author.mention))
                                  
    if get_xp(message.author.id) >= 479133759 and get_level(message.author.id) ==39:
        add_level(message.author.id)
        await client.send_message(message.channel, "%s! You leveled up making you rank 40"%(message.author.mention))
                                  
                                 
def user_add_xp(user_id: int, xp: int):
    if os.path.isfile("users.json"):
        try:
            with open('users.json', 'r') as fp:
                users = json.load(fp)
            users[user_id]['xp'] += xp
            with open('users.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('users.json', 'r') as fp:
                users = json.load(fp)
            users[user_id] = {}
            users[user_id]['xp'] = xp
            with open('users.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
    else:
        users = {user_id: {}}
        users[user_id]['xp'] = xp
        with open('users.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)


def get_xp(user_id: int):
    if os.path.isfile('users.json'):
        with open('users.json', 'r') as fp:
            users = json.load(fp)
        return users[user_id]['xp']
    else:
        return 0


def add_level(user_id:int):
    if os.path.isfile("users.json"):
        try:
            with open("users.json", "r") as fp:
                users = json.load(fp)
            users[user_id]["lvl"] += 1
            with open("users.json", "w") as fp:
                json.dump(users, fp, indent=4)
        except KeyError:
            with open("users.json", "r") as fp:
                users = json.load(fp)
            users[user_id]["lvl"] = 1
            with open("users.json", "w") as fp:
                json.dump(users, fp, indent=4)

def get_level(user_id:int):
    try:
        with open("users.json", "r") as fp:
            users = json.load(fp)
        return users[user_id]["lvl"]

    except KeyError:
        return 0

client.run("Mzg0NzA4OTQ2ODI2NjI1MDM1.DP2vpA.lkuzj_99tjAGqzDZfBaBhx9pF-g")
