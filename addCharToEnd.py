import time

def addCharToEnd(charToAdd, fileIn, fileOut):
    add = charToAdd
    with open(fileOut, 'w+') as out_file:
        with open(fileIn, 'r') as in_file:
            for line in in_file:
                out_file.write(line.rstrip('\n') + add)


while True:
    choice = input("Type INPUT or QUIT\n").upper()
    if(choice == 'INPUT'):
        inputfile = input("Enter input file: \n")
        outputfile = (input("Enter output file name: \n"))
        if '.' not in outputfile:
            outputfile = outputfile + '.' + inputfile.rsplit('.', 1)[1]
        addCharToEnd(',', inputfile, outputfile)
        print('Done')
        time.sleep(3)
        break
    elif(choice == 'QUIT'):
        break
    else:
        print("Not a command")
        continue
        
