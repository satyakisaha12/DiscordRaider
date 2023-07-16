import requests
import time
import threading
import shutil
import os

# Colours
# Purple light \033[95m
# Purple dark \033[38;5;53m
# Yellow \u001b[33m
# Red \u001b[31m

# Error codes
# 403 Locked

# Making data folder
if not os.path.exists("data"):
    os.makedirs("data")
    print("Data folder created")

# Making tokens.txt
file_path = os.path.join("data", "tokens.txt")
if not os.path.exists(file_path):
    print("Tokens file created")
    with open(file_path, 'w'):
        pass

# Making webhooks.txt
file_pathWB = os.path.join("data", "webhooks.txt")
if not os.path.exists(file_pathWB):
    print("Webhooks file created")
    with open(file_pathWB, 'w'):
        pass

while True:
    # Clearing the console
    os.system('cls' if os.name == 'nt' else 'clear')

    # File path to the tokens
    file_path = "data/tokens.txt"
    file_pathWB = "data/webhooks.txt"

    # Counting tokens
    def count_lines(file_path):
        with open(file_path, 'r') as file:
            line_count = 0
            for _ in file:
                line_count += 1
        return line_count

    # Print mooner logo
    moon_logo = '''\033[95m
    ███╗   ███╗ ██████╗  ██████╗ ███╗   ██╗███████╗██████╗ 
    ████╗ ████║██╔═══██╗██╔═══██╗████╗  ██║██╔════╝██╔══██╗
    ██╔████╔██║██║   ██║██║   ██║██╔██╗ ██║█████╗  ██████╔╝
    ██║╚██╔╝██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██╔══██╗
    ██║ ╚═╝ ██║╚██████╔╝╚██████╔╝██║ ╚████║███████╗██║  ██║
    ╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝  
                                        
    Made by _r3ci_  youtube.com/@_R3CI dsc.gg/r3ci\033[0m
    '''

    # Token count print
    token_count_text = "            \033[38;5;53mYou have currently loaded {0} tokens\033[38;5;53m".format(count_lines(file_path))

    # Options print
    options = '''
    
                | \033[95m <1> \033[95m \033[38;5;53m Joiner  \033[38;5;53m         |
                | \033[95m <2> \033[95m \033[38;5;53m Leaver \033[38;5;53m          |
                | \033[95m <3> \033[95m \033[38;5;53m Spammer \033[38;5;53m         |
                | \033[95m <4> \033[95m \033[38;5;53m Reactor \033[38;5;53m         |
                | \033[95m <5> \033[95m \033[38;5;53m Webhook spammer \033[38;5;53m |
    
    '''

    # Middle text stuff
    terminal_width = shutil.get_terminal_size().columns
    padding = (terminal_width - len(moon_logo.split('\n')[1])) // 2
    print("\n".join(" " * padding + line for line in moon_logo.split('\n')))
    print(" " * padding + token_count_text)
    print("\n".join(" " * padding + line for line in options.split('\n')))

    print(" ")
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
            
            payload = {
                'session_id': "cbdc916cbb4c6d6dbc2f5f9f36451e7f"
            }
            url = f"https://discord.com/api/v9/invites/{invite}"

            response = requests.post(url, headers=header)

            if response.status_code == 200:
                print("Successfully joined with token:", token[:-5] + "**********")
            else:
                print("Error occurred while joining the server with token:", token[:-5] + "**********", "Status code:", response.status_code)

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
                print("Left the server successfully with token:", token[:-5] + "**********")
            else:
                print("Error occurred while leaving the server with token:", token[:-5] + "**********", "Status code:", response.status_code)

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
                    print(f"Message {i + 1} sent successfully with token:", token[:-5] + "**********")
                else:
                    print(f"Error occurred while sending message {i + 1} with token:", token[:-5] + "**********", "Status code:", response.status_code)

        threads = []
        for token in tokens:
            thread = threading.Thread(target=send_message, args=(token,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    # Reactor
    if choice == 4:
        with open(file_path, "r") as file:
            tokens = file.read().splitlines()

        channel_id = input("Channel ID: ")
        message_id = input("Message ID: ")
        emoji = input("Emoji: ")

        for token in tokens:
            headers = {
                'Authorization': token
            }

            url = f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me"
            response = requests.put(url, headers=headers)

            if response.status_code == 204:
                print("Reaction added successfully with token:", token[:-5] + "**********")
            else:
                print("Error occurred while adding the reaction with token:", token[:-5] + "**********", "Status code:", response.status_code)
                
    # Webhook spammer
    if choice == 5:
        with open(file_pathWB, "r") as file:
            webhooks = file.read().splitlines()
        
        message = input("Message: ")
        repeat_count = int(input("Repeat count: "))
        
        payload = {'content': message}

        def send_webhook_message(webhook_url):
            for _ in range(repeat_count):
                response = requests.post(webhook_url, json=payload)
            
                if response.status_code == 204:
                    print("Message sent successfully to", webhook_url[:-5] + "**")
                else:
                    print("Failed to send message to", webhook_url[:-5] + "**", "Error:", response.text)
        
        threads = []
        for webhook_url in webhooks:
            thread = threading.Thread(target=send_webhook_message, args=(webhook_url,))
            thread.start()
            threads.append(thread)
        
        for thread in threads:
            thread.join()
    
    print("Operation completed. Returning in 5s")
    time.sleep(5)