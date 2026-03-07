import sys


if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Please pass in the name of the log file as an argument.")
		sys.exit(1)

	print("File name: ", sys.argv[1])
