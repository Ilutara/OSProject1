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
    encrypt = subprocess.Popen(["python3", "encrypt.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

    log.stdin.write("START driver\n")
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
            s = get_string()
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
            s = get_string()
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
