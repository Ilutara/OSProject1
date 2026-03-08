from logger import log

if __name__ == "__main__":
	while True:
		msg = input("> ")
		if msg == "QUIT":
			break
		print("IN: ", msg)
		log("testboop")
