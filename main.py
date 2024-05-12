import os
import getpass
import json

def get_username():
    while True:
        username = input("Enter your username: ").strip()
        if username:
            return username

def load_username():
    try:
        with open("C://AGCLI/data.json", "r") as file:
            data = json.load(file)
            return data.get("username")
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None

def save_username(username):
    os.makedirs("C://AGCLI", exist_ok=True)
    with open("C://AGCLI/data.json", "w") as file:
        json.dump({"username": username}, file)

def print_kali_terminal(username):
    hostname = getpass.getuser()
    location = "~"
    terminalEntrance = f"┌─({username}@{hostname}) - [{location}]"
    print(terminalEntrance)
    cmd = input("└─▪  ")
    translate(cmd)

Running = True  # Define Running outside the main function

def main():
    username = load_username()
    if not username:
        username = get_username()
        save_username(username)
    global Running
    while Running:
        print_kali_terminal(username)

def translate(cmd):
    global Running
    if cmd.lower() == "exit":
        Running = False


if __name__ == "__main__":
    main()
