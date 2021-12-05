import json


def getconfig(guildID, ctx=None):
    
    with open("config.json", 'r') as file:
        data = json.load(file)

    if str(guildID) not in data["guilds"]:
        # create config for guild
        defaultconfig = {
            "name": f"{ctx.guild.name}",
            "prefix": "chotu"
        }

        updateconfig(guildID, defaultconfig)
        return getconfig(guildID)
    else:
        return data["guilds"][str(guildID)]


def updateconfig(guildID, data):
    with open("config.json", 'r') as file:
        config = json.load(file)
    
    config['guilds'][str(guildID)] = data
    updated_data = json.dumps(config, indent=4)

    with open("config.json", 'w') as file:
        file.write(updated_data)


def get_prefix(bot, message ):
    if not message.guild:
        return "chotu"
    else:
        data = getconfig(message.guild.id, ctx=message)
        return data["prefix"]
