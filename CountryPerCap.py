# The program will read a text file with countries and their per capita. After
# reading the file, the user will be prompt to enter a country and the program
# will provide the per capita.

def main():

    countryData = readData("perCapita.txt")
    printRecords(countryData)
    getCountry(countryData)

# Reads the text file 
def readData(filename):

    # Creates an empty dictionary
    countryData = {}

    infile = open(filename, "r")

    # Reads over each record
    for line in infile:

        fields = line.split()
        country = fields[0]
        perCapita = fields[1]
        countryData[country] = createList(fields)

    infile.close()

    return countryData

# Creates a list of countries and capita per country
def createList(fields):

    perCapita = []

    for i in range(1, len(fields)):
        capita = fields[i]
        perCapita.append(capita)
    return perCapita 

# User enters a country if listed and returns the per capita
def getCountry(countryData):

    location = input("Enter a country to find the per capita: ")

    cap = countryData[location]
    
    if location in countryData:
        print("The country's per capita is ", cap)
    else:
        print("Country not found")

# Prints list of countries and per capita for each country
def printRecords(countryData):
 
    for country in sorted(countryData):
        print("%-15s" % country, end ="")

        perCapita = countryData[country]
        for i in range(len(perCapita)):
            capita = perCapita[i]
            print("%20s" % capita, end = "")
            print("\n")

main()


