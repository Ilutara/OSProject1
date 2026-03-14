PROJECT 1

3/7/2026 15:22
Goal for session: read through requirements, set up environment and documentation, decide on programming language, figure out what to build first

Since I have coded using processes in both Java and C before, I think I will usePython, to familiarize myself more with the language and the Subprocess module.

This seems to be similar to the project I did in UNIX where I was asked to code a simple shell. The difference is that this program focuses on encrypting/decrypting strings and has a history option.

Progress update:
created git repo, did initial commit, removed swp file created by keeping md fiile open as suggested

3/7/2026 16:01
Goal for session: work on log file

What was accomplished: outlined structure of file, added method to format log message and print it to file

I noticed a few things:
- file is rewritten every time i run the program. may need to fix this depending on how exactly i use this
- no new line at end of each log, easy fix
- QUIT not added to history -- change how handle

3/8/2026 12:45
Goals: fix some of the things I noticed, work on encrypt file

Will delay fixing file stuff until i figure out exactly how to call/use logger.py

For vignere cipher: what if there are non alphabetic characters? leave them as is for now
This was answered in the documentation: assume alpha input of one case. added handling for other cases just in case

making each command all caps can be annoying when testing: make it accept all lowercase too?

3/8/2026 16:14
I did accomplish my goal for the session. Namely:
- fixed newline issue
- noticed year was only 2 characters, fixed that by using %Y instead of %y
- coded the encrypt/decrypt file

I just realized I have not followed the proper format for the devlog, so I will start now.

Next session I'm thinking of doing the driver program and working with streams to make sure that part of the project works properly

3/13/2026 16:03
Goal: build most of the driver program

Future task: final tests, comments (possibly), and submission

Current problems: encrypt doesn't print results to command line, message logging is messed up

what is the flow of info?
input to driver -> send valid command to encrypt
		-> send valid command to logger? yes since encrypt doesn't have history feature
encrypt program -> result to command line (through driver or directly)?
logger program -> print to file

still have to do:
fix logging messages -- includes results
fix pipe flow -- fixed minus printing log to file for some reason
fix sessions in file? prevent complete overwrite?
password command options
log exit of driver, change start message?

note:
history lasts per run--move to file maybe?
history contains all strings entered to be encrypted or decrypted
password used by driver and passkey used by encryption?? both pass and passkey mentioned in documentation for encrypt.py
results must also be logged
python compatibility issues?
entered passwords not stored in history
once a valid string obtained for encryption/decryption store it in history

fixed:
logging messages (prints results and formatted properly)
pipe flow logic
logging start and exit of driver
menu
options when entering string (also bonus feature of not needing to do this if history is empty)
history exit option
