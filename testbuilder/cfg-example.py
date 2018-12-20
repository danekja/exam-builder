from testbuilder import datatypes as types

############################################
#           Configuration variables
############################################
#path to the output file
outputFile = "pokus.txt"
#number of tests to generate
nbOfTests = 10
#number of lines per page, set for standard A4 by default
linesPerPage = 64
#number of characters per line, set for standard A4 by default
columnsPerLine = 80
# Localized "Question" string
questionTitle = ' Otázka '
# Number of digits for question index (2 is enough for 1 - 99 questions)
questionIndexDigits = 2
# Test header
header = 'Zápočtový test z PIA, ak. rok 2018/2019'
# "Name" string
name = 'Jméno:'
# "Personal number" string
personalNb = 'Os. číslo:'

# list of definitions of individual test parts
# in this example each test would have
# 7 questions: 4 easy, 2 medium, 1 hard
definitions = [
    types.TestDefinition("easy", 4),
    types.TestDefinition("medium", 2),
    types.TestDefinition("hard", 1),

]