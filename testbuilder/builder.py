import random
from testbuilder import data as d

############################################
#           Configuration variables
############################################
outputFile = "pokus.txt"
nbOfTests = 45
questionsPerTest = 10
questionTitle = ' Otázka '
questionIndexDigits = 2

#             Formatting
linesPerPage = 64
columnsPerLine = 80

############################################
#            Constants
# - no need to modify if you do not touch the
# - implementation itself
############################################

HEADING_LINES = 7
CONTENT_COLUMNS = columnsPerLine - 2
HALF_CONTENT_COLUMNS = int(CONTENT_COLUMNS / 2)
LINES_PER_QUESTION = 8
QUESTIONS_PER_FIRST_PAGE = 7 #this needs to be computed!
QUESTIONS_PER_LAST_PAGE = 3  #this needs to be computed!
EMPTY_LINES_FIRST_PAGE = linesPerPage - HEADING_LINES - QUESTIONS_PER_FIRST_PAGE * LINES_PER_QUESTION
QUESTION_TITLE_LEN = len(questionTitle)
QUESTION_HEADER_CONTENT_LEN = CONTENT_COLUMNS - questionIndexDigits - QUESTION_TITLE_LEN

############################################
#            Code
############################################

def createTests(number = 0, dataname = ""):
    for i in range(0, number):
        test = _generateTest(dataname)
        _printTest(test)

def _generateTest(dataname = ""):
    data = d.data[dataname]
    seq = _generateTestSequence(questionsPerTest, len(data))

    testData = []
    for i in seq:
        testData.append(data[i])

    return testData

def _generateTestSequence(amount, srcSize):
    toRet = []

    if(amount > srcSize):
        print("You can only add as many questions to a test as many you have in source test set!")
        print("Exiting...")
        exit(-1)

    for i in range(0,amount):
        candidate = _getRandomQuestionIndex(srcSize)
        while candidate in toRet:
            candidate = _getRandomQuestionIndex(srcSize)

        toRet.append(candidate)

    return toRet

def _getRandomQuestionIndex(srcSize):
    return random.randrange(0, srcSize)

def _printTest(data = []):
    with open(outputFile, 'a', encoding="utf8") as file:
        _printHeader(file)
        i = 0
        for q in data:
            i += 1
            _printQuestion(file, q.line1, q.line2, i)
        _printEndOfPage(file, len(data))

def _printHeader(file):
    file.write('|{:#^{width}}|\n'.format('', width=CONTENT_COLUMNS))
    file.write('|{: ^{width}}|\n'.format('', width=CONTENT_COLUMNS))
    file.write('|{: ^{width}}|\n'.format('Zápočtový test z PIA, ak. rok 2018/2019', width=CONTENT_COLUMNS))
    file.write('|{: ^{width}}|\n'.format('', width=CONTENT_COLUMNS))
    file.write('|{: <{width}}'.format('Jméno:', width=HALF_CONTENT_COLUMNS))
    file.write('{: <{width}}|\n'.format('Os. číslo:', width=HALF_CONTENT_COLUMNS))
    file.write('|{:#^{width}}|\n'.format('', width=CONTENT_COLUMNS))
    file.write('|{: ^{width}}|\n'.format('', width=CONTENT_COLUMNS))
    pass

def _printQuestion(file, question1 = None, question2 = '', index = 0):
    file.write('|{:#^{width}}|\n'.format('', width=CONTENT_COLUMNS))
    file.write('|{: ^{width}}|\n'.format('', width=CONTENT_COLUMNS))
    file.write('|{}{: <{indexWidth}}{: ^{width}}|\n'.format(questionTitle, index, question1, indexWidth = questionIndexDigits, width = QUESTION_HEADER_CONTENT_LEN))
    file.write('|{: ^{width}}|\n'.format(question2, width=CONTENT_COLUMNS))
    file.write('|{: ^{width}}|\n'.format('', width=CONTENT_COLUMNS))
    file.write('|{: ^{width}}|\n'.format('', width=CONTENT_COLUMNS))
    file.write('|{: ^{width}}|\n'.format('', width=CONTENT_COLUMNS))
    file.write('|{:_^{width}}|\n'.format('', width=CONTENT_COLUMNS))

    if index == 7:
        if EMPTY_LINES_FIRST_PAGE > 0:
            file.write('{: >{width}}\n'.format('Nezapomeňte otočit na druhou stranu!', width=columnsPerLine))
        for i in range(0, EMPTY_LINES_FIRST_PAGE - 1):
            file.write('{: >{width}}\n'.format('', width=columnsPerLine))

def _printEndOfPage(file, questions):
    #two pages rows minus header rows minus rows per test question
    toPrint = linesPerPage - LINES_PER_QUESTION * QUESTIONS_PER_LAST_PAGE

    for i in range(0, toPrint):
        file.write('{: ^80}\n'.format(''))


if __name__ == '__main__':
    createTests(nbOfTests, "example")