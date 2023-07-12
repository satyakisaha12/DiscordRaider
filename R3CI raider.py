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

Token = input("token ONLY ONE: ")
channelID = input("Channel ID: ")
MessageContent = input("Message: ")
RepeatCount = int(input("How many times do you want to send the message? "))
Delay = int(input("What should the delay be (in seconds)? "))

payload = {
    'content': MessageContent
}

header = {
    'authorization': Token
}

for i in range(RepeatCount):
    url = f"https://discord.com/api/v9/channels/{channelID}/messages"
    time.sleep(Delay)

    response = requests.post(url, data=payload, headers=header)

    if response.status_code == 200:
        print(f"Message {i+1} sent successfully.")
    else:
        print(f"Error occurred while sending message {i+1}. Status code:", response.status_code)