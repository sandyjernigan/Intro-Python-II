import sys
import textwrap

from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "outside",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", "foyer",
                    """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", "overlook",
                    """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", "narrow",
                    """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", "treasure",
                    """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
}

# Declare Players
player = [
    Player("Player 1", "outside")
]

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# Function for formatting output
def printCenter(string="", num=1, char="~", width=80):
    # num is the number of times to print
    # char is character printed around the string text
    # width is the number of characters wide 
    for x in range(0,num):
        print(string.center(width, char))

def printRoom(currentRoom):
    # Print Current Room
    pStr = currentRoom.name
    printCenter(pStr, 1, " ")
    printCenter("~ ~ ~ ~ ~", 1, " ")

    # Current Room Description
    print(textwrap.fill(currentRoom.description, 80))
    printCenter("")


# Function to select action
def movePlayer(action):
	switcher = { 
		"w": "n_to", 
		"a": "w_to", 
		"s": "s_to", 
		"d": "e_to", 
	} 

	# returns action or default to invalid
	return switcher.get(action, "invalid") 

# Function to get room key
def selectRoom(newRoom):
	#for eachRoom in room:
        #compare name to the key
    if newRoom == "Foyer":
        return "foyer"

# Print Player Name
printCenter("", 2)
printCenter(" Hello " + player[0].name + " ")
printCenter("", 2)

# Print Current Room
print("Current Location:")
printRoom(room[player[0].room])

# Get user input
def userChoice():
    return input("Please choose a direction (w,a,s,d, or q to quit): ")

choice = userChoice()

printCenter()

while choice != "q":

    # Get action selected
    action = movePlayer(choice)

    if action == "invalid":
        print("Invalid Selection.")
    else:
        # if action is available, select new room
        if hasattr(room[player[0].room], action):
            # Get new room
            newRoom = getattr(room[player[0].room], action)
            

            # Print new Room
            print("You have moved into:")
            printRoom(newRoom)

            # Get room key value
            newRoomName = newRoom.shortname
            
            # Set room for player
            if newRoom != None:
                player[0].room = newRoomName

        # action not available, return "Dead End"
        else:
            print("Dead End. Please make another selection.")

    # Ask for next direction
    choice = input("Please choose a direction (w,a,s,d, or q to quit): ")
    printCenter()

print("Final Stop - " + player[0].room)

