# -*- coding: utf-8 -*-

from string import printable

#### get words from datafile
def readWords(filename='words.dat'):
    with open(filename, 'r') as infile:
        S = infile.read().lower().split() 
    return(S)


#### return the percentage of remaining words that have that letter

def remainPerc(S, letter):
    count = 0
    size = len(S)
    for i in S:
        if letter in i:
            count = count + 1
    perc = (count / size) * 100
    return round(perc, 2)


#### dictionary with the stats percentage stats, sorted
def statsDict(S, avail, confirmed):
    statistics = { k : remainPerc(S, k) for k in avail}
    for i in confirmed:
        del statistics[i]
    return sorted(statistics.items(), key = lambda x:x[1], reverse=True)
    


#### remove words with letter that have been diconfirmed

def removeit(S, noavail):
    for i in noavail:
        for j in S:
            if i in j:
                S.remove(j)
    return S

#### remove words that don't have letters matching the confirmed letters

def removeC(S, letter, position):
    l = []
    for i in S:
        if i[int(position)-1] == letter:
            l.append(i)
    return l


#### make sure confirmed letters are not overwritten

def alreadyTaken(word, num):
    if word[int(num)].isalpha == True:
        return False

#### hangman helper function
def hangmanHelper(S):
    
    ###3 initalize main variable
    avail = list(printable[10:36])
    word = ["_"]*5
    noavail = []
    confirmed = []
    
    print('Welcome to Hangman Helper!')
    
    print('Press ? for instructions')
    print("\n")
    
    while len(S)>1:
        print("Available letters: ", "".join(avail))
        print("Word: ", "".join(word))
        action = input("What will you do? ")
        print("\n")
        
        
        #### Main program logic, uses the input
        if action == "?":
            
            print('Press + to confirm a letter')
            print("Press - to disconfirmed a letter")
            print('Press S for statistics on possible letters')
            print("Press P to print out all the possible guesses")
            print("Press R to reset Hangman Helper")
            print("\n")
            continue
        
        
        elif action == ".":
            
            return
        
        
        elif action == "-":
            #### Takes in input letter and makes sure it is valid
            
            minusletter = input("What letter do you want to remove? ")
            
            while minusletter.isalpha() == False:
                minusletter = input("What letter do you want to remove? ")
                
            avail.remove(minusletter.lower())
            noavail.append(minusletter)
            S = removeit(S, noavail)
            
            print("\n")
            continue
        
        
        elif action == "+":
            #### Takes the input letter and makes sure it is valid
            
            addletter = input("What letter do you want to add? ")
            
            while (addletter.lower() in avail) == False: 
                addletter = input("What letter do you want to add? ")
                
            while addletter.isalpha() == False:
                addletter = input("What letter do you want to add? ")
                
            #### Takes in the input position andmakes sure it is valid
            position = input("Where do you want to put this letter? ")
            
            while word[int(position)-1].isalpha() == True:
                position = input("Where do you want to put this letter? ")
                
            while position.isdigit() == False:
                position = input("Where do you want to put this letter? ")
                
            while int(position) > 5 or int(position) < 1:
                position = input("Where do you want to put this letter? ")
                
            word[int(position)-1] = addletter.lower()
            confirmed.append(addletter.lower())
            S = removeC(S, addletter, position)
            
            print("\n")
            continue
        
        
        elif action.lower() == "s":
            
            print("Number of words remaining: ", len(S))
            print(statsDict(S, avail, confirmed))
            print("\n")
            continue
        
        
        elif action.lower() == "p":
            
            print(S)
            print("\n")
            continue
        
        
        elif action.lower() == "r":
            return True
        
        
        else:
            
            print("Please enter a valid input")
            print("Enter ? to learn about valid inputs\n")
        
       
    ##### activates when there is only one or zero possible words
    if len(S) == 1:
        
        print("The word must be: ", "".join(S))
        
    elif len(S) < 1:
        
        print("oops, something went wrong")
        print("The word might not be in our wordlist\n")
    
    return True
                
            
            
            

####main function

if __name__ == '__main__':
    # Read in the list of 5 letter words
    # Keep on repeating until program is quit
    while hangmanHelper(S=readWords('words.dat')):
        print("Let's try again!\n")