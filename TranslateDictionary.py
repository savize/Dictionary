import json
from difflib import get_close_matches

data = json.load(open("projects/data.json"))

while True:
    def dictionary(w):
        w = w.lower()
        if w in data:
            return (data[w])
        elif w.title() in data:
            return data[w.title()]
        elif w.upper() in data:
            return data[w.upper()]
        elif len(get_close_matches(w, data.keys())) > 0 :
            guess = input (f"Did u mean '{get_close_matches(w, data.keys())[0]}' instead? Y for Yes , N for No:").upper()
            if guess == 'Y':
                return (data[get_close_matches(w, data.keys())[0]])
            elif guess == 'N':
                b = input (f"Choose one: {get_close_matches(w, data.keys())}:")
                if b in (f"{get_close_matches(w, data.keys())}"):
                    return (data[b])
                else :
                    return ("Sorry! I can't get your mean!")
            else:
                return ("Check the spelling, please!")
        else:
            return ("Check the spelling, please!")

    word = input("\nTell me your word:")
    result = dictionary(word)

    if isinstance(result, list):
        for item in result:
            print(item)
    else:
        print(result)