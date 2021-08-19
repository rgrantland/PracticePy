import tkinter as tk
from random import randint

# creating gui window and titling window appropriately
window = tk.Tk()
window.title("Dice Roller")

# creating string variables that will be used to get data from the user
numberOfDiceVar = tk.StringVar()
modifierVar = tk.StringVar()

# function to roll dice after selection and inputs
def rollingDice(numberOfSides):
    # initializing variables
    total = 0
    diceString=""
    counter=0
    # clearing error message before run
    errorMessage.config(text="")

    # if feild for number of dice or modifier is blank then autofill 1 and 0 respectively
    # otherwise, take user input and convert to int for calculations
    # if input not int then send error message to user
    try:
        if numberOfDiceVar.get() == "":
            numberOfDice = 1
        else:
            numberOfDice = numberOfDiceVar.get()
            numberOfDice = int(numberOfDice)
    except:
        errorMessage.config(text="Please enter a number")
        numberOfDice = 0
    try:
        if modifierVar.get() == "":
            modifier = 0
        else:
            modifier = modifierVar.get()
            modifier = int(modifier)
    except: 
        errorMessage.config(text="Please enter a number")
        numberOfDice = 0
        modifier = 0

    # roll as many dice as the user asked for
    for i in range(numberOfDice):
        dRoll = randint(1, numberOfSides)
        # keeping track of dice total
        total = total + dRoll
        # incrementing counter to help with output format later
        counter = counter + 1

        # used to keep window format from widening
        if numberOfDice <= 15:
            diceString = diceString + str(dRoll) + "  "
            resultDice.config(text=diceString)
        else:
            diceString = diceString + str(dRoll) + "  "
            if counter%15 == 0:
                diceString = diceString + "\n"
            resultDice.config(text=diceString)
        
    # add modifier to total and output total to user
    total = total + modifier
    resultTotal.config(text=total)

    # clear the original string variables so they can be reused 
    numberOfDiceVar.set("")
    modifierVar.set("")

# creating labels and entry feilds for user to interact with
howManyDice = tk.Label(
    text="Enter the number of dice you would like to roll:",
    height=2,
)

numberOfDiceEntry = tk.Entry(
    window, 
    width=10,
    textvariable = numberOfDiceVar
)

modifiers = tk.Label(
    text="Enter any modifiers to be added:",
    height=2,
)

modifierEntry = tk.Entry(
    window, 
    width=10,
    textvariable = modifierVar
)

whichDice = tk.Label(
    text="Which dice would you like to use?",
    height = 2,
    width = 60,
)

diceLabel = tk.Label(
    window,
    text="Resulting dice rolls:",
    height=2,
)

totalLabel = tk.Label(
    window, 
    text="Total of dice with modifier:",
    height=2,
)

# Black labels that will fill when diceRoller function is called
resultDice = tk.Label(window, text="")
resultTotal = tk.Label(window, text="")
errorMessage = tk.Label(window, text="", font='bold', fg='red')

# creating buttons for the user to interact with and will call diceRoller function appropriately
d4btn = tk.Button(
    window,
    text="d4",
    width=20,
    height=3,
    bg="gray",
    fg="white",
    command = lambda: rollingDice(4)
)

d6btn = tk.Button(
    window,
    text="d6",
    width=20,
    height=3,
    bg="gray",
    fg="white",
    command = lambda: rollingDice(6) 
)

d8btn = tk.Button(
    window,
    text="d8",
    width=20,
    height=3,
    bg="gray",
    fg="white",
    command = lambda: rollingDice(8)
)

d10btn = tk.Button(
    window,
    text="d10",
    width=20,
    height=3,
    bg="gray",
    fg="white",
    command = lambda: rollingDice(10)
)

d20btn = tk.Button(
    window,
    text="d20",
    width=20,
    height=3,
    bg="gray",
    fg="white",
    command = lambda: rollingDice(20)
)

d100btn = tk.Button(
    window,
    text="d100",
    width=20,
    height=3,
    bg="gray",
    fg="white",
    command = lambda: rollingDice(100)
)

# setting labels, entries, and buttons on the window in a grid based format 
errorMessage.grid(row=0, columnspan=3)
howManyDice.grid(row=1, columnspan=2)
modifiers.grid(row=2, columnspan=2)

numberOfDiceEntry.grid(row=1, column=2)
modifierEntry.grid(row=2, column=2) 

whichDice.grid(row=3, columnspan=3)

d4btn.grid(row=4, column=0)
d6btn.grid(row=4, column=1)
d8btn.grid(row=4, column=2)

d10btn.grid(row=5, column=0)
d20btn.grid(row=5, column=1)
d100btn.grid(row=5, column=2)

diceLabel.grid(row=6, column=0)
resultDice.grid(row=6, column=1, columnspan=2)

totalLabel.grid(row=7, column=0)
resultTotal.grid(row=7, column=1, columnspan=2)

# starting gui
window.mainloop()


# function to print options menu to console
def printDiceMenu():
    print('dice options: d4, d6, d8, d10, d20, d100')
    print('enter "bye" to go back to exit')
    print('----------------------------------------')

# function to roll dice and output to console
def rollingDice(numberOfSides):
    # initializing variables
    total = 0

    # taking input from user to get number of dice and modifier to be used in calculations
    numberOfDice = input('how many dice would you like to roll?: ')
    modifier = input('enter any modifiers to be added: ')

    # outputting error if number of dice or modifier cannot convert to integer
    try:
        numberOfDice = int(numberOfDice)
        modifier = int(modifier)
    except:
        print("\n!!! Input was not a number. Aborting this roll. Please try again. !!!\n")
        numberOfDice = 0
        modifier = 0

    # rolling all the dice the user asked for
    for i in range(numberOfDice):
        dRoll = randint(1, numberOfSides)
        # outputing each dice roll to console
        print('\t', dRoll)
        # adding total of all dice rolls
        total = total + dRoll
    
    # adding modifier to total
    total = total + modifier
    # printing modifier and total to console
    print("modifier: ", modifier)
    print("total: ", total, '\n')

# function to start diceRoller: console version
def diceRoller():
    # repeats loop until user inputs 'bye'
    while(True):
        printDiceMenu()
        # taking user input to choose they type of dice
        diceChoice = input('which dice would you like to roll?: ')
        # calling rollingDice acording to user choice
        if diceChoice == 'd4':
            rollingDice(4)
        elif diceChoice == 'd6':
            rollingDice(6)
        elif diceChoice == 'd8':
            rollingDice(8)
        elif diceChoice == 'd10':
            rollingDice(10)
        elif diceChoice == 'd20':
            rollingDice(20)
        elif diceChoice == 'd100':
            rollingDice(100)
        elif diceChoice == 'bye':
            print('\nThanks for rolling!\n')
            break
        # error handeling for invalid input
        else:
            print('\nInvalid input. Please enter one of the listed dice options or type "bye" to exit to the game menu.')

diceRoller()