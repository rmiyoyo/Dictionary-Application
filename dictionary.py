import json
from difflib import get_close_matches
from googletrans import Translator

data = json.load(open("data.json"))

def translate_word(w):
	w = w.lower()#Helps ignore the user's punctuation of first word.
	if w in data:
		return data[w]
	elif len(get_close_matches(w, data.keys())) > 0:
		yn = input("Did you mean %s instead? Reply with Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
		yn = yn.upper()
		if yn == "Y":
			return data[get_close_matches(w, data.keys())[0]]
		elif yn == "N":
			return "The word does not exist. Please double check."
		else:
			return "We did not understand your reply."
	else:
		return "The word does not exist. Please double check."
	pass

word = input("Enter your word: ")
translator = Translator()
print(translator.translate(word, dest='sw'))
output = translator.translate(translate_word(word), dest='sw')

if type(output) == list:
	for item in output:
		print(item)
else:
	print(output)