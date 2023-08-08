print("Welcome to TaskForce X (Camp 608)!")

# Username and password input
usr = input("State your username: ")
psw = input("Enter your password: ")

# Username and password database
username1 = "localadmin"
password1 = "Q%$1NIs0-#"

# Command input start
if usr == username1 and psw == password1:
    print("TaskForce X Authentication completed, please enter your command")
    i = 0
    while i <100:
        commandinput = input(">")
        if commandinput == "help":
            print("Welcome to TaskForce X Command Input, a secret command terminal hosted by TaskForce X.")
            print("Commands include:")
            print("1. >help (Lists all valid commands.)")
            print("2. >crash (Crashes entire command input terminal.)")
            print("3. >roastparents (A conversation example of roasting your parents.)")
            print("3. >roastchina (A change my mind meme.)")
        elif commandinput == "msfconsole":
            psw = input("Password: ")
            if psw == "okmom":
                servers = ["us_central1","us_central2","asia_central","europe_central"]
                print("Establishing connection to nearby server.")
                import time
                import random
                time.sleep(3)
                randomserver = random.randint(1,4)
                print("Nearest server detected: " + servers[randomserver])
                print("AVTR Link Console connected")
                while i <100:
                    cmdinput = input(">")
                    if cmdinput == "-h A9s2(*#+_-) -u imtrllmstr -p okmom":
                        print("Finding similar hashes to A9s2(*#+_-)...")
                        print("Found 3 match(es) to A9s2(*#+_-).")
                        selectone = input("Please select a match:")
                        if selectone == "1":
                            selectone = int(selectone)
                            print("Match " + selectone + ": s0d'1uM")
                        elif selectone == "2":
                            selectone = int(selectone)
                            print("Match " + selectone + ": ad8ch0r1ne")
                        elif selectone == "3":
                            selectone = int(selectone)
                            print("Match " + selectone + ": s812a;]^#")
                        else:
                            print("Unable to find int in reply.")
                    elif cmdinput == "-h w92(s\]&Q#$) -u imtrllmstr -p okmom":
                        print("Finding similar hashes to w92(s\]&Q#$)...")
                        print("Found 1 match(es) to w92(s\]&Q#$).")
                        selectone = input("Please select a match:")
                        if selectone == "1":
                            selectone = int(selectone)
                            print("Match " + selectone + ": okmom")
                        else:
                            print("Unable to find int in reply.")
                    elif cmdinput == "quit()":
                        quit()
                    else:
                        print("Hash unknown.")
            else:
                print("Incorrect password.")
        elif commandinput == "crash":
            while 2 == 2:
                print("0101000101010010110100")
        elif commandinput == "roastchina":
            print("If Korean pop is kpop, then Chinese rap is crap.")
        elif commandinput == "roastparents":
            print("Parent: I put a roof over your head")
            print("Parent: Clothes on your back")
            print("Parent: Food on your table")
            print("Kid: Ain't that what you supposed to do?")
            print("Kid: I'm your child")
            print("Kid: You had me")
            print("Kid: I didn't ask to be here")
            print("Kid: I'm YOURS")
        elif commandinput == "--adm()":
            confirm = input("Enter secret keycode: ")
            if confirm == "Y2K0":
                print("Control Panel successfully loaded.")
                controlpanel = input(">")
                if controlpanel == "find(internetusr)":
                    print("Enter 'arp -a' in your terminal.")
                elif controlpanel == "quit()":
                    quit()
            else:
                print("Incorrect keycode.")
        else:
            print("Enter a valid command from the list of commands.")
else:
    print("Incorrect username or password.")

