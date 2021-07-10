import time

# Goes at the beginning of the code
print("")

textDelayTime = .10
helpCommand = "//help"

def start():
    startFile = open("Files/startMem.txt", "r")
    startConfirm = startFile.read()
    startFile.close()

    def PROTOCOL_START():
        print("Welcome to this Python Pokemon Prototype!")
        time.sleep(textDelayTime)
        print("Here you will be able to catch Pokemon as well as battle with others!")
        time.sleep(textDelayTime)
        print("If at any time you are confused, feel free to type in the help command: ", helpCommand)
        
        startFile = open("Files/startMem.txt", "w")
        startFile.truncate(0)
        startFile.write("yes")
    
    if startConfirm == "no":
        PROTOCOL_START()
    else:
        print("Loading previous save file!")

start()

# Goes at the end of the code
print("")