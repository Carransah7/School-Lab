#Opens the file in read mode
file = open('lab3in.txt', 'r')
#Reads the lines in the file and saves it in myLines
myLines = file.readlines()
#Iterates through the lines in myLines
for line in myLines:
    #Removes the newline character at the end of the line
    line = line.rstrip('\n')
    #Checks if the line contains only alphabetic characters
    isAlpha = True
    #Checks each character in the line
    for character in line:
        #Checks if the character is not alphabetic
        if not character.isalpha() and not character.isspace():
            #If character is not alphabetic it sets isAlpha to False
            isAlpha = False
    
    #If the line is alphabetic it will be printed
    if isAlpha:
        print(line)
    #If it's not alphabetic it will print the message below
    else:
        print("This line has non-alphabetic characters.")

#Closes file
file.close()


#Opens lab3in.txt in read mode and lab3out.txt in write mode
with open('lab3in.txt', 'r') as infile, open('lab3out.txt', 'w') as outfile:
    #Assigns the 1 to lineNum
    lineNum = 1
    #Iterates through the lines in infile
    for line in infile:
        #Removes the newline character at the end of the line
        numChars = len(line.rstrip())  # change this line
        #Prints the line number and the number of characters in the line
        print('The no. of characters in line ' + str(lineNum) + ' is ' + str(numChars))
        #Writes the line in uppercase to outfile
        outfile.write(line.upper())
        #Increments lineNum by 1
        lineNum += 1
