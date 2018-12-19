import random
import printer

import data as d

############################################
#           Configuration variables
############################################
outputFile = "pokus.txt"
nbOfTests = 45
questionsPerTest = 10

############################################
#            Code
############################################

def createTests(number = 0, dataname = ""):
    for i in range(0, number):
        test = _generateTest(dataname)
        printer.printTest(outputFile, test)

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


if __name__ == '__main__':
    createTests(nbOfTests, "2018_01")