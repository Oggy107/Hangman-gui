import random

from data.wordList import wordList

def getWord():
    word = random.choice(wordList)

    letterList = list(word)
    listForDic = list(word)
    ansDic = {}
    wordToGuess = ""

    if len(word) <= 4:
        count = 2
   
        while count:
            randomNum = random.randint(0, (len(word)-1))
            ansDic[randomNum] = listForDic[randomNum]
            letterList[randomNum] = '-'
            count -= 1

    elif len(word) <= 6:
        count = 3

        while count:
            randomNum = random.randint(0, (len(word)-1))
            ansDic[randomNum] = listForDic[randomNum]
            letterList[randomNum] = '-'
            count -= 1

    elif len(word) <= 8:
        count = 4

        while count:
            randomNum = random.randint(0, (len(word)-1))
            ansDic[randomNum] = listForDic[randomNum]
            letterList[randomNum] = '-'
            count -= 1

    elif len(word) <= 10:
        count = 5

        while count:
            randomNum = random.randint(0, (len(word)-1))
            ansDic[randomNum] = listForDic[randomNum]
            letterList[randomNum] = '-'
            count -= 1

    elif len(word) <= 14:
        count = 7

        while count:
            randomNum = random.randint(0, (len(word)-1))
            ansDic[randomNum] = listForDic[randomNum]
            letterList[randomNum] = '-'
            count -= 1

    else:
        count = 9

        while count:
            randomNum = random.randint(0, (len(word)-1))
            ansDic[randomNum] = listForDic[randomNum]
            letterList[randomNum] = '-'
            count -= 1

    for letter in letterList:
        wordToGuess += letter

    return wordToGuess, word, ansDic

class engine:
    EASY = 1
    NORMAL = 2
    HARD = 3

    def __init__(self):
        self._ques, self._ans, self._ansDic = getWord()
        self._letterList = list(self._ques)
        self._difficulty = engine.EASY
        self._retries = 0
        self._guessed = False

        self.initializeDifficulty()

    def getQues(self):
        return self._ques

    def getAns(self):
        return self._ans

    def getAnsDic(self):
        return self._ansDic

    @property
    def difficulty(self):
        return self._difficulty

    def initializeDifficulty(self):
        if self._difficulty == engine.EASY:
            self._retries = 6

        elif self._difficulty == engine.NORMAL:
            self._retries = 5

        elif self._difficulty == engine.HARD:
            self._retries = 3

    def getRetries(self):
        return self._retries

    def evaluate(self, guess):
        if self._guessed == True:
            return "won"

        elif not self._retries:
            return "lost"

        if guess in self._ansDic.values():
            newQues = ""

            keys = list(self._ansDic.keys())
            values = list(self._ansDic.values())

            pos = values.index(guess)
            pos = keys[pos]

            self._letterList[pos] = guess
            for letter in self._letterList:
                newQues += letter
            self._ques = newQues

            self._ansDic.pop(pos)

            if self._ques == self._ans:
                self._guessed = True
                return "won"

            return "right"

        else:
            self._retries -= 1
            return "wrong"