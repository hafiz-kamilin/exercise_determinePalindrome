#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Mohd Hafizuddin Bin Kamilin"
__date__ = "27 May 2021"

# class for checking if the string is palindrome or not
class PalindromeCheck:

    def __init__(self, inputString):

        # reference for finding the trash symbol string from the inputString
        # NOTE: due to how python compiler deal with string, special characters 
        #       such as \, ", and ' must have a backslash (i.e. \" and \\) to be
        #       recognized as a proper string
        self.referenceTrash = "`~!@#$%^&*()-_=+[{]}\\|;:\'\",<.>/?"
        self.referenceTrashLength = len(self.referenceTrash)
        # get the inputString
        self.inputString = inputString
        # for storing the trashSymbolsFound found in the inputString
        self.trashSymbolsFound = ""
        # get the maximum index number
        self.maxIndex = len(inputString) - 1
        # index scanning for head and tail of inputString
        self.headIndex = 0
        self.tailIndex = 0
        # unless disproven, we assume the inputString is a palindrome
        self.palindrome = True
        # for recording the number of matching character found in the inputString
        self.matchingStringFound = 0

    # method for checking the trash symbol
    def checkForTrashSymbol(self, individualString):

        for symbol in range(self.referenceTrashLength):

            # return true if we found a trash symbol (no need to perform the comparison for this character)
            if (individualString == self.referenceTrash[symbol]):

                # if the trash symbol string have not being saved yet
                if not (individualString in self.trashSymbolsFound):

                    # save the trash symbol string
                    self.trashSymbolsFound += individualString

                return True
        
        # return false if no trash symbol found (perform the comparison)
        return False

    # method for checking if the string is palindrome or not
    def scanStringForPalindrome(self):

        # scan from the head part of inputString
        # NOTE: by ensuring the sum of headIndex and tailIndex is equal or less than the maxIndex,
        #       we can ensure the head and tail scanner won't be scanning the character on the same index.
        #       upholding the requirement of "InputString is scanned only once".
        while ((self.headIndex + self.tailIndex <= self.maxIndex) and (self.headIndex != self.maxIndex - self.tailIndex)):

            # if character starting from the head is not a trash symbol
            if (self.checkForTrashSymbol(self.inputString[self.headIndex]) == False):

                # scan from the tail part of inputString
                # NOTE: by ensuring the sum of headIndex and tailIndex is equal or less than the maxIndex,
                #       we can ensure the head and tail scanner won't be scanning the character on the same index.
                #       upholding the requirement of "InputString is scanned only once".
                while ((self.headIndex + self.tailIndex <= self.maxIndex) and (self.headIndex != self.maxIndex - self.tailIndex)):

                    # if character starting from the tail is not a trash symbol
                    if (self.checkForTrashSymbol(self.inputString[self.maxIndex - self.tailIndex]) == False):

                        # if the characters matched
                        if (self.inputString[self.headIndex] == self.inputString[self.maxIndex - self.tailIndex]):

                            self.matchingStringFound += 1
                            # increment the index to find another matching tail character
                            self.tailIndex += 1
                            break

                        # the inputString is not a palindrome
                        else:

                            self.palindrome = False
                            break

                    # increment the index to find matching character
                    self.tailIndex += 1

            # increment the index to find character without trash symbol
            self.headIndex += 1

        # if head scanner and tail scanner are pointing on the same index
        if (self.headIndex == self.maxIndex - self.tailIndex):

            # use head scanner (headIndex) only to check if the character is a trash symbol or not
            self.checkForTrashSymbol(self.inputString[self.headIndex])

        # if there is no maching character found
        if (self.matchingStringFound == 0):

            # inputString with only 1 character is definitely not a palindrome
            self.palindrome = False

        # (optional) sort the trashSymbolsFound to match with the Sitecore Technical Assignment's answer
        self.trashSymbolsFound = "".join(sorted(self.trashSymbolsFound, key = self.referenceTrash.index))

# main
if __name__ == "__main__":

    print("\nDo note due to how Python interpreter handle the string, trash symbol such as \\, \", and ' must have a backslash added before the symbol!")
    print("Write the string (trash symbol will be ignored) to check if it is a palindrome or not.\n")
    inputString = input("InputString: ")

    pCheck = PalindromeCheck(inputString)
    # perform the palindrome check
    pCheck.scanStringForPalindrome()
    # show the results
    print("TrashSymbolsString: " + pCheck.trashSymbolsFound)
    print("Result should be: " + str(pCheck.palindrome) + "\n")
