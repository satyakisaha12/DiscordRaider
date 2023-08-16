import requests
import time
import threading
import os
import colorama
import webbrowser
import logging
import random
import websocket
import json
import tls_client
import base64
from pystyle import Write, Colors
from colorama import Fore

# Colours
purple_light = colorama.Fore.LIGHTMAGENTA_EX
purple_dark = colorama.Fore.LIGHTMAGENTA_EX
yellow = colorama.Fore.YELLOW
red = colorama.Fore.RED
green = colorama.Fore.GREEN

# Errors
Locked = f"{red} [LOCKED]? {red}"
Invalid = f"{red} [INVALID]? {red}"
Valid = f"{colorama.Fore.GREEN} [VALID] {colorama.Fore.GREEN}"
NoAcces = f"{red} [NO ACCESS]? {red}"
Succes = f"{colorama.Fore.GREEN} [SUCCESS] {colorama.Fore.GREEN}"
RateLimit = f"{colorama.Fore.YELLOW} [RATELIMIT] {colorama.Fore.YELLOW}"
Banned = f"{red} [BANNED]? {red}"

# Error codes
# 401 Api?
# 403 Locked/Banned
# 50001 No access
# 40007 Banned from a server

# Getting fingerprint
finger_fail = False
session = requests.Session()

headers = {
        'Accept': '*/*',
        'Referer': 'https://discord.com/',
        'User-Agent': 'Mozilla/5.0'
}
response = session.get('https://discord.com/api/v9/experiments', headers=headers)

if response.status_code == 200:
    data = response.json()
    fingerprint = data["fingerprint"]
else:
    finger_fail = True

# Making data folder
if not os.path.exists("data"):
    os.makedirs("data")

# Making tokens.txt
file_path = os.path.join("data", "tokens.txt")
if not os.path.exists(file_path):
    with open(file_path, 'w'):
        pass

# Making webhooks.txt
file_pathWB = os.path.join("data", "webhooks.txt")
if not os.path.exists(file_pathWB):
    with open(file_pathWB, 'w'):
        pass

# Making logs.txt
file_path_logs = os.path.join("data", "logs.txt")
if not os.path.exists(file_path_logs):
    with open(file_path_logs, 'w'):
        pass

# VARIABLES
discord = "https://discord.com/invite/auaX4vqZra"
youtube = "https://www.youtube.com/@_R3CI_"
discord_acc = "_r3ci_"
file_path_tokens = "data/tokens.txt"
file_path_webhooks = "data/webhooks.txt"
file_path_logs = "data/logs.txt"

