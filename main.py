import sys
import subprocess

history = []

def get_string():
    global history

    s = input("Enter string: ").lower()

    if not s.isalpha():
        print("Error: only letters allowed.")
        return get_string()

    history.append(s)
    return s


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid number of arguments.")
        sys.exit(1)

    fileName = sys.argv[1]

    log = subprocess.Popen(["python3", "logger.py", fileName], stdin=subprocess.PIPE, text=True)
    encrypt = subprocess.Popen(["python3", "encrypt.py"], stdin=subprocess.PIPE, stdout=log.stdin, text=True)

    log.stdin.write("START driver")
    log.stdin.flush()

    while True:
        line = input("> ")
        cmd = line.lower()

        if cmd == "history":
            for i, s in enumerate(history):
                print(f"{i}: {s}")
            continue

        elif cmd == "password":
            pwd = input("Enter password: ").lower()
            if not pwd.isalpha():
                print("Error: only letters allowed.")
                continue

            encrypt.stdin.write(f"PASS {pwd}\n")
            encrypt.stdin.flush()

        elif cmd == "encrypt":
            s = get_string()
            encrypt.stdin.write(f"ENCRYPT {s}\n")
            encrypt.stdin.flush()

        elif cmd == "decrypt":
            s = get_string()
            encrypt.stdin.write(f"DECRYPT {s}\n")
            encrypt.stdin.flush()

        elif cmd == "quit":
            encrypt.stdin.write("QUIT\n")
            encrypt.stdin.flush()

            log.stdin.write("QUIT\n")
            log.stdin.flush()
            break

        else:
            print("Invalid command.")

    encrypt.stdin.close()
    log.stdin.close()

    encrypt.wait()
    log.wait()
