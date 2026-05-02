import os

from colorama import Fore, Style, init
from telethon.sync import TelegramClient

init(autoreset=True)
api_id = #GET ONE YOURSELF AT https://my.telegram.org
api_hash = #GET ONE YOURSELF AT https://my.telegram.org
session_path = os.path.join(os.path.dirname(__file__), "session")
with TelegramClient(session_path, api_id, api_hash) as client:
    while True:
        mode = input(
            f"\n{Fore.MAGENTA}Enter mode (1 = send by username, 2 = send by user ID 3 = read, 0 = exit): {Style.RESET_ALL}"
        )
        if mode == "1":
            username = input("Enter username without @ : ")
            message = input("Enter message : ")
            client.send_message(username, message)
            print(f"{Fore.GREEN}Sent!{Style.RESET_ALL}")
        elif mode == "2":
            user_id = input("Enter user ID : ")
            message = input("Enter message : ")
            client.send_message(int(user_id), message)
            print(f"{Fore.GREEN}Sent!{Style.RESET_ALL}")
        elif mode == "3":
            username = input("Enter username without @ : ")
            messages = client.get_messages(username, limit=15)
            for msg in reversed(messages):
                if msg.text:
                    sender = msg.sender.username or msg.sender.first_name
                    print(f"{sender} : {msg.text}")
        elif mode == "4":
            username = input("Enter user ID : ")
            messages = client.get_messages(int(username), limit=10)
            for msg in reversed(messages):
                if msg.text:
                    sender = msg.sender.username or msg.sender.first_name
                    print(f"{sender} : {msg.text}")
        elif mode == "0":
            break
        else:
            print(f"{Fore.RED}Invalid mode{Style.RESET_ALL}")
