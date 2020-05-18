command = ""
started = False
while True :
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started")
    elif command == "stop":
        if not started:
            print("Car is already Stopped!")
        else:
         started = False
         print("Car stop")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
help - to ask for help
quit - quit the game""")
    elif command == "quit":
        break
    else:
        print("Sorry I don't understand")





