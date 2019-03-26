from testbuilder.datatypes import TestQuestion

data = {
    "easy": [
        TestQuestion(["Easy question 1?"]),
        TestQuestion(["Easy question 2?"]),
        TestQuestion(["Easy question multiline",
                      " continued multiline?"]),
    ],
    "medium": [
        TestQuestion(["Medium question 1?"]),
        TestQuestion(["Medium question multiline",
                      " continued multiline?"]),
    ],
    "hard": [
        TestQuestion(["Hard question 1?"]),
        TestQuestion(["Hard question 2?"])
    ]
}