import requests
import time
import threading
import shutil
import os

# Colours
purple_light = "\033[95m"
purple_dark = "\033[38;5;53m"
yellow = "\u001b[33m"
red = "\u001b[31m"

# Errors
Locked = "\u001b[31m [LOCKED] \u001b[31m"
Invalid = "\u001b[33m [INVALID] \u001b[33m"
Valid = "\033[92m [VALID] \033[92m"

# Error codes
# 403 Locked/Banned

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

def getCookie(session):
    session.get("https://discord.com", headers={}).text
    return "; ".join(f"{k}={v}" for k, v in session.cookies.items())
session = requests.Session()
response = session.get("https://discord.com")
cookie_string = getCookie(session)

def main_program():
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
        mooner_logo = '''\033[95m
                                        ███╗   ███╗ ██████╗  ██████╗ ███╗   ██╗███████╗██████╗ 
                                        ████╗ ████║██╔═══██╗██╔═══██╗████╗  ██║██╔════╝██╔══██╗
                                        ██╔████╔██║██║   ██║██║   ██║██╔██╗ ██║█████╗  ██████╔╝
                                        ██║╚██╔╝██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██╔══██╗
                                        ██║ ╚═╝ ██║╚██████╔╝╚██████╔╝██║ ╚████║███████╗██║  ██║
                                        ╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝  
                                            
                                                    youtube.com/@_R3CI dsc.gg/r3ci
        '''

        # Token count text
        token_count = "                                                 You have currently loaded {0} tokens".format(count_lines(file_path))

        # Options text
        options = '''
        

                                                                                    
                                                <1>  Joiner           <6> Is typing...       
                                                <2>  Leaver           <7> Checker 
                                                <3>  Spammer          <8>  soon
                                                <4>  Reactor          <9>  soon
                                                <5>  Webhook spammer  <10> soon
                    
        '''
        # Printing
        print(purple_dark + mooner_logo)
        print(purple_light + token_count)
        print(purple_dark + options)
        print(" ")
        choice = int(input(purple_dark + "Type the number of the option you want: "))

        # Joiner
        if choice == 1:
            tokens = open(file_path, "r+").read().splitlines()

            invite = input("invite: ")

            def join_server(token):
                header = {'Authorization': token}
                
                payload = {'session_id': cookie_string}
                url = f"https://discord.com/api/v9/invites/{invite}"

                response = requests.post(url, headers=header)

                if response.status_code == 200:
                    print("Successfully joined with token:", token[:-5] + "*****")
                else:
                    print("Error occurred while joining the server with token:", token[:-5] + "*****", "Status code:", response.status_code)

            threads = []
            for token in tokens:
                thread = threading.Thread(target=join_server, args=(token,))
                thread.start()
                threads.append(thread)

            for thread in threads:
                thread.join()

        # LEAVER
        elif choice == 2:
            tokens = open(file_path, "r+").read().splitlines()

            guild_id = input("Guild ID: ")

            def leave_server(token):
                header = {'Authorization': token}

                url = f"https://discord.com/api/v9/users/@me/guilds/{guild_id}"

                response = requests.delete(url, headers=header)

                if response.status_code == 204:
                    print("Left the server successfully with token:", token[:-5] + "*****")
                else:
                    print("Error occurred while leaving the server with token:", token[:-5] + "*****", "Status code:", response.status_code)

            threads = []
            for token in tokens:
                thread = threading.Thread(target=leave_server, args=(token,))
                thread.start()
                threads.append(thread)

            for thread in threads:
                thread.join()

        # SPAMMER
        elif choice == 3:
            tokens = open(file_path, "r+").read().splitlines()

            channel_id = input("Channel ID: ")
            message_content = input("Message: ")
            repeat_count = int(input("Repeat (how many times): "))

            payload = {'content': message_content}

            def send_message(token):
                header = {'Authorization': token}

                for i in range(repeat_count):
                    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"

                    response = requests.post(url, json=payload, headers=header)

                    if response.status_code == 200:
                        print(f"Message {i + 1} sent successfully with token:", token[:-5] + "*****")
                    else:
                        print(f"Error occurred while sending message {i + 1} with token:", token[:-5] + "*****", "Status code:", response.status_code)


            threads = []
            for token in tokens:
                thread = threading.Thread(target=send_message, args=(token,))
                thread.start()
                threads.append(thread)

            for thread in threads:
                thread.join()

        # Reactor
        elif choice == 4:
            tokens = open(file_path, "r+").read().splitlines()

            channel_id = input("Channel ID: ")
            message_id = input("Message ID: ")
            emoji = input("Emoji: ")

            for token in tokens:
                headers = {'Authorization': token}

                url = f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me"
                response = requests.put(url, headers=headers)

                if response.status_code == 204:
                    print("Reaction added successfully with token:", token[:-5] + "*****")
                else:
                    print("Error occurred while adding the reaction with token:", token[:-5] + "*****", "Status code:", response.status_code)
                    
        # Webhook spammer
        elif choice == 5:
            webhooks = open(file_pathWB, "r+").read().splitlines()
            
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
        
        # Is typing...
        elif choice == 6: 
            tokens = open(file_path, "r+").read().splitlines()
            
            channel_id = input("Channel ID: ")
            delay = int(input("Delay (in seconds): "))
            for token in tokens:
                time.sleep(delay)
                url = f"https://discord.com/api/v9/channels/{channel_id}/typing"
                headers = {'Authorization': token}
                
                response = requests.post(url, headers=headers)
                
                if response.status_code == 204:
                    print("Succes", token[:-5] + "*****")
                else:
                    print("Error", token[:-5] + "*****", "Error:", response.text)
                    
        # Checker
        elif choice == 7: 
            tokens = open(file_path, "r+").read().splitlines()
        
            for token in tokens:
                url = "https://discord.com/api/v9/users/@me/affinities/guilds"
                headers = {'Authorization': token}
                
                response = requests.get(url, headers=headers)
                
                if response.status_code == 200:
                    print("Valid Token", token[:-5] + "*****")
                elif response.status_code == 401:
                    print(Invalid, token[:-5] + "*****")
                elif response.status_code == 403:
                    print(Locked, token[:-5] + "*****")
                else:
                    print(Invalid, token[:-5] + "*****")
        else:
            print("No such option")
        print("Returning")
        time.sleep(3)
        

if __name__ == "__main__":
    threading.Thread(target=main_program).start()