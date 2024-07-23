# CS-003 - LAB 8 - Chapter 7
# 7/22/2024
# Zoraida Rodriguez
# Timothy Sanders
#
# Problem Statement
# We need to create an application that can take in a file that contains a ranked list of boys and girls baby names
# and prints a message displaying the duplicate names that show up in both boys and girls names, along with the
# corresponding ranking in each list. To run, this application requires a file path and name specified in the
# BABY_NAME_FILE constant.

BABY_NAME_FILE = 'babynames.txt'
OUTPUT_FILE_NAME_ONE = 'rankedBoysNames.txt'
OUTPUT_FILE_NAME_TWO = 'rankedGirlsNames.txt'


def main():
    createTwoFiles(BABY_NAME_FILE, OUTPUT_FILE_NAME_ONE, OUTPUT_FILE_NAME_TWO)
    try:
        boysNamesList = convertFileToList(OUTPUT_FILE_NAME_ONE)
        girlsNamesList = convertFileToList(OUTPUT_FILE_NAME_TWO)
    except FileNotFoundError as fnfe:
        print("ERROR: Incorrect file path specified")
        raise fnfe
    duplicateNameList = findDuplicateNames(boysNamesList, girlsNamesList)
    displayDuplicateNames(duplicateNameList)


## The createTwoFiles() function will take in a single file that contains multiple rows of a rank and two names
## The function then splits the data from the input file into two separate files, outputFileNameOne and
## outputFileNameTwo
#  @param inputFileName: str
#       - A string that specifies the existing file that contains the data we will split into
#         outputFileNameOne and outputFileNameTwo
#  @param outputFileNameOne: str
#       - A string that gives the name of the first output file that will be generated
#  @param outputFileNameTwo: str
#       - A string that gives the name of the second output file that will be generated
def createTwoFiles(inputFileName: str, outputFileNameOne: str, outputFileNameTwo: str) -> None:
    try:
        inputFile = open(inputFileName, "r", encoding="utf-8")
    except FileNotFoundError:
        print("ERROR: Incorrect file path specified")
        validFile = False
        while not validFile:
            userFileName = input("Please enter the correct file path: ")
            try:
                inputFile = open(userFileName, "r", encoding="utf-8")
                validFile = True
            except FileNotFoundError:
                validFile = False
    outputFileListOne = []
    outputFileListTwo = []
    for line in inputFile:
        lineList = line.strip().split()
        outputFileListOne.append((lineList[0], lineList[1]))
        outputFileListTwo.append((lineList[0], lineList[2]))
    writeTupleListToFile(outputFileNameOne, outputFileListOne)
    writeTupleListToFile(outputFileNameTwo, outputFileListTwo)


## Creates a file with the given fileName from the specified tupleList
#  @param - fileName
#       - A string filename/path to create a new file at
#  @param - tupleList
#       - The input list of tuples to create a file from
#  @return - None
def writeTupleListToFile(fileName: str, tupleList: list[tuple[int, str]]) -> None:
    try:
        with open(fileName, 'w') as file:
            for integer, string in tupleList:
                file.write(f"{integer} {string}\n")
    except Exception as e:
        raise OSError(f"An error occurred while writing to the file: {e}")


## Reads a file and returns a list containing tuples of an integer rank and a string name
#  @param inputFileName: str
#       - The file from which data will be read and converted into a list
#  @return list[tuple[int, str]]
def convertFileToList(inputFileName: str) -> list[tuple[int, str]]:
    resultList = []
    with open(inputFileName, 'r', encoding="utf-8") as file:
        for line in file:
            lineList = line.strip().split()
            resultList.append((int(lineList[0]), lineList[1]))
    return resultList


## This function will take in two lists of names and returns a list of tuples that contain the common name,
#   what rank the name was in inputListOne and what rank the name was in inputListTwo
#  @param - inputListOne
#       - A ranked list of names for comparison
#  @param - inputListTwo
#       - A ranked list of names for comparison
#  @return - duplicateNameList
#       - A list of tuples with a name and the rank it was found in each input list
def findDuplicateNames(
        inputListOne: list[tuple[int, str]],
        inputListTwo: list[tuple[int, str]]
) -> list[tuple[str, int, int]]:
    duplicateNameList = []
    for (firstRank, firstName) in inputListOne:
        for (secondRank, secondName) in inputListTwo:
            if secondName.lower() == firstName.lower():
                duplicateNameList.append((firstName, firstRank, secondRank))
    return duplicateNameList


