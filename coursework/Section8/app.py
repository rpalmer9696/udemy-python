import json
import difflib
import pandas


def get_definition(word):
    match = difflib.get_close_matches(word, data.keys(), 1, 0.8)

    if word in data:
        return data[word]
    elif match:
        if input("Did you mean %s instead? y/n\n" % match[0]) == "y":
            return data[match[0]]

    return "Sorry the word couldn't be found"


def display_definition(definition):
    if type(definition) is not str:
        [print(i) for i in definition]
    else:
        print(definition)


with open("data.json", "r") as file:
    data = json.load(file)


userInput = ""
while userInput.lower() != "n":
    userInput = input("Enter a word:\n")
    display_definition(get_definition(userInput))
    userInput = input("\nWould you like to pick another word? y/n\n")

