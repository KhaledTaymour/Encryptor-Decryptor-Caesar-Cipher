import math

class Helper:
    #constructor having inputs: list of colleges, departments, students, courses
    def __init__(self):
        
        #alphabet is a data structure to hold info about each English letter
        
        self.alphabet = [{"originalOrder": 1, "letter": "A", "originalFrequency": 8.12, "currentFrequency": 0 , "currentCount": 0}, { "originalOrder": 2, "letter": "B", "originalFrequency": 1.49, "currentFrequency": 0 , "currentCount": 0}, { "originalOrder": 3, "letter": "C", "originalFrequency": 2.71, "currentFrequency": 0 , "currentCount": 0}, { "originalOrder": 4, "letter": "D", "originalFrequency": 4.32, "currentFrequency": 0 , "currentCount": 0}, { "originalOrder": 5, "letter": "E", "originalFrequency": 12.02, "currentFrequency": 0 , "currentCount": 0}, { "originalOrder": 6, "letter": "F", "originalFrequency": 2.30
, "currentFrequency": 0 , "currentCount": 0}, { "originalOrder": 7, "letter": "G", "originalFrequency": 2.03, "currentFrequency": 0 , "currentCount": 0}, { "originalOrder": 8, "letter": "H", "originalFrequency": 5.92, "currentFrequency": 0 , "currentCount": 0}, { "originalOrder": 9, "letter": "I", "originalFrequency": 7.31, "currentFrequency": 0 , "currentCount": 0}, { "originalOrder": 10, "letter": "J", "originalFrequency": 0.10, "currentFrequency": 0 , "currentCount": 0}, { "originalOrder": 11, "letter": "K", "originalFrequency": 0.69, "currentFrequency": 0 , "currentCount": 0}, { "originalOrder": 12, "letter": "L", "originalFrequency": 3.98, "currentFrequency": 0 , "currentCount": 0}, { "originalOrder": 13, "letter": "M", "originalFrequency": 2.61, "currentFrequency": 0 , "currentCount": 0}, { "originalOrder": 14, "letter": "N", "originalFrequency": 6.95, "currentFrequency": 0 , "currentCount": 0}, { "originalOrder": 15, "letter": "O", "originalFrequency": 7.68, "currentFrequency": 0 , "currentCount": 0}, { "originalOrder": 16, "letter": "P", "originalFrequency": 1.82
, "currentFrequency": 0 , "currentCount": 0}, { "originalOrder": 17, "letter": "Q", "originalFrequency": 0.11, "currentFrequency": 0 , "currentCount": 0}, { "originalOrder": 18, "letter": "R", "originalFrequency": 6.02, "currentFrequency": 0 , "currentCount": 0}, { "originalOrder": 19, "letter": "S", "originalFrequency": 6.28, "currentFrequency": 0 , "currentCount": 0}, { "originalOrder": 20, "letter": "T", "originalFrequency": 9.10, "currentFrequency": 0 , "currentCount": 0}, { "originalOrder": 21, "letter": "U", "originalFrequency": 2.88, "currentFrequency": 0 , "currentCount": 0}, { "originalOrder": 22, "letter": "V", "originalFrequency": 1.11, "currentFrequency": 0 , "currentCount": 0}, { "originalOrder": 23, "letter": "W", "originalFrequency": 2.09, "currentFrequency": 0 , "currentCount": 0}, { "originalOrder": 24, "letter": "X", "originalFrequency": 0.17, "currentFrequency": 0 , "currentCount": 0}, { "originalOrder": 25, "letter": "Y", "originalFrequency": 2.11, "currentFrequency": 0 , "currentCount": 0}, { "originalOrder": 26, "letter": "Z", "originalFrequency": 0.07, "currentFrequency": 0 , "currentCount": 0}]
        
        
        # keysCorrelationCoefficient holds the correlation coefficient for each English letter
        
        self.keysCorrelationCoefficient = [{"key": 0, "corCoef": 0}, {"key":  1, "corCoef": 0}, {"key": 2, "corCoef": 0}, {"key": 3, "corCoef": 0}, {"key": 4, "corCoef": 0}, {"key": 5, "corCoef": 0}, {"key": 6, "corCoef": 0}, {"key": 7, "corCoef": 0}, {"key": 8, "corCoef": 0}, {"key": 9, "corCoef": 0}, {"key": 10, "corCoef": 0}, {"key": 11, "corCoef": 0}, {"key": 12, "corCoef": 0}, {"key": 13, "corCoef": 0}, {"key": 14, "corCoef": 0}, {"key": 15, "corCoef": 0}, {"key": 16, "corCoef": 0}, {"key": 17, "corCoef": 0}, {"key": 18, "corCoef": 0}, {"key": 19, "corCoef": 0}, {"key": 20, "corCoef": 0}, {"key": 21, "corCoef": 0}, {"key": 22, "corCoef": 0}, {"key": 23, "corCoef": 0}, {"key": 24, "corCoef": 0}, {"key": 25, "corCoef": 0}, {"key": 26, "corCoef": 0}]
        
