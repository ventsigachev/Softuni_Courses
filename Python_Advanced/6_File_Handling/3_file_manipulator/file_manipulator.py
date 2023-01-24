import os

while True:
    with open("commands_file.txt", "r") as cf:
        read_line = cf.readline()[:-1]

        while not read_line == "End":
            text = read_line.split("-")
            command = text[0]

            if command == "Create":
                file = open(text[1], "w")
                file.close()
            elif command == "Add":
                content = text[2]
                file = open(text[1], "a")
                file.write(f"{content}\n")
                file.close()
            elif command == "Replace":
                old_string = text[2]
                new_string = text[3]
                try:
                    with open(text[1], "r") as rf:
                        file_text = rf.read()
                    file_text = file_text.replace(old_string, new_string)
                    with open(text[1], "w") as rf:
                        rf.write(file_text)
                except FileNotFoundError:
                    print("An error occurred")
            elif command == "Delete":
                try:
                    os.remove(text[1])
                except FileNotFoundError:
                    print("An error occurred")

            read_line = cf.readline()[:-1]
        break
