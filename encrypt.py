from logger import log
import sys

__passkey = ""

def vignere_encrypt(word):
	encrypted = ""
	if __passkey == "":
		print("ERROR Password not set")
		return
	full_length_passkey = (__passkey * (len(word) // len(__passkey))) + __passkey[:len(word) % len(__passkey)]
	#print(full_length_passkey)
	for i in range(len(word)):
		if word[i].isalpha():
			shift = ord(full_length_passkey[i].upper()) - ord('A')
			if word[i].isupper():
				encrypted += chr((ord(word[i]) + shift - ord('A')) % 26 + ord('A'))
			else:
				encrypted += chr((ord(word[i]) + shift - ord('a')) % 26 + ord('a'))
		else:
			encrypted += word[i]
	print(f"RESULT {encrypted}")
	return encrypted

def vignere_decrypt(word):
	decrypted = ""
	if __passkey == "":
		print("ERROR Password not set")
	full_length_passkey = (__passkey * (len(word) // len(__passkey))) + __passkey[:len(word) % len(__passkey)]
	#print(full_length_passkey)
	for i in range(len(word)):
		if word[i].isalpha():
			shift = ord(full_length_passkey[i].upper()) - ord('A')
			if word[i].isupper():
				decrypted += chr((ord(word[i]) - shift - ord('A')) % 26 + ord('A'))
			else:
				decrypted += chr((ord(word[i]) - shift - ord('a')) % 26 + ord('a'))
		else:
			decrypted += word[i]
	print(f"RESULT {decrypted}")
	return decrypted


if __name__ == "__main__":
	for msg in sys.stdin:
		msg = msg.strip()

		temp = msg.split(" ", 1)
		cmd = temp[0].upper()
		
		if cmd == "PASS" or cmd == "PASSKEY":
			#print(f"len is {len(temp)}")
			if len(temp) != 2:
				print("Must have argument. Try again", file=sys.stdout)
				sys.stdout.flush()
				continue
			__passkey = temp[1]
			print(f"RESULT", file=sys.stdout)
			sys.stdout.flush()
		elif cmd == "ENCRYPT":
			if len(temp) != 2:
				print("ERROR must have argument", file=sys.stdout)
				sys.stdout.flush()
				continue
			vignere_encrypt(temp[1])
		elif cmd == "DECRYPT":
			if len(temp) != 2:
				print("ERROR must have argument", file=sys.stdout)
				sys.stdout.flush()
				continue
			vignere_decrypt(temp[1])
		elif cmd == "QUIT":
			print("QUIT", file=sys.stdout)
			break
		else:
			print("Invalid option. Try again", file=sys.stdout)
			sys.stdout.flush()
			#return ERROR
