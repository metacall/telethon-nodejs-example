#!/usr/bin/env python3

#
#	MetaCall Telethon NodeJS Example by Parra Studios
#	Example of using Python Telethon in NodeJS with MetaCall.
#
#	Copyright (C) 2016 - 2020 Vicente Eduardo Ferrer Garcia <vic798@gmail.com>
#
#	Licensed under the Apache License, Version 2.0 (the "License");
#	you may not use this file except in compliance with the License.
#	You may obtain a copy of the License at
#
#		http://www.apache.org/licenses/LICENSE-2.0
#
#	Unless required by applicable law or agreed to in writing, software
#	distributed under the License is distributed on an "AS IS" BASIS,
#	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#	See the License for the specific language governing permissions and
#	limitations under the License.
#

# A simple script to print some messages.
import os
import sys
import time

from telethon import TelegramClient, events, utils

def get_env(name, message, cast=str):
    if name in os.environ:
        return os.environ[name]
    while True:
        value = input(message)
        try:
            return cast(value)
        except ValueError as e:
            print(e, file=sys.stderr)
            time.sleep(1)

session = os.environ.get('TG_SESSION', 'anonymous')
api_id = get_env('TG_API_ID', 'Enter your API ID: ', int)
api_hash = get_env('TG_API_HASH', 'Enter your API hash: ')
proxy = None  # https://github.com/Anorov/PySocks

# Create and start the client so we can make requests (we don't here)
client = TelegramClient(session, api_id, api_hash, proxy=proxy).start()

def register(cb):
    # `pattern` is a regex, see https://docs.python.org/3/library/re.html
    # Use https://regexone.com/ if you want a more interactive way of learning.
    #
    # "(?i)" makes it case-insensitive, and | separates "options".
    @client.on(events.NewMessage(pattern=r'(?i).*\b(hello|hi)\b'))
    async def handler(event):
        sender = await event.get_sender()
        name = utils.get_display_name(sender)
        cb(name, event.text)

def run():
    try:
        print('(Press Ctrl+C to stop this)')
        client.run_until_disconnected()
    finally:
        client.disconnect()
