from telethon.sync import TelegramClient
import os
api_id = #GET ONE YOURSELF AT https://my.telegram.org
api_hash = #GET ONE YOURSELF AT https://my.telegram.org
session_path = os.path.join(os.path.dirname(file), "session")
with TelegramClient(session_path, api_id, api_hash) as client:
    while True:
        mode = input("\nEnter mode (1 = send, 2 = read, 0 = exit): ")
        if mode == "1":
            username = input("Enter username without @ : ")
            message = input("Enter message : ")
            client.send_message(username, message)
            print("Sent!")
        elif mode == "2":
            username = input("Enter username without @ : ")
            messages = client.get_messages(username, limit=10)
            for msg in reversed(messages):
                if msg.text:
                    sender = msg.sender.username or msg.sender.first_name
                    print(f"{sender} : {msg.text}")
        elif mode == "0":
            break
        else:
            print("Invalid mode")