#Logging
log_file_path = "data/logs.txt"

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# auto token checker for cmd tiltle
def main_program():
    while True:            
        # Cleaning ocnsole
        os.system('cls')
        logging.info("console was cleared")
        
        # Counting tokens
        def count_lines(file_path):
            with open(file_path, 'r') as file:
                line_count = 0
                for _ in file:
                    line_count += 1
            return line_count
        
        # Print mooner logo with gradient effect
        Write.Print("""
                                        ███╗   ███╗ ██████╗  ██████╗ ███╗   ██╗███████╗██████╗ 
                                        ████╗ ████║██╔═══██╗██╔═══██╗████╗  ██║██╔════╝██╔══██╗
                                        ██╔████╔██║██║   ██║██║   ██║██╔██╗ ██║█████╗  ██████╔╝
                                        ██║╚██╔╝██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██╔══██╗
                                        ██║ ╚═╝ ██║╚██████╔╝╚██████╔╝██║ ╚████║███████╗██║  ██║
                                        ╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝  
        """, Colors.blue_to_purple, interval=0.000)
        logging.info("printed mooner logo")
        
        # token count shit i dont know 
        token_count = "{0}".format(count_lines(file_path))
        
        # Options text with gradient effect
        Write.Print("""
                                                            <0> Socials                                                                               
                                            |    <1>  Joiner           <6> Is typing...    |      
                                            |    <2>  Leaver           <7> Checker         |  
                                            |    <3>  Spammer          <8> Token locker    |
                                            |    <4>  Reactor          <9>  soon           |
                                            |    <5>  Webhook spammer  <10> Exit           |
        """, Colors.blue_to_purple, interval=0.000)
        logging.info("printed options")
        if finger_fail == True:
            print("")
            Write.Print("Failed getting fingerprint some features may not work", Colors.blue_to_purple, interval=0.000)
        
        # Choice
        print(" ")
        choice = int(input(purple_dark + "[>>>]: "), )
        logging.info("printed option chooser")
       
        # Socials
        if choice == 0:
            logging.info("chose socials (0)")
            Write.Print('''
<1> Discord server
<2> Youtube    
<3> Discord acc                
                  ''', Colors.blue_to_purple, interval=0.000)
            logging.info("printed social options")
            choice_socials = int(input(purple_dark + 
"[>>>]: "))
            logging.info("printed option choser for socials")
            if choice_socials == 1:
                webbrowser.open(discord)
                logging.info("chose discord (socials) (1)")
            elif choice_socials == 2:
                webbrowser.open(youtube)
                logging.info("chose youtube (socials) (2)")
            elif choice_socials == 3:
                print(discord_acc)
                logging.info("chose discord_acc (socials) (3)")
            else:
                print ("no such option")
                logging.info("put in a option that doesnt exist (socials)")
            
        # Joiner
        if choice == 1:
            logging.info("chose joiner (1)")
            with open(file_path_tokens, "r") as file:
                tokens = file.read().splitlines()

            invite = Write.Input(f"Invite: ", Colors.blue_to_purple, interval=0.000)
            logging.info("put in invite (joiner)")
            for token in tokens:
                def __init__(self, token) -> None:
                    self.session = tls_client.Session(client_identifier='chrome_108')
                ws = websocket.WebSocket()
                ws.connect("wss://gateway.discord.gg/?v=9&encoding=json"); ws.send(json.dumps({"op": 2,"d": {"token": token, "properties": {"$os": "windows","$browser": "Discord","$device": "desktop"},"presence": {"status": random.choice(["online", "dnd", "idle"]),"since": 0,"activities": [],"afk": False}}}))
                try:
                    recv = json.loads(ws.recv())
                    session = recv["d"]["session_id"]
                    break
                except:
                    pass
            
            def joiner(token, session):
                headers = {'accept':  '*/*'}
                headers = {'accept-language': 'pl-PL, pl;q=0.9'}
                headers = {'cache-control': 'no-cache'}
                headers = {'authorization': token}
                headers = {'content-type': 'application/json'}
                headers = {'origin': 'https://discord.com'}
                headers = {'cookie': '__dcfduid=676e06b0565b11ed90f9d90136e0396b; __sdcfduid=676e06b1565b11ed90f9d90136e0396bc28dfd451bebab0345b0999e942886d8dfd7b90f193729042dd3b62e2b13812f; __cfruid=1cefec7e9c504b453c3f7111ebc4940c5a92dd08-1666918609; locale=en-US'}
                headers = {'pragma': 'no-cache'}
                headers = {'referer': 'https://discord.com/channels/@me'}  
                headers = {'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"'}
                headers = {'sec-ch-ua-mobile': '?0'}
                headers = {'sec-ch-ua-platform': '"Windows"'}
                headers = {'sec-fetch-dest': 'empty'}
                headers = {'sec-fetch-mode': 'cors'}
                headers = {'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyLUZSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA3LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlcGVhc2VfY2hhbm5lcCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE1NDc1MCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='}
                headers = { 'x-debug-options': 'bugReporterEnabled'}
                headers = {'sec-fetch-site': 'same-origin'}
                headers = {'x-discord-locale': 'en-US'}
                headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
                payload = {'session_id': session}

                response = requests.post(f"https://discord.com/api/v9/invites/{invite}", json=payload, headers=headers)

                if response.status_code == 200:
                    print(Succes, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("Joiner succes")
                elif response.status_code == 401:
                    print(Invalid, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("Joiner invalid token")
                elif response.status_code == 403:
                    print(Locked, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("Joiner locked token")
                elif response.status_code == 429:
                    print(Invalid, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("Joiner invalid token")
                elif response.status_code == 40007:
                    print(Banned, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("Joiner banned token")
                else:
                    print(Invalid, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("Joiner invalid token")

            threads = []
            for token in tokens:
                thread = threading.Thread(target=joiner, args=(token,))
                thread.start()
                threads.append(thread)
                
            for thread in threads:
                thread.join()

        # LEAVER
        elif choice == 2:
            logging.info("chose leaver (2)")
            with open(file_path_tokens, "r") as file:
                tokens = file.read().splitlines()

            guild_id = Write.Input("Guild ID: ", Colors.blue_to_purple, interval=0.000)
            logging.info("put in guild id (leaver)")

            def leaver(token):
                header = {'Authorization': token}

                url = f"https://discord.com/api/v9/users/@me/guilds/{guild_id}"

                response = requests.delete(url, headers=header)

                if response.status_code == 204:
                    print(Succes, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("leaver succes")
                elif response.status_code == 401:
                    print(Invalid, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("leaver invalid token")
                elif response.status_code == 403:
                    print(Locked, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("leaver locked token")
                else:
                    print(Invalid, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("leaver invalid token")

            threads = []
            for token in tokens:
                thread = threading.Thread(target=leaver, args=(token,))
                thread.start()
                threads.append(thread)
                
            for thread in threads:
                thread.join()

        # SPAMMER
        elif choice == 3:
            logging.info("chose spammer (3)")
            with open(file_path_tokens, "r") as file:
                tokens = file.read().splitlines()

            channel_id = input("Channel ID: ")
            logging.info("put in channel id")
            message_content = input("Message: ")
            logging.info("put in message content")
            repeat_count = int(input("Repeat count (How many times): "))
            logging.info("put in repeat count")
        
            def spammer(token):
                url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
                headers = {'Authorization': token}
                payload = {'content': message_content}

                for _ in range(repeat_count):
                    response = requests.post(url, json=payload, headers=headers)
                    if response.status_code == 200:
                        print(Succes, purple_light + token[:-5] + "*****", yellow, response)
                        logging.info("spammer succes")
                    elif response.status_code == 401:
                        print(Invalid, purple_light + token[:-5] + "*****", yellow, response)
                        logging.info("spammer invalid token")
                    elif response.status_code == 429:
                        print(RateLimit, purple_light + token[:-5] + "*****", yellow, response)
                        logging.info("spammer ratelimit (use proxies to bypass)")
                    elif response.status_code == 403:
                        print(Invalid, "/", Banned, purple_light + token[:-5] + "*****", yellow, response)
                        logging.info("spammer invalid or banned token")
                    else:
                        print("Unknown Error", purple_light + token[:-5] + "*****", yellow, response)
                        logging.info("spammer unknown error")

            threads = []
            for token in tokens:
                thread = threading.Thread(target=spammer, args=(token,))
                thread.start()
                threads.append(thread)
                
            for thread in threads:
                thread.join()

        # Reactor
        elif choice == 4:
            logging.info("chose reactor (4)")
            with open(file_path_tokens, "r") as file:
                tokens = file.read().splitlines()

            channel_id = Write.Input("Channel ID: ", Colors.blue_to_purple, interval=0.000)
            logging.info("put in channel id")
            message_id = Write.Input("Message ID: ", Colors.blue_to_purple, interval=0.000)
            logging.info("put in message id")
            emoji = Write.Input("Emoji (use win + .): ", Colors.blue_to_purple, interval=0.000)
            logging.info("put in emoji")

            def reactor(token):
                headers = {'Authorization': token}
                url = f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me"

                response = requests.put(url, headers=headers)
                if response.status_code == 204:
                    print(Succes, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("reactor succes")
                elif response.status_code == 401:
                    print(Invalid, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("reactor invalid token")
                elif response.status_code == 403:
                    print(Locked, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("reactor locked token")
                else:
                    print(Invalid, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("reactor invalid token")

            threads = []
            for token in tokens:
                thread = threading.Thread(target=reactor, args=(token,))
                thread.start()
                threads.append(thread)
                
            for thread in threads:
                thread.join()

        # Webhook spammer
        elif choice == 5:
            logging.info("chose webhook spammer (5)")
            with open(file_path_webhooks, "r") as file:
                webhooks = file.read().splitlines()

            message = Write.Input("Message: ", Colors.blue_to_purple, interval=0.000)
            logging.info("put in message")
            repeat_count_str = Write.Input("Repeat count: ", Colors.blue_to_purple, interval=0.000)
            repeat_count = int(repeat_count_str)
            logging.info("put in repeat count")

            def webhook_spammer(webhook_url, message, repeat_count):
                for _ in range(repeat_count):
                    
                    payload = {'content': message}
                    
                    response = requests.post(webhook_url, json=payload)

                    if response.status_code == 204:
                        print(Succes, purple_light + webhook_url[:-5] + "*****", yellow, response)
                        logging.info("webhook spammer succes")
                    elif response.status_code == 401:
                        print(Invalid, purple_light + webhook_url[:-5] + "*****", yellow, response)
                        logging.info("webhook spammer invalid webhook")
                    else:
                        print(Invalid, purple_light + webhook_url[:-5] + "*****", yellow, response)
                        logging.info("webhook spammer invalid webhook")

            threads = []
            for webhook_url in webhooks:
                thread = threading.Thread(target=webhook_spammer, args=(webhook_url, message, repeat_count))
                thread.start()
                threads.append(thread)

            for thread in threads:
                thread.join()

        # Is typing...
        elif choice == 6:
            logging.info("chose is typing (6)")
            with open(file_path_tokens, "r") as file:
                tokens = file.read().splitlines()

            channel_id = Write.Input("Channel ID: ", Colors.blue_to_purple, interval=0.000)
            logging.info("put in channel id")
            logging.info("put in deleay")
            url = f"https://discord.com/api/v9/channels/{channel_id}/typing"

            def is_typing(token):
                headers = {'Authorization': token}
                response = requests.post(url, headers=headers)

                if response.status_code == 204:
                    print(Succes, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("is typing succes")
                elif response.status_code == 401:
                    print(Invalid, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("is typing invalid token")
                elif response.status_code == 403:
                    print(Locked, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("is typing locked token")
                else:
                    print(Invalid, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("is typing invalid token")

            threads = []
            for token in tokens:
                thread = threading.Thread(target=is_typing, args=(token,))
                thread.start()
                threads.append(thread)
                
            for thread in threads:
                thread.join()

        # Checker
        elif choice == 7:
            logging.info("chose checker (7)")
            with open(file_path_tokens, "r") as file:
                tokens = file.read().splitlines()

            def checker(token):
                url = "https://discord.com/api/v9/users/@me/affinities/guilds"
                headers = {'Authorization': token}
                response = requests.get(url, headers=headers)

                if response.status_code == 200:
                    print(Valid, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("checker valid token")
                elif response.status_code == 401:
                    print(Invalid, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("checker invalid token")
                elif response.status_code == 403:
                    print(Locked, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("checker locked token")
                else:
                    print(Invalid, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("checker invalid token")

            threads = []
            for token in tokens:
                thread = threading.Thread(target=checker, args=(token,))
                thread.start()
                threads.append(thread)
                
            for thread in threads:
                thread.join()

        # Token locker
        elif choice == 8:
            logging.info("chose token locker (8)")
            with open(file_path_tokens, "r") as file:
                tokens = file.read().splitlines()
            Write.Print("ARE U SURE U WANT TO **LOCK** ALL THE TOKENS IN TOKENS.TXT? y/n", Colors.blue_to_purple, interval=0.000)
            token_locker_confirm = Write.Input("[>>>]: ", Colors.blue_to_purple, interval=0.000)
            
            def token_locker(token):
                if token_locker_confirm == "y" or "Y":
                    logging.info("Token locker was confirmed")
                    logging.info("token locking has started")
                    Write.Print("Reccomend using like 2-3 times to make sure tokens are locked", Colors.blue_to_purple, interval=0.000)
                    payload = {"bio": "."}
                    headers = {'Authorization': token}
                    url = "https://discord.com/api/v9/users/%40me/profile"
                    response = requests.patch(url, json=payload, headers=headers)

                    if response.status_code == 200:
                        print(Succes, purple_light + token[:-5] + "*****", yellow, response)
                        logging.info("token locker succes")
                    elif response.status_code == 401:
                        print(Invalid, purple_light + token[:-5] + "*****", yellow, response)
                        logging.info("token locker invalid token")
                    elif response.status_code == 403:
                        print(Locked, purple_light + token[:-5] + "*****", yellow, response)
                        logging.info("token locker locked token")
                    else:
                        print(Invalid, purple_light + token[:-5] + "*****", yellow, response)
                        logging.info("token locker invalid token")

                    threads = []
                    for token in tokens:
                        thread = threading.Thread(target=token_locker, args=(token,))
                        thread.start()
                        threads.append(thread)
                        
                    for thread in threads:
                        thread.join()
                
        elif choice == 10:
            logging.info("exited (10)")
            break
        elif choice == 100:
            logging.info("entered the TEST SPACE")
            Write.Print("This is a testing space for me (R3CI) wired stuff can be here so I recommend re-opening",Colors.blue_to_purple, interval=0.000)
            print("")
            print(f"tkns {token_count}")

        else:
            print("No such option")
            logging.info("put in an option that doesn't exist")

        Write.Print("Returning in 3s", Colors.blue_to_purple, interval=0.000)
        time.sleep(3)
        logging.info("returned")


if __name__ == "__main__":
    main_program()