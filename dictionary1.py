import json
from difflib import get_close_matches

data = json.load(open("Dictionary\data.json"))

def meaning(word):
    word1 = word.lower()
    if word1 in data:
        return data[word1]
    elif word in data:
        return data[word]
    elif len(get_close_matches(word1, data.keys())):
        yn = input("Did you mean %s? Enter 'Y' for 'Yes' and 'N' for 'No': " % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word1, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please enter something meaningful ;)"
        else:
            return "Sorry, We didn't get you :("
    else:
        return "The word doesn't exist. Please enter something meaningful ;)"

word = input("Enter a word: ")

output = meaning(word)
if type(output) == list:
    for item in output:
        print(str(output.index(item) + 1) + "." + item)
else:
    print(str(output))