######## Helper Functions ###########
        
    # Check if the character is an self.alphabet ir not
    # return true or false
    def isCharacterFoundInAlphabet(self, char):
        foundChar = False

        for j in range(len(self.alphabet)):
            if self.alphabet[j]["letter"] == char.upper():
                foundChar = True
                break

        return foundChar
        
        
   # gets the character by its order in the self.alphabet
    def getCharacterByOrder(self, order):
        letter = None

        for i in range(len(self.alphabet)):

            if self.alphabet[i]["originalOrder"] == order:
                letter = self.alphabet[i]["letter"]
                break

        return letter        
    
    # apply shift on the character & returns the shifted one
    def getShiftedChar(self, char, shift):
        newOrder = char["originalOrder"] + shift

        if newOrder > 26:
            newOrder = newOrder - 26
        elif newOrder < 1:
            newOrder = newOrder + 26

        shiftedCharacter = self.getCharacterByOrder(newOrder)
        if shiftedCharacter == None:
            return char["letter"]
        else:
            return shiftedCharacter


    # takes the original text & the key and returns the shifted text
    def makeShift(self, text, shift):
        shiftedText = ''

        for i in range(len(text)):
            currentChar = text[i]

            if self.isCharacterFoundInAlphabet(currentChar):
                isCaps = currentChar.isupper()

                for j in range(len(self.alphabet)):
                    if self.alphabet[j]["letter"] == currentChar.upper():
                        shiftedChar = self.getShiftedChar(self.alphabet[j], shift)

                        if not(isCaps):
                            shiftedChar = shiftedChar.lower()
                        shiftedText += (shiftedChar)
                        break

            else:
                shiftedText += currentChar

            # remove escaping characters 
            shiftedText = shiftedText.replace('\n','')
            shiftedText = shiftedText.replace('\t','')
            shiftedText = shiftedText.replace("\'s","'s")

        return shiftedText


    # function to encrypt using cauesar cipher
    def encrypt(self, text, key):
        return self.makeShift(text, key)
    
    # function to decrypt using cauesar cipher
    def decrypt(self, text, key):
        return self.makeShift(text, -key)
    
    # function to reset the frequency value for each letter
    def resetAlphabet(self):
        for j in range(len(self.alphabet)):
            self.alphabet[j]["currentCount"] = 0
            self.alphabet[j]["currentFrequency"] = 0
            
    # calculates the frequency for each English letter
    def calculateFrequencyPerEachLetter(self, text):
        totalNumberOfAlphabetCharacters = 0

        self.resetAlphabet()

        for i in range(len(text)):
            currentChar = text[i]

            if self.isCharacterFoundInAlphabet(currentChar):
                totalNumberOfAlphabetCharacters += 1

                for j in range(len(self.alphabet)):
                    if currentChar.upper() == self.alphabet[j]["letter"]:
                        self.alphabet[j]["currentCount"] += 1

        for m in range(len(self.alphabet)):
            self.alphabet[m]["currentFrequency"] = self.alphabet[m]["currentCount"] / totalNumberOfAlphabetCharacters

        return self.alphabet
    
    ################ Helper functions for correlation coefficient #####################
    def calculateSigmaXY(self):
        total = 0

        for j in range(len(self.alphabet)):
            total += (self.alphabet[j]["originalFrequency"] * self.alphabet[j]["currentFrequency"])

        return total

    def calculateSigmaX(self):
        total = 0

        for j in range(len(self.alphabet)):
            total += self.alphabet[j]["originalFrequency"]

        return total

    def calculateSigmaY(self):
        total = 0

        for j in range(len(self.alphabet)):
            total += self.alphabet[j]["currentFrequency"]

        return total

    def calculateSigmaXSquare(self):
        total = 0

        for j in range(len(self.alphabet)):
            total += (self.alphabet[j]["originalFrequency"] * self.alphabet[j]["originalFrequency"])

        return total

    def calculateSigmaYSquare(self):
        total = 0

        for j in range(len(self.alphabet)):
            total += (self.alphabet[j]["currentFrequency"] * self.alphabet[j]["currentFrequency"])

        return total    

    # calculates the Correlation Coefficient
    def calculateCorrelationCoefficient(self):
        numerator = 26 * self.calculateSigmaXY() - (self.calculateSigmaX() * self.calculateSigmaY())
        denomenator = (math.sqrt(26 * self.calculateSigmaXSquare() - (self.calculateSigmaX())**2 )) * (math.sqrt(26 * self.calculateSigmaYSquare() - (self.calculateSigmaY())**2 ))

        return numerator / denomenator
    
    # Brute Force on a cipherText; decrypt it & gets its key
    def bruteForceCipher(self, cipherText):
        topKey = None
        topKeyCorCoef = 0

        for k in range(len(self.keysCorrelationCoefficient)):
            # 1. decrypt
            decryptedText = self.decrypt(cipherText, self.keysCorrelationCoefficient[k]["key"])

            # 2. Calculate letters Frequency
            self.calculateFrequencyPerEachLetter(decryptedText)

            # 3. calculate & set correlation coefficient for each key
            self.keysCorrelationCoefficient[k]["corCoef"] = self.calculateCorrelationCoefficient()

            if self.keysCorrelationCoefficient[k]["corCoef"] > topKeyCorCoef:
                topKeyCorCoef = self.keysCorrelationCoefficient[k]["corCoef"]
                topKey = self.keysCorrelationCoefficient[k]["key"]

        print(f'Key to decrypt: {topKey}')
        print(f'decrypted Text: {self.decrypt(cipherText, topKey)}')

        #return topKey