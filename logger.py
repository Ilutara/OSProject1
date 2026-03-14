import sys
from datetime import datetime
import pytz

def log(fileName):
	with open(f"{fileName}.txt", 'w') as file:
		for msg in sys.stdin:
			msg = msg.strip()

			if msg == "QUIT":
				break
			message(file, msg)	

def message(file, str):
	spl = str.split(" ", 1)
	if len(spl) < 2:
		return

	logMsg = datetime.now().strftime("%Y-%m-%d %H:%M") + " [" + spl[0] + "] " + spl[1]
	#print(logMsg, file = sys.stdout)
	file.write(logMsg + "\n")
	file.flush()

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Please pass in the name of the log file as an argument.")
		sys.exit(1)

	fileName = sys.argv[1]
	print("File name: ", fileName)
	log(fileName)

