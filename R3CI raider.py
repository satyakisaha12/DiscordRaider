import requests
import time

print('''
  _____    ____     _____   _____      _____               _____   _____    ______   _____  
 |  __ \  |___ \   / ____| |_   _|    |  __ \      /\     |_   _| |  __ \  |  ____| |  __ \ 
 | |__) |   __) | | |        | |      | |__) |    /  \      | |   | |  | | | |__    | |__) |
 |  _  /   |__ <  | |        | |      |  _  /    / /\ \     | |   | |  | | |  __|   |  _  / 
 | | \ \   ___) | | |____   _| |_     | | \ \   / ____ \   _| |_  | |__| | | |____  | | \ \ 
 |_|  \_\ |____/   \_____| |_____|    |_|  \_\ /_/    \_\ |_____| |_____/  |______| |_|  \_\
                                                                                            
''')

print('''
1. Joiner
2. Leaver
3. Spammer
''')

Chose = int(input("Type the number of the option you want: "))

if Chose == 1:
    Token = input("token: ")
    Invite = input("invite: ")

    header = {
        'Authorization': Token
    }
    
    url = f"https://discord.com/api/v9/invites/{Invite}"

    response = requests.post(url, headers=header)
    
    if response.status_code == 200:
        print("Successfully joined.")
    else:
        print("Error occurred while joining the server. Status code:", response.status_code)

# LEAVER

if Chose == 2: 
    Token = input("token: ")
    GuildID = input("Guild ID: ")

    header = {
        'Authorization': Token
    }

    url = f"https://discord.com/api/v9/users/@me/guilds/{GuildID}"

    response = requests.delete(url, headers=header)

    if response.status_code == 204:
        print("Left the server successfully.")
    else:
        print("Error occurred while leaving the server. Status code:", response.status_code)

# SPAMMER

if Chose == 3:
    Token = input("token: ")
    channelID = input("Channel ID: ")
    MessageContent = input("Message: ")
    RepeatCount = int(input("Repeat (how many times): "))
    Delay = int(input("Delay (in seconds): "))

    payload = {
        'content': MessageContent
    }

    header = {
        'Authorization': Token
    }

    for i in range(RepeatCount):
        url = f"https://discord.com/api/v9/channels/{channelID}/messages"
        time.sleep(Delay)

        response = requests.post(url, json=payload, headers=header)

        if response.status_code == 200:
            print(f"Message {i+1} sent successfully.")
        else:
            print(f"Error occurred while sending message {i+1}. Status code:", response.status_code)
