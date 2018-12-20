import random
from testbuilder import printer
from testbuilder import datatypes as types

from testbuilder import data as d

############################################
#           Configuration variables
############################################
outputFile = "pokus.txt"
nbOfTests = 10

############################################
#            Code
############################################

"""
Generates and prints given number of tests based on the
passed testDefinitions.
"""
def createTests(testDefinitions, number = 0):
    for i in range(0, number):
        test = _generateTest(testDefinitions)
        printer.printTest(outputFile, test)

"""
Prepares single test based on the given definitions list.

Returns list of TestQuestion instances representing the test.
"""
def _generateTest(definitions):
    testData = []

    for definition in definitions:
        data = d.data[definition.src]
        seq = _generateTestSequence(definition.count, len(data))

        for i in seq:
            testData.append(data[i])

    return testData

"""
Generates sequence of unique numbers in range 0..srcSize
which identify the questions used in the given test.

The amount parameter is the length of the returned sequence and must be
smaller or equal to the source dataset size.
"""
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

""""
Returns random integer from the range 0..srcSize.

Used to pick random question from the source dataset.
"""
def _getRandomQuestionIndex(srcSize):
    return random.randrange(0, srcSize)


if __name__ == '__main__':
    definitions = [types.TestDefinition("2018_zk_pers", 4),
                   types.TestDefinition("2018_zk_qa", 1),
                   types.TestDefinition("2018_zk_sec", 4),
                   types.TestDefinition("2018_zk_devops", 1),
                   types.TestDefinition("2018_zk_arch", 6),
                   types.TestDefinition("2018_zk_wss", 4),
                   types.TestDefinition("2018_zk_med", 1),
                   types.TestDefinition("2018_zk_long", 1)]

    createTests(definitions, nbOfTests)