## This function will print a formatted message that displays the duplicate name that was found and the rank
#  that it was found in each list
#  Ex: "Alexis | found in the boys list with rank ... and in the girls list with rank..."
#  At the end of the function, a message will print that displays the total number of duplicate names
#  @param - duplicateNamesList: list[tuple[str, int, int]]
#       - A list of all duplicate names found, along with the rank in each of the boys/girls lists
#  @return - None
def displayDuplicateNames(duplicateNamesList:  list[tuple[str, int, int]]) -> None:
    maxNameLength = 0
    for x in duplicateNamesList:
        if len(x[0]) > maxNameLength:
            maxNameLength = len(x[0])
    for record in sorted(duplicateNamesList):
        print(f"{record[0]:>{maxNameLength+1}} | found in the boys list with rank {record[1]:<3} and in the girls list with rank {record[2]:<3}")
    print("The size of duplicated list is %d" % (len(duplicateNamesList)))


if __name__ == "__main__":
    main()

# Sample Program Output
"""
python lab-8-chapter-7.py

   Addison | found in the boys list with rank 542 and in the girls list with rank 160
      Alex | found in the boys list with rank 63  and in the girls list with rank 990
    Alexis | found in the boys list with rank 103 and in the girls list with rank 11 
       Ali | found in the boys list with rank 379 and in the girls list with rank 871
     Amari | found in the boys list with rank 407 and in the girls list with rank 434
     Angel | found in the boys list with rank 44  and in the girls list with rank 128
     Ariel | found in the boys list with rank 554 and in the girls list with rank 220
    Ashton | found in the boys list with rank 76  and in the girls list with rank 665
     Avery | found in the boys list with rank 226 and in the girls list with rank 77 
    Bailey | found in the boys list with rank 432 and in the girls list with rank 99 
   Cameron | found in the boys list with rank 50  and in the girls list with rank 252
...
     Rowan | found in the boys list with rank 476 and in the girls list with rank 706
      Ryan | found in the boys list with rank 12  and in the girls list with rank 436
     Rylee | found in the boys list with rank 777 and in the girls list with rank 135
      Sage | found in the boys list with rank 666 and in the girls list with rank 361
   Shannon | found in the boys list with rank 873 and in the girls list with rank 256
      Shea | found in the boys list with rank 890 and in the girls list with rank 790
    Sidney | found in the boys list with rank 722 and in the girls list with rank 374
    Skylar | found in the boys list with rank 471 and in the girls list with rank 155
    Skyler | found in the boys list with rank 236 and in the girls list with rank 310
    Taylor | found in the boys list with rank 216 and in the girls list with rank 22 
    Teagan | found in the boys list with rank 907 and in the girls list with rank 520
     Tyler | found in the boys list with rank 16  and in the girls list with rank 575
The size of duplicated list is 71
"""

"""
python lab-8-chapter-7.py

ERROR: Incorrect file path specified
Please enter the correct file path: babynames.txt
   Addison | found in the boys list with rank 542 and in the girls list with rank 160
      Alex | found in the boys list with rank 63  and in the girls list with rank 990
    Alexis | found in the boys list with rank 103 and in the girls list with rank 11 
       Ali | found in the boys list with rank 379 and in the girls list with rank 871
     Amari | found in the boys list with rank 407 and in the girls list with rank 434
     Angel | found in the boys list with rank 44  and in the girls list with rank 128
     Ariel | found in the boys list with rank 554 and in the girls list with rank 220
    Ashton | found in the boys list with rank 76  and in the girls list with rank 665
     Avery | found in the boys list with rank 226 and in the girls list with rank 77 
    Bailey | found in the boys list with rank 432 and in the girls list with rank 99 
   Cameron | found in the boys list with rank 50  and in the girls list with rank 252
...
     Rowan | found in the boys list with rank 476 and in the girls list with rank 706
      Ryan | found in the boys list with rank 12  and in the girls list with rank 436
     Rylee | found in the boys list with rank 777 and in the girls list with rank 135
      Sage | found in the boys list with rank 666 and in the girls list with rank 361
   Shannon | found in the boys list with rank 873 and in the girls list with rank 256
      Shea | found in the boys list with rank 890 and in the girls list with rank 790
    Sidney | found in the boys list with rank 722 and in the girls list with rank 374
    Skylar | found in the boys list with rank 471 and in the girls list with rank 155
    Skyler | found in the boys list with rank 236 and in the girls list with rank 310
    Taylor | found in the boys list with rank 216 and in the girls list with rank 22 
    Teagan | found in the boys list with rank 907 and in the girls list with rank 520
     Tyler | found in the boys list with rank 16  and in the girls list with rank 575
The size of duplicated list is 71
"""