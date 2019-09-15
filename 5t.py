import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open(r"G:\Study\Programming languages\Python\Udemy - The Python Mega Course Build 10 Real World Applications\08 Application 1 Building an Interactive Dictionary\076 data.json"))
print(data)

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        else:
            return("Did you mean %s instead? Enter Y if yes, N if no" % get_close_matches(w, data.keys())[1])
    else:
        return "This wort doesn't exist. Please double check it."
word = input("Enter word: ")

print(translate(word))