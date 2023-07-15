import requests
import time
import threading
import shutil
import os

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

while True:
    # Clearing the console
    os.system('cls' if os.name == 'nt' else 'clear')

    # File path to the tokens
    file_path = "data/tokens.txt"

    # Counting tokens
    def count_lines(file_path):
        with open(file_path, 'r') as file:
            line_count = 0
            for _ in file:
                line_count += 1
        return line_count

    # Print mooner logo
    moon_logo = '''
    __  __                             
    |  \/  | ___   ___  _ __   ___ _ __ 
    | |\/| |/ _ \ / _ \| '_ \ / _ \ '__|
    | |  | | (_) | (_) | | | |  __/ |   
    |_|  |_|\___/ \___/|_| |_|\___|_|   
                                        
    Made by _r3ci_  youtube.com/@_R3CI dsc.gg/r3ci
    '''

    # Token count print
    token_count_text = "You have currently loaded {0} tokens".format(count_lines(file_path))

    # Options print
    options = '''
    1. Joiner IN WORK           6. Soon
    2. Leaver                   7. Soon
    3. Spammer                  8. Soon
    4. DM Spammer IN WORK       9. Soon
    5. Webhook spammer          10. Soon
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
                    print(f"Message {i + 1} sent successfully with token:", token[:-5] + "**********")
                else:
                    print(f"Error occurred while sending message {i + 1} with token:", token[:-5] + "**********", "Status code:", response.status_code)

        threads = []
        for token in tokens:
            thread = threading.Thread(target=send_dm, args=(token,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    if choice == 5:
        Webhook = input("Webhook: ")
        repeat_count = int(input("Repeat (how many times): "))
        message_content = input("Message: ")

        payload = {
            "content": message_content
        }
        for i in range(repeat_count):
            response = requests.post(Webhook, json=payload)

        if response.status_code == 204:
            print("Message sent successfully!")
        else:
            print("Failed to send the message. Status code: ", response.status_code)
    print("Operation completed. Returning in 2s")
    time.sleep(2)