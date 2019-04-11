# The roster of the Arkon Zips 2018-2019 Men's Basketball Team
# The program will separate the roster, append a player, sort the roster, remove a player, display the longest and shortest names on the roster

def main():
    
    roster = ["Ivey", "Jackson", "Utomi", "Cheese", "Toles", "Riak", "Banks", "McIntyre", "Roscoe", "Walter", "Williams", "Olojakpoke", "Sayles", "Fischer"]
    
    separateRos(roster)
    print("\n")
    appendRos(roster)
    print("\n")
    sortRos(roster)
    print("\n")
    removeRos(roster)
    print("\n")
    longestName(roster)
    print("\n")
    shortestName(roster)

# Separates the last names of the players with a "|"
def separateRos(roster):
    
    for i in range (len(roster)):
        if i > 0:
            print("|", end = " ")
        print(roster[i], end = " ")
    return

# Append a new player to the team
def appendRos(roster):

    roster.append("Zygote")
    print(roster)
    return

# Sort the roster in reverse alphabetical order
def sortRos(roster):

    roster.sort(reverse=True)
    print (roster)
    return

# Remove the player at position 3 of the list
def removeRos(roster):

    print ("The player remove from the roster is", roster.pop(3))
    return

# Display the longest names from the list
def longestName(roster):
    i = 0
    LONGEST_NAME = 10
    roster = ["Ivey", "Jackson", "Utomi", "Cheese", "Toles", "Riak", "Banks", "McIntyre", "Roscoe", "Walter", "Williams", "Olojakpoke", "Sayles", "Fischer"]
    while i != len(roster):
        player = roster[i]
        if len(player) < LONGEST_NAME:
            roster.pop(i)
        else:
            i = i + 1
    print(roster)
    return

# Display the shortest names from the list
def shortestName(roster):
    i = 0
    SHORTEST_NAME = 4
    roster = ["Ivey", "Jackson", "Utomi", "Cheese", "Toles", "Riak", "Banks", "McIntyre", "Roscoe", "Walter", "Williams", "Olojakpoke", "Sayles", "Fischer"]
    while i != len(roster):
        player = roster[i]
        if SHORTEST_NAME < len(player):
            roster.pop(i)
        else:
            i = i + 1
    print(roster)
    return

main()
