import time, glob
from os import listdir
from os.path import isfile, join

# Goes at the beginning of the code
print("")

textDelayTime = .10
helpCommand = "//help"

def start():
    startFile = open("Files/startMem.txt", "r")
    startConfirm = startFile.read()
    startFile.close()

    fileDirectory = "C:/Users/hamza/Documents/GitHub/Pokemon-Prototype/Files"

    filesInDir = [f for f in listdir(fileDirectory) if isfile(join(fileDirectory, f))]

    if "saveDat.txt" in filesInDir:
        saveDatTrue = True
    else:
        saveDatTrue = False

    def PROTOCOL_START():
        enterName = input("Please enter a name: ")

        openSaveFile = open("Files/saveDat.txt", "r")
        Lines = openSaveFile.readlines()
        print(Lines)
        openSaveFile.close()

        usernameEntered = enterName + "\n"

        Lines[0] = usernameEntered

        openSaveFile = open("Files/saveDat.txt", "w")
        openSaveFile.writelines(Lines)
        openSaveFile.close()

        print("\nSave file created!")

        print("Welcome to this Python Pokemon Prototype!")
        time.sleep(textDelayTime)
        print("Here you will be able to catch Pokemon as well as battle with others!")
        time.sleep(textDelayTime)
        print("If at any time you are confused, feel free to type in the help command: ", helpCommand)
        
        startFile = open("Files/startMem.txt", "w")
        startFile.truncate(0)
        startFile.write("yes")
    
    if startConfirm == "yes" and saveDatTrue:
        print("Loading previous save file!")

        openSavDatName = open("Files/saveDat.txt", "r")
        savDat = openSavDatName.readlines()
        name = savDat[0]
        name = name.replace("Trainer Name: ", "")
        print("Hello Trainer", name)
        openSavDatName.close()

    if startConfirm == "no":
        PROTOCOL_START()

start()

# Goes at the end of the code
print("")