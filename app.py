import time
from telethon import TelegramClient

from modules.parseTxtFile import parseTxtFile
from modules.sender import sender

api_id = 'app_id'
api_hash = "app_hash"
database_filename = 'users_db'
what_to_hide = 'chat'
sending_delay = 30
max_messages = 40
message = '''
Your message content
'''.replace('\n', '', 1)

users = []
parseTxtFile(database_filename, users)

users_count = len(users)
counter = 0

client = TelegramClient('anon', api_id, api_hash)
async def main():
    global counter

    if users_count > 0:
        if counter < max_messages:
            while counter != users_count:
                await sender(client, users, message, counter, what_to_hide)
                counter += 1
                time.sleep(sending_delay)
        else:
            print('Достигнут лимит отправки сообщений.\nВы можете изменить переменную лимита max_messages (Не рекомендуется)')

with client:
    client.loop.run_until_complete(main())