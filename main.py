import sys
import subprocess

history = []

def get_string(save):
    global history

    if len(history) == 0:
        str = input("Enter string: ").lower()
        if not str.isalpha():
            print("Error: only letters allowed.")
            return get_string(save)
        if save == True:
            history.append(str)
        return str
            

    option = int(input("Enter 1 if you would like to use a past string and enter 2 if you would like to use a new string: "))
    if option == 1: #history option
        for i, s in enumerate(history):
            print(f"{i}: {s}")
        nb = int(input("Enter the number of the string you would like to use: "))
        if nb >= len(history) or nb < 0:
            print("Error: index out of bounds")
            return get_string(save)
        str = history[nb]
    elif option == 2: #new string
        str = input("Enter string: ").lower()
        if not str.isalpha():
            print("Error: only letters allowed.")
            return get_string(save)
    else:
        print("Invalid option")

    if save == True:
        history.append(str)
    return str


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid number of arguments.")
        sys.exit(1)

    fileName = sys.argv[1]

    log = subprocess.Popen(["python3", "logger.py", fileName], stdin=subprocess.PIPE, text=True)
    encrypt = subprocess.Popen(["python3", "encrypt.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

    log.stdin.write("START driver\n")
    log.stdin.flush()

    while True:
        menu = "MENU: password encrypt decrypt history quit\n"
        line = input(menu+"> ")
        cmd = line.lower()

        if cmd == "history":
            for i, s in enumerate(history):
                print(f"{i}: {s}")
            continue
        elif cmd == "password":
            pwd = get_string(False)
            msg = f"PASSKEY {pwd}\n"
            encrypt.stdin.write(msg)
            encrypt.stdin.flush()
            log.stdin.write(msg)
            log.stdin.flush()
            result = encrypt.stdout.readline().strip()
            print(result)
            log.stdin.write(result+"\n")
            log.stdin.flush()
        elif cmd == "encrypt":
            s = get_string(True)
            msg = f"ENCRYPT {s}\n"
            encrypt.stdin.write(msg)
            encrypt.stdin.flush()
            log.stdin.write(msg)
            log.stdin.flush()
            result = encrypt.stdout.readline().strip()
            print(result)
            log.stdin.write(result+"\n")
            log.stdin.flush()
        elif cmd == "decrypt":
            s = get_string(True)
            msg = f"DECRYPT {s}\n"
            encrypt.stdin.write(msg)
            encrypt.stdin.flush()
            log.stdin.write(msg)
            log.stdin.flush()
            result = encrypt.stdout.readline().strip()
            print(result)
            log.stdin.write(result+"\n")
            log.stdin.flush()
        elif cmd == "quit":
            encrypt.stdin.write("QUIT\n")
            encrypt.stdin.flush()
            log.stdin.write("QUIT\n")
            log.stdin.flush()
            break
        else:
            print("Invalid command.")

    log.stdin.write("EXIT driver\n")
    log.stdin.flush()

    encrypt.stdin.close()
    log.stdin.close()

    encrypt.wait()
    log.wait()
