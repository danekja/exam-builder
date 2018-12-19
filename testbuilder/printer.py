# coding=utf-8

############################################
#            Constants
# - no need to modify if you do not touch the
# - implementation itself
############################################

#             Formatting
linesPerPage = 64
columnsPerLine = 80
questionTitle = ' Otázka '
questionIndexDigits = 2

HEADING_LINES = 7
CONTENT_COLUMNS = columnsPerLine - 2
HALF_CONTENT_COLUMNS = int(CONTENT_COLUMNS / 2)
LINES_PER_QUESTION = 8
QUESTIONS_PER_FIRST_PAGE = 7 #this needs to be computed!
QUESTIONS_PER_LAST_PAGE = 3  #this needs to be computed!
EMPTY_LINES_FIRST_PAGE = linesPerPage - HEADING_LINES - QUESTIONS_PER_FIRST_PAGE * LINES_PER_QUESTION
QUESTION_TITLE_LEN = len(questionTitle)
QUESTION_HEADER_CONTENT_LEN = CONTENT_COLUMNS - questionIndexDigits - QUESTION_TITLE_LEN



#########################################
#           Public API
#########################################
printedLines = 0

def printTest(outputFile, data = []):
    questionCount = len(data)

    with open(outputFile, 'a', encoding="utf8") as file:
        _printHeader(file)
        i = 0

        for q in data:

            if not _remainingLinesCheck(file, q):
                if i < questionCount:
                    _printNextPageNotice(file)
                _printEndOfPage(file)


            i += 1
            _printQuestion(file, q.questionTexts, q.freeSpace, i)

        if printedLines > 0:
            _printEndOfPage(file)


########################################
#           Implementation
########################################



def _printHeader(file):
    _print(file, '|{:#^{width}}|\n'.format('', width=CONTENT_COLUMNS))
    _print(file, '|{: ^{width}}|\n'.format('', width=CONTENT_COLUMNS))
    _print(file, '|{: ^{width}}|\n'.format('Zápočtový test z PIA, ak. rok 2018/2019', width=CONTENT_COLUMNS))
    _print(file, '|{: ^{width}}|\n'.format('', width=CONTENT_COLUMNS))
    _print(file, '|{: <{width}}'.format('Jméno:', width=HALF_CONTENT_COLUMNS), newline = False)
    _print(file, '{: <{width}}|\n'.format('Os. číslo:', width=HALF_CONTENT_COLUMNS))
    _print(file, '|{:#^{width}}|\n'.format('', width=CONTENT_COLUMNS))
    _print(file, '|{: ^{width}}|\n'.format('', width=CONTENT_COLUMNS))

def _printQuestion(file, questionTexts = ['No question provided!'], freeSpace = 4, index = 0):
    #print question header
    _print(file, '|{:#^{width}}|\n'.format('', width=CONTENT_COLUMNS))
    _print(file, '|{: ^{width}}|\n'.format('', width=CONTENT_COLUMNS))
    _print(file, '|{: ^{width}}|\n'.format('', width=CONTENT_COLUMNS))

    # print question text
    _print(file, '|{}{: <{indexWidth}}{: ^{width}}|\n'.format(questionTitle, index, questionTexts[0], indexWidth = questionIndexDigits, width = QUESTION_HEADER_CONTENT_LEN))
    for i in range(1, len(questionTexts)):
        _print(file, '|{: ^{width}}|\n'.format(questionTexts[i], width=CONTENT_COLUMNS))

    # print space for answers
    for i in range(0, freeSpace - 1):
        _print(file, '|{: ^{width}}|\n'.format('', width=CONTENT_COLUMNS))

    #print question end
    _print(file, '|{:_^{width}}|\n'.format('', width=CONTENT_COLUMNS))

def _remainingLinesCheck(file, question):
    # how many lines this question takes
    toPrintLines = 3 + len(question.questionTexts) + question.freeSpace

    if printedLines + toPrintLines >= linesPerPage:
        return False

    return True

def _printNextPageNotice(file):
    _print(file, '{: >{width}}\n'.format('Nezapomeňte otočit na druhou stranu!', width=columnsPerLine))

def _printEndOfPage(file):
    global printedLines
    for i in range(0, linesPerPage - printedLines):
        _print(file, '{: >{width}}\n'.format('', width=columnsPerLine))

    assert printedLines == linesPerPage
    printedLines = 0


def _print(file, text, newline = True):
    global printedLines

    file.write(text)

    if newline:
        printedLines = printedLines + 1
