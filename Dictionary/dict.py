import json
from difflib import get_close_matches

#loading data
data = json.load(open("data.json"))

#funtion to get meaning of word
def meaning(word):
    meanings = ""
    #Changing list to string
    for meaning in data[word]:
        meanings = meanings + " ".join(meaning.split(" ")) + "\n"
    return meanings

def dict(word):
    #checking different cases
    if word in data.keys():
        return meaning(word)
    elif word.lower() in data.keys():
        return meaning(word.lower())
    elif word.title() in data.keys():
        return meaning(word.title())
    if word.upper() in data.keys():
        return meaning(word.upper())
    #Finding best matches
    elif len(get_close_matches(word, data.keys())) > 0:
        choice = input("did you mean %s ?(y/n)" % get_close_matches(word, data.keys())[0])
        if choice.lower() == 'y':
            return meaning(et_close_matches(word, data.keys())[0])
        else:
            return "Sorry we couldn't understand your entry"
    else:
        return "word doesn't exist"
