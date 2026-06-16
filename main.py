#!/usr/bin/env python3
import json
from typing import TypedDict

class Task(TypedDict):
    id: int
    task: str

def input_args(input: str):
    args: list[str] = []
    curr_arg = ""
    is_parenthesis_started = False
    for char in input:
        if char == '"':
            is_parenthesis_started = not is_parenthesis_started
            continue
        if char == ' ' and not is_parenthesis_started:
            if curr_arg: # prevents double spaces
                args.append(curr_arg)
            curr_arg = ""
            continue
        curr_arg += char
    args.append(curr_arg)
    return args

def main():
    content: list[Task] = []
    try:
        with open("tasks.json", "r") as f:
            content = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        content = []

    try:
        while True:
            command = input("task-cli>> ")
            args = input_args(command)
            if args[0] == 'add':
                if len(args) < 2:
                    print("Enter some value")
                    continue
                data = args[1]
                item_id: int = 0
                if not content:
                    item_id = 1
                else:
                    item_id = content[-1]["id"] + 1
                
                json_data: Task = {
                    "id": item_id,
                    "task": data
                }

                content.append(json_data)

                with open("tasks.json", "w") as f:
                    json.dump(content, f)
            elif args[0] == 'list':
                if len(content) == 0:
                    print("Enter some tasks using 'add' command")
                for i in range(len(content)):
                    print(f'{content[i]["id"]}: {content[i]["task"]}')

            elif args[0] == 'update':
                if len(args) < 3:
                    print("Enter in this format update <your_id> <your content>")
                try:
                    update_id = int(args[1])

                    new_content = [task for task in content if task["id"] != update_id]

                    if len(new_content) == len(content):
                        raise ValueError

                    content = new_content

                    update_data = args[2]

                    json_data: Task = {
                        "id": update_id,
                        "task": update_data
                    }
                    content.append(json_data)
                
                    with open("tasks.json", "w") as f:
                        json.dump(content, f)

                except ValueError:
                    print("Please enter a valid id")


            # if args[0] == 'delete':

            elif args[0] == 'exit':
                break
            else:
                print("Invalid command type help for command list")

    except KeyboardInterrupt:
        print("\nExiting...")

