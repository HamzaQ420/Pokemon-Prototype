import time, random, sys, os
from os import listdir, read, system, terminal_size
from os.path import isfile, join

# Goes at the beginning of the code
print("")

textDelayTime = .10
helpCommand = "/help"

def start():
    print("Hello!")
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

        print("Pick a starter pokemon! Enter the corresponding number for which starter you would like.")

        starterList = [
            "Bulbasaur",
            "Charmander",
            "Squirtle", 
            "Chikorita",
            "Cyndaquill",
            "Totodile",
            "Treecko",
            "Torchic",
            "Mudkip",
            "Turtwig",
            "Chimchar",
            "Piplup",
            "Snivy",
            "Tepig",
            "Oshawott",
            "Rowlett",
            "Litten",
            "Popplio",
            "Grookey",
            "Scorbunny",
            "Sobble"
        ]

        starterIndex = 0
        starterFinalIndex = len(starterList)

        while starterIndex < starterFinalIndex:
            print(str(starterIndex + 1) + ". " + starterList[starterIndex])
            starterIndex = starterIndex + 1

        isPickingStarter = True
        while isPickingStarter:
            pickAStarter= input("Input the number for your starter: ")
            try:
                int(pickAStarter)
                intConvertable = True
            except ValueError:
                intConvertable = False

            if intConvertable:
                pickAStarterINT = int(pickAStarter)
                isPickingStarter = False

        starterFileOpen = open("Files/Pokemon Files/" + starterList[int(pickAStarter) - 1] + ".txt", "w")

        print("You picked " + starterList[int(pickAStarter) - 1] + " as your starter!")
        starterFileOpen.write("Name: " + starterList[int(pickAStarter) - 1] + "\nLevel: 1" + "\nHP: 10")

        print("\nSave file created!")

        print("Welcome to this Python Pokemon Prototype!")
        time.sleep(textDelayTime)
        print("Here you will be able to catch Pokemon as well as battle with others!")
        time.sleep(textDelayTime)
        print("If at any time you are confused, feel free to type in the help command:", helpCommand)
        
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

