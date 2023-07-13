import requests
import time
import threading

# File path to the tokens

file_path = "data/tokens.txt"

# Counting tokens

def count_lines(file_path):
    with open(file_path, 'r') as file:
        line_count = 0
        for _ in file: 
            line_count += 1
    return line_count

print('''
  __  __                             
 |  \/  | ___   ___  _ __   ___ _ __ 
 | |\/| |/ _ \ / _ \| '_ \ / _ \ '__|
 | |  | | (_) | (_) | | | |  __/ |   
 |_|  |_|\___/ \___/|_| |_|\___|_|   

U have currently loaded {0} tokens

///TEST VERSION\\\                                                                                                                   
'''.format(count_lines(file_path)))

print('''
1. Joiner IN WORK
2. Leaver
3. Spammer
4. DM Spammer IN WORK
''')

choice = int(input("Type the number of the option you want: "))

# Joiner

if choice == 1:
    with open(file_path, "r") as file:
        tokens = file.read().splitlines()

    invite = input("invite: ")

    def join_server(token):
        header = {
            'Authorization': token
        }

        url = f"https://discord.com/api/v9/invites/{invite}"

        response = requests.post(url, headers=header)

        if response.status_code == 200:
            print("Successfully joined with token:", token)
        else:
            print("Error occurred while joining the server with token:", token, "Status code:", response.status_code)

    threads = []
    for token in tokens:
        thread = threading.Thread(target=join_server, args=(token,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

# LEAVER

if choice == 2:
    with open(file_path, "r") as file:
        tokens = file.read().splitlines()

    guild_id = input("Guild ID: ")

    def leave_server(token):
        header = {
            'Authorization': token
        }

        url = f"https://discord.com/api/v9/users/@me/guilds/{guild_id}"

        response = requests.delete(url, headers=header)

        if response.status_code == 204:
            print("Left the server successfully with token:", token)
        else:
            print("Error occurred while leaving the server with token:", token, "Status code:", response.status_code)

    threads = []
    for token in tokens:
        thread = threading.Thread(target=leave_server, args=(token,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

# SPAMMER

if choice == 3:
    with open(file_path, "r") as file:
        tokens = file.read().splitlines()

    channel_id = input("Channel ID: ")
    message_content = input("Message: ")
    repeat_count = int(input("Repeat (how many times): "))
    delay_ask = input("Do you want to delay the messages? Y/N: ")
    if delay_ask == 'Y':
        delay = int(input("Delay (in seconds): "))
    else:
        delay = 0

    payload = {
        'content': message_content
    }

    def send_message(token):
        header = {
            'Authorization': token
        }

        for i in range(repeat_count):
            url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
            time.sleep(delay)

            response = requests.post(url, json=payload, headers=header)

            if response.status_code == 200:
                print(f"Message {i + 1} sent successfully with token:", token)
            else:
                print(f"Error occurred while sending message {i + 1} with token:", token, "Status code:", response.status_code)

    threads = []
    for token in tokens:
        thread = threading.Thread(target=send_message, args=(token,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

# DM SPAMMER

if choice == 4:
    with open(file_path, "r") as file:
        tokens = file.read().splitlines()

    channel_id = input("Channel ID: ")
    message_content = input("Message: ")
    repeat_count = int(input("Repeat (how many times): "))
    delay = int(input("Delay (in seconds): "))

    payload = {
        'content': message_content
    }

    def send_dm(token):
        header = {
            'Authorization': token
        }

        for i in range(repeat_count):
            url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
            time.sleep(delay)

            response = requests.post(url, json=payload, headers=header)

            if response.status_code == 200:
                print(f"Message {i + 1} sent successfully with token:", token)
            else:
                print(f"Error occurred while sending message {i + 1} with token:", token, "Status code:", response.status_code)

    threads = []
    for token in tokens:
        thread = threading.Thread(target=send_dm, args=(token,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
