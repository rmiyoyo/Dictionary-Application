import json
from difflib import get_close_matches
# from googletrans import Translator

# load dictionary file
with open("data.json") as words_file:
	data = json.load(words_file)

def word_definition(word):
	"""
	function to return meaning of word from the json file.
	"""

	# if word in data, return the word
	if word in data:
		return data[word]

	# if word not in data, get close matches
	elif len(get_close_matches(word, data.keys())) > 0:
		closest_word = get_close_matches(word, data.keys())[0]
		user_confirmation = input(f"Did you mean {closest_word}? Enter Y if yes, N if No: ")
		user_confirmation = user_confirmation.upper()

		if user_confirmation == "Y":
			return data[closest_word]
		elif user_confirmation == "N":
			return f"{word.upper()} is not available."
		else:
			return "Answer not understood."
	else:
		return "This word does not exist in our dictionary."

def main():
	user_input = input("Enter word to be searched: ")
	definition = word_definition(user_input)
	print(definition)

if __name__ == "__main__":
	main()