"""
This is the very first program I have followed through in a tutorial and 
managed to write from start to finish. Tonnes of errors in the process but here we are.
I tried it more than once to make to work. I am very proud it did.
"""
import json
from difflib import get_close_matches
from googletrans import Translator

data = json.load(open("data.json"))

def translate(w):
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
output = translate(word)

if type(output) == list:
	for item in output:
		print(item)
else:
	print(output)