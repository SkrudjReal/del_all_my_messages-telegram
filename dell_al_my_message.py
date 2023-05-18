from pyrogram.errors import FloodWait
from pyrogram import Client, enums

import time

# api_id and api_hash wich you can get in https://my.telegram.org/. Create your app and get it.
api_id = # Your api_id in int format, like - 1234567
api_hash = # Your api_hash in str format like - 'deadbeef1337600613'

app = Client('ses', api_id, api_hash)

app.start()

me = app.get_me()
groups = {}
del_msg_counter = 0

num = 0 
for dialog in app.get_dialogs():
    if dialog.chat.type == enums.ChatType.GROUP or dialog.chat.type == enums.ChatType.SUPERGROUP:
        num += 1
        groups[dialog.chat.id] = {'title': dialog.chat.first_name or dialog.chat.title, 'num': num}

while True:
    group_id = int
    for key, val in groups.items():
        print(f'\033[32m{val["num"]}.\033[0m {key} \033[35m{val["title"]}\033[0m')
    while True:
        print('\033[31m0 - exit\033[0m')
        quest = input('Choose a num group for delete messages: \033[32m')
        print('\033[0m')
        if quest.isdigit():
            if int(quest) == 0:
                exit()
            group_id = [(key, val) for key, val in groups.items() if int(quest) == val['num']][0][0]
            if group_id != int:
                break
        else:
            print(f'Num({quest}) of group not found')
    for msg in app.search_messages(group_id, from_user = 'me'):
        try:
            msg.delete()
            del_msg_counter += 1
        except FloodWait as e:
            print('Have to sleep', e.x, 'seconds')
            time.sleep(e.x)
    print(f'Deleted \033[36m{del_msg_counter}\033[0m messages from chat \033[35m{groups[group_id]["title"]}\033[0m')
    input('Press any key to continue...')
    print('\n')
    del_msg_counter = 0


