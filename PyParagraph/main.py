import os
import re

#function to perform the operations on the paragraphs
def paragraph_operations(inputFilepath, delim):
    #open the paragraph file
    txtfile = open(inputFilepath, "r")
    paragraph = txtfile.read()

    #split the paragraph into an array of senteces
    if delim == "\n":
        sentences = re.split("(?<=[.!?])\"\n+|(?<=[.!?])\n", paragraph)
    elif delim == " ":
        sentences = re.split("(?<=[.!?])\" +|(?<=[.!?]) ", paragraph)

    #split the sencetences into words
    words = re.split(" ", paragraph)

    #count the letters
    letters = re.findall("\w", paragraph)

    #count the characters in the words
    # letters = 0
    # letterstest = 0
    # for word in words:
    #     letters += len(re.findall("\w", word))
    #     letterstest += len(word)
    
    # print(letters)
    # print("***", letterstest)
    # print("!!!", len(letterstest2))
    #print(sentences)
    
    #print results
    print("Paragraph Analysis")
    print("-----------------")
    print("Approximate Word Count:", len(words))
    print("Approximate Sentence Count:", len(sentences))
    print("Average Letter Count:", round(len(letters) / len(words),1))
    #print("***Average Letter Count:", round(letterstest / len(words),1))
    #print("!!!Average Letter Count:", round(len(letterstest2) / len(words),1))
    print("Average Sentence Length:", len(words) / len(sentences))

    # senTest = re.split("(?<=[.!?])\"\n+|(?<=[.!?])\n", paragraph)
    # #senTest = re.split("(\.\s)|(\.\"\s)", paragraph)
    # for i in range(len(senTest)):
    #     print(i, senTest[i])
    #     print()
    # print(len(senTest))


#setup variables to refernce files to be read locations
inputFilepathsample = "../python-challenge/PyParagraph/Resources/sample.txt"
inputFilepath1 = "../python-challenge/PyParagraph/Resources/paragraph_1.txt"
inputFilepath2 = "../python-challenge/PyParagraph/Resources/paragraph_2.txt"

#call the functions to analyze the paragraphs
print("Sample")
paragraph_operations(inputFilepathsample, " ")
print()

print("Paragraph 1")
paragraph_operations(inputFilepath1, " ")
print()

print("Paragraph 2")
paragraph_operations(inputFilepath2, "\n")
print()


