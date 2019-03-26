# coding=utf-8

from testbuilder import cfg

############################################
#  Printer module - all formatting logic
############################################
#            Constants
# - no need to modify if you do not touch the
# - implementation itself
############################################

#             Formatting
# wrapper from cfg script, because im too lazy to find and prefix
linesPerPage = cfg.linesPerPage
columnsPerLine = cfg.columnsPerLine
questionTitle = cfg.questionTitle
questionIndexDigits = cfg.questionIndexDigits

CONTENT_COLUMNS = columnsPerLine - 2
HALF_CONTENT_COLUMNS = int(CONTENT_COLUMNS / 2)
QUESTION_TITLE_LEN = len(questionTitle)
QUESTION_HEADER_CONTENT_LEN = CONTENT_COLUMNS - questionIndexDigits - QUESTION_TITLE_LEN



#########################################
#           Public API
#########################################
printedLines = 0

"""
Prints single test into the given outputFile (appends to the end of file).

Expects list of TestQuestion instances.
"""
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
            _printQuestion(file, q, i)

        if printedLines > 0:
            _printEndOfPage(file)


########################################
#           Implementation
########################################


"""
Prints header of the test.
"""
def _printHeader(file):
    _print(file, '|{:#^{width}}|\n'.format('', width=CONTENT_COLUMNS))
    _print(file, '|{: ^{width}}|\n'.format('', width=CONTENT_COLUMNS))
    _print(file, '|{: ^{width}}|\n'.format(cfg.header, width=CONTENT_COLUMNS))
    _print(file, '|{: ^{width}}|\n'.format('', width=CONTENT_COLUMNS))
    _print(file, '|{: <{width}}'.format(cfg.name, width=HALF_CONTENT_COLUMNS), newline = False)
    _print(file, '{: <{width}}|\n'.format(cfg.personalNb, width=HALF_CONTENT_COLUMNS))
    _print(file, '|{:#^{width}}|\n'.format('', width=CONTENT_COLUMNS))
    _print(file, '|{: ^{width}}|\n'.format('', width=CONTENT_COLUMNS))

"""
Prints single question block.

Optional parameter index is used to mark question with particular number.

e.g.: Question 1: What is your name?
"""
def _printQuestion(file, q, index = 0):

    #print question header
    _print(file, '|{:#^{width}}|\n'.format('', width=CONTENT_COLUMNS))
    _print(file, '|{: ^{width}}|\n'.format('', width=CONTENT_COLUMNS))
    _print(file, '|{: ^{width}}|\n'.format('', width=CONTENT_COLUMNS))

    # print question text
    _print(file, '|{}{: <{indexWidth}}{: ^{width}}|\n'.format(questionTitle, index, q.questionTexts[0], indexWidth = questionIndexDigits, width = QUESTION_HEADER_CONTENT_LEN))
    for i in range(1, len(q.questionTexts)):
        _print(file, '|{: ^{width}}|\n'.format(q.questionTexts[i], width=CONTENT_COLUMNS))

    # print space for answers
    for i in range(0, q.freeSpace - 1):
        _print(file, '|{: ^{width}}|\n'.format('', width=CONTENT_COLUMNS))

    #print question end
    _print(file, '|{:_^{width}}|\n'.format('', width=CONTENT_COLUMNS))

"""
Checks whether the question fits to the current page or not.
"""
def _remainingLinesCheck(file, question):
    # how many lines this question takes
    toPrintLines = 3 + len(question.questionTexts) + question.freeSpace

    if printedLines + toPrintLines >= linesPerPage:
        return False

    return True

"""
Prints single line noticing students that they need to check the other
page as well :).
"""
def _printNextPageNotice(file):
    _print(file, '{: >{width}}\n'.format('Nezapomeňte otočit na další stranu!', width=columnsPerLine))

"""
Fills the remainder of the page with empty lines.
"""
def _printEndOfPage(file):
    global printedLines
    for i in range(0, linesPerPage - printedLines):
        _print(file, '{: >{width}}\n'.format('', width=columnsPerLine))

    assert printedLines == linesPerPage
    printedLines = 0


"""
Wrapper around file.write method which counts printed lines.

The line count is stored in this script´s global variable and is used
for formatting purposes.
"""
def _print(file, text, newline = True):
    global printedLines

    file.write(text)

    if newline:
        printedLines = printedLines + 1
