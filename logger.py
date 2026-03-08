import sys
from datetime import datetime
import pytz

def message(file, str):
	spl = str.split(" ", 1)
	logMsg = datetime.now().strftime("%Y-%m-%d %H:%M") + " [" + spl[0] + "] " + spl[1]
	print(logMsg)
	file.write(logMsg + "\n")

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Please pass in the name of the log file as an argument.")
		sys.exit(1)

	fileName = sys.argv[1]
	print("File name: ", fileName)

	with open(f"{fileName}.txt", 'w') as file:
		while True:		
			msg = input("boop> ")
			if msg == "QUIT":
				break
			message(file, msg)	
		#file.write('Hello World!')

