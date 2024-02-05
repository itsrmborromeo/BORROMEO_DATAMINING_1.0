wordContainer = "Face every challenge with faith"

words = 0

for i in wordContainer:

    if i == " " or i == "\t" or i == "\n":

        words += 1

if len(wordContainer) > 0:
    print("Number of words:", words + 1)

else:
    print("Number of words: 0")