def gameplayCommands():
    print("Whenever you need assistance with anything or with comands, type in:", helpCommand)

    def HLPCommand():
        print("Help Window:\n\n--/Spawn, spawns a random pokemon to attempt to catch.")
        print("-/Inventory, opens your pokeball and coin inventory")

    def inventoryCommand():
        inventoryOpen = open("Files/inventory.txt", "r")
        readInventory = inventoryOpen.readlines()
        inventoryOpen.close()
        inventoryIndex = len(readInventory) - 1
        while inventoryIndex != -1:
            word = readInventory[inventoryIndex]

            word = word.replace("\n", "")
            word = word.replace("coins: ", "Coins: ")
            word = word.replace("pokeB: ", "Pokeballs: ")
            word = word.replace("great: ", "Great Balls: ")
            word = word.replace("ultra: ", "Ultra Balls: ")
            word = word.replace("premB: ", "Premier Balls: ")
            word = word.replace("mastr: ", "Master Balls: ")

            print(word)
            inventoryIndex = inventoryIndex - 1

    def pokedexCommmand():
        print("Pokedex")

    def spawnCommand():
        print("Spawn Command Triggered")
        pokeDataBaseRead = open("Files/pokemonDataBase.txt", "r")
        pokeDBR = pokeDataBaseRead.readlines()

        newDataBase = []
        for string in pokeDBR:
            newDat = string.replace("\n", " ")
            newDataBase.append(newDat)

        pokeSpawnerActive = True
        while pokeSpawnerActive:
            pokeGen = random.randint(130, 135)
            pokeSpawned = newDataBase[pokeGen]
            pokeSpawned = pokeSpawned[5:]

            if "[1]" in pokeSpawned:
                pokeRoll = random.randint(1, 3)
                if pokeRoll == 1:
                    pokeSpawnerActive = False
            elif "[2]" in pokeSpawned:
                pokeRoll = random.randint(1, 10)
                if pokeRoll == 1:
                    pokeSpawnerActive = False
            elif "[3]" in pokeSpawned:
                pokeRoll = random.randint(1, 30)
                if pokeRoll == 1:
                    pokeSpawnerActive = False
            elif "(Mythical)" in pokeSpawned or "(Legendary)" in pokeSpawned:
                pokeRoll = random.randint(1, 75)
                if pokeRoll == 1:
                    pokeSpawnerActive = False

        print("\n", pokeSpawned)

        if "[" in pokeSpawned:
            print("POKE [ FOUND")

        saveDatOpen = open("Files/saveDat.txt", "r")
        saveDatOpenRead = saveDatOpen.readlines()
        print(saveDatOpenRead)
        saveDatOpen.close()

        print(len(saveDatOpenRead))
        encounter = saveDatOpenRead[2]
        print(encounter)

        encounter = encounter.replace("\n", "")
        splitEncounter = encounter.split(": ", 1)
        print(splitEncounter[0])
        print(splitEncounter[1])
        encounterCounter = int(splitEncounter[1]) + 1

        encounterSTR = splitEncounter[0] + ": " + str(encounterCounter) + "\n"
        print(encounterSTR)
        saveDatOpenRead[2] = encounterSTR

        print(saveDatOpenRead)

        saveDatRewrite = open("Files/saveDat.txt", "w")
        print(saveDatOpenRead)
        saveDatRewrite.writelines(saveDatOpenRead)
        saveDatRewrite.close()

        pokeSpawnedRename = pokeSpawned

        pokeSpawnedRename = pokeSpawnedRename.replace("[1]", "")
        pokeSpawnedRename = pokeSpawnedRename.replace("[2]", "")
        pokeSpawnedRename = pokeSpawnedRename.replace("[3]", "")

        pokeSpawnedRename = pokeSpawnedRename.replace("(Starter)", "")
        pokeSpawnedRename = pokeSpawnedRename.replace("(Legendary)", "")
        pokeSpawnedRename = pokeSpawnedRename.replace("(Mythical)", "")

        pokeSpawnedRename = pokeSpawnedRename.replace(" ", "")

        if "*" in pokeSpawnedRename:
            strIndex = pokeSpawnedRename.index("*")
            strLength = len(pokeSpawnedRename)

            charRemoveNum = strIndex - strLength

            pokeSpawnedRename = pokeSpawnedRename[:charRemoveNum]
        
        print("It's a wild " + pokeSpawnedRename + "!")

        print("\nTo catch it use a pokeball!")
        inventoryOpen = open("Files/inventory.txt", "r")
        readInventory = inventoryOpen.readlines()
        inventoryOpen.close()

        indexLength = len(readInventory)

        for x in readInventory:
            indexLength = indexLength - 1
            word = readInventory[indexLength]
            word = word.replace("\n", "")

            if word[0] == "c":
                coinAMT = int(word[7:])
                word = word.replace("coins: ", "Coins: ")
                print(word)
            elif word[0] == "p" and word[1] == "o":
                pokeballAMT = int(word[7:])
                word = word.replace("pokeB: ", "Pokeballs: ")
                print(word)
            elif word[0] == "g":
                greatballAMT = int(word[7:])
                word = word.replace("great: ", "Great Balls: ")
                print(word)
            elif word[0] == "u":
                ultraballAMT = int(word[7:])
                word = word.replace("ultra: ", "Ultra Balls: ")
                print(word)
            elif word[0] == "p" and word[1] == "r":
                premierballAMT = int(word[7:])
                word = word.replace("premB: ", "Premier Balls: ")
                print(word)
            elif word[0] == "m":
                masterballAMT = int(word[7:])
                word = word.replace("mastr: ", "Master Balls: ")
                print(word)
        
        if masterballAMT > 0:
            hasBalls = True
        elif premierballAMT > 0:
            hasBalls = True
        elif ultraballAMT > 0:
            hasBalls = True
        elif greatballAMT > 0:
            hasBalls = True
        elif pokeballAMT > 0:
            hasBalls = True
        else:
            hasBalls = False
        
        z = 0

        pokemonFileList = os.listdir("Files/Pokemon Files/")

        print("Use /pokeball to choose a pokeball to catch the pokemon in!")
        isCatching = True
        pokeFileDIRTemplate = "Files/Pokemon Files/" + pokeSpawnedRename
        pokeFileDat = "Name: " + pokeSpawnedRename + "\nLevel: 1\nHP: 10"

        while isCatching == True:

            itemIndex = 0
            newPokeFileList = []
            pokemonFileNames = []
            newPokeFileList.clear()
            pokemonFileNames.clear()
            while itemIndex < len(pokemonFileList):
                pokeFileName = pokemonFileList[itemIndex]
                pokeFileName = pokeFileName.replace(".txt", "")
                itemIndex = itemIndex + 1
                newPokeFileList.append(pokeFileName)
                pokeFileName = pokeFileName.replace(".txt", "")

                pokeFileName = pokeFileName.replace("2", "")
                pokeFileName = pokeFileName.replace("3", "")
                pokeFileName = pokeFileName.replace("4", "")
                pokeFileName = pokeFileName.replace("5", "")
                pokeFileName = pokeFileName.replace("6", "")
                pokeFileName = pokeFileName.replace("7", "")
                pokeFileName = pokeFileName.replace("8", "")
                pokeFileName = pokeFileName.replace("9", "")
                
                pokemonFileNames.append(pokeFileName)

            pokeRunChance = random.randint(1, 10)
            
            z = z + 1
            print("\nTurn: " + str(z) + "\n")
            if pokeRunChance == 1 and z > 2:
                isCatching = False
                print(pokeSpawnedRename + " ran away!")
            
            battleCatchINPT = input("Command: ")
            
            print("")

            if battleCatchINPT == "/pokeball" and hasBalls == True:
                
                print("1. Pokeballs: " + str(pokeballAMT) + "\n2. Great Balls: " + str(greatballAMT))
                print("3. Ultra Balls: " + str(ultraballAMT) + "\n4. Premier Balls: " + str(premierballAMT))
                print("5. Master Balls: " + str(masterballAMT))

                ispickingBall = True
                pokeBallMaxChance = 15
                greatBallMaxChance = 10
                ultraBallMaxChance = 6
                masterBallMaxChance = 1

                while ispickingBall:
                    ballConfirm = input("Input the number of ball you would like to use: ")
                    if int(ballConfirm) == 1 and pokeballAMT > 0: 
                        catchChance = pokeBallMaxChance
                        pokeballAMT = pokeballAMT - 1
                        ispickingBall = False
                    elif int(ballConfirm) == 2 and greatballAMT > 0:
                        catchChance = greatBallMaxChance
                        greatballAMT = greatballAMT - 1
                        ispickingBall = False
                    elif int(ballConfirm) == 3 and ultraballAMT > 0:
                        catchChance = ultraBallMaxChance
                        ultraballAMT = ultraballAMT - 1
                        ispickingBall = False
                    elif int(ballConfirm) == 4 and premierballAMT > 0:
                        catchChance = pokeBallMaxChance
                        premierballAMT = premierballAMT - 1
                        ispickingBall = False
                    elif int(ballConfirm) == 5 and masterballAMT > 0:
                        catchChance = masterBallMaxChance
                        masterballAMT = masterballAMT - 1
                        ispickingBall = False
                    else:
                        print("You don't have enough of that!")
                
                inventoryOpenWrite = open("Files/inventory.txt", "w")
                inventoryOpenWrite.truncate(0)
                inventoryOpenWrite.write("mastr: " + str(masterballAMT) + "\npremB: " + str(premierballAMT))
                inventoryOpenWrite.write("\nultra: " + str(ultraballAMT) + "\ngreat: " + str(greatballAMT))
                inventoryOpenWrite.write("\npokeB: " + str(pokeballAMT) + "\ncoins: " + str(coinAMT))
                inventoryOpenWrite.close()

                print(str(catchChance))
                ballBreakoutRoll1 = random.randint(1, catchChance)
                if ballBreakoutRoll1 == 1:
                    time.sleep(textDelayTime)
                    print("1!")
                    ballBreakoutRoll2 = random.randint(1, catchChance)
                    if ballBreakoutRoll2 == 1:
                        time.sleep(textDelayTime)
                        print("2!")
                        ballBreakoutRoll3 = random.randint(1, catchChance)
                        if ballBreakoutRoll3 == 1:
                            print("You caught " + pokeSpawnedRename + "!")

                            saveDatRewrite = open("Files/saveDat.txt", "w")
                            caught = saveDatOpenRead[3]
                            
                            caughtNum = caught.replace("\n", "")
                            splitCaught = caughtNum.split(": ", 1)
                            print(splitCaught[0])
                            print(splitCaught[1])
                            caughtCounter = int(splitCaught[1]) + 1

                            caughtSTR = splitCaught[0] + ": " + str(caughtCounter) + "\n"
                            saveDatOpenRead[3] = caughtSTR
                            saveDatRewrite.writelines(saveDatOpenRead)

                            saveDatRewrite.close()

                            if pokeSpawnedRename in pokemonFileNames:
                                countRepeats = pokemonFileNames.count(pokeSpawnedRename)
                                newCaughtPokeFile = open(pokeFileDIRTemplate + str(countRepeats + 1) + ".txt", "w")
                                newCaughtPokeFile.write(pokeFileDat)
                                newCaughtPokeFile.close()
                                isCatching = False
                            else:
                                newCaughtPokeFile = open(pokeFileDIRTemplate + ".txt", "w")
                                newCaughtPokeFile.write(pokeFileDat)
                                newCaughtPokeFile.close()
                                isCatching = False
                    else:
                        print(pokeSpawnedRename + " broke out!")
                else:
                    print(pokeSpawnedRename + " broke out!")
            elif battleCatchINPT == "/run":
                runChance = random.randint(1, 5)
                if runChance == 1:
                    print("You got away!\n")
                    isCatching = False
                else:
                    print("You couldn't get away!")
            elif battleCatchINPT == "/pokeball" and hasBalls == False:
                print("You don't have any pokeballs!")
                print(pokeSpawnedRename + " ran away!\nBuy more pokeballs at the shop! (/shop)")
                isCatching = False

    def quitCommand():
        sys.exit()

    isPlaying = True

    while isPlaying:
        commandInput = input()
        if commandInput == helpCommand:
            HLPCommand()
        elif commandInput == "/spawn":
            spawnCommand()
        elif commandInput == "/quit":
            quitCommand()
        elif commandInput == "/dex":
            pokedexCommmand()
        elif commandInput == "/inventory":
            inventoryCommand()

start()
gameplayCommands()

# Goes at the end of the code
print("")