import json


def add_user_to_blacklist(user_id: int):
    with open("blacklist.json", "r+") as file:
        file_data = json.load(file)
        file_data["ids"].append(user_id)
    with open("blacklist.json", "w") as file:
        file.seek(0)
        json.dump(file_data, file, indent=4)


def remove_user_from_blacklist(user_id: int):
    with open("blacklist.json", "r") as file:
        file_data = json.load(file)
        file_data["ids"].remove(user_id)
    with open("blacklist.json", "w") as file:
        file.seek(0)
        json.dump(file_data, file, indent=4)

def add_status_to_config(status):
    with open("config.json", "r+") as file:
        file_data = json.load(file)
        file_data["statuses"].append(status)
    with open("config.json", "w") as file:
        file.seek(0)
        json.dump(file_data, file, indent=4)


def remove_status_from_config(status):
    with open("config.json", "r") as file:
        file_data = json.load(file)
        file_data["statuses"].remove(status)
    with open("config.json", "w") as file:
        file.seek(0)
        json.dump(file_data, file, indent=4)
