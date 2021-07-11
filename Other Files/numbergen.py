x = 0

numList = []

while x < 898:
    file = open("Files/pokemonDataBase.txt", "w")
    x = x + 1

    print(x)
    if x < 10:
        strx = "00" + str(x)
    elif x < 100 and x > 9:
        strx = "0" + str(x)
    else:
        strx = str(x)

    numList.append(strx + " - " + "\n")

file.writelines(numList)

file.close()