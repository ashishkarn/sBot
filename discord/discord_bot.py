# Standard library imports
import sys
import os
import logging
from logging.config import fileConfig
import re

# Third party imports
import discord

# Path hack
sys.path.insert(0, os.path.abspath('..'))

# Local application imports
from utils.core import get_env, get_random_quote, is_keyword_mentioned # bot standard functions

# validate all mandatory files exist before starting
#assert os.path.isfile('../utils/logging_config.ini') # Logs config file
assert os.path.isfile('.env')                       # environment variables file

# Instantiate logging in accordance with config file
#fileConfig('../utils/logging_config.ini')
#logger = logging.getLogger('discord')

# Explicit start of the bot runtime
#logger.info("Started Discord bot")

try:
    # Check if it is PROD or TEST environment
    environment = get_env('ENV', __file__)
    #logger.info("Running on environment: {}".format(environment))

    # Get TOKEN environment variable
    token = get_env('TOKEN', __file__)
    #logger.info("Got Discord token")
except Exception as e:
    #logger.exception("Could not get environment variables: {}".format(str(vars(e))))
    pass

try:
    # Instatiate Discord client
    client = discord.Client()
    #logger.info("Instantiated Discord client")
except Exception as e:
    logger.exception("Error while instantiating Discord client: {}".format(str(vars(e))))
    pass

@client.event
async def on_message(message):

    # Do not reply to comments from these users, including itself (client.user)
    blocked_users = [ client.user ]
    # Bot does not reply to itself and only when mentioned
    if is_keyword_mentioned(message.content):
        #logger.info("Replied to message of user '{}' in guild '{}' / channel '{}'".format(message.author, message.guild, message.channel))
        msg = get_random_quote().format(message)
        await message.channel.send(msg)
        
print("Executing")

if __name__ == '__main__':
    try:
        # Run Discord bot
        client.run(token[:-1])
        #logger.info("Started Discord client")
    except Exception as e:
        #logger.exception("Error while running Discord client: {}".format(str(vars(e))))
        pass
