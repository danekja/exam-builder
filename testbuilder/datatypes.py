from typing import NamedTuple

"""
Class representing single test question. Contains the text as well as any metadata
for formatting.
"""
class TestQuestion:

    def __init__(self, questionTexts, freeSpace = 4):
        self.questionTexts = questionTexts
        self.freeSpace = freeSpace

"""
Represents definition of a test part - source of questions
and number of questions to be present from the particular source.
"""
class TestDefinition(NamedTuple):
    src: str
    count: int
