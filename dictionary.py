import json
from difflib import get_close_matches
from googletrans import Translator

with open("data.json") as words_file:
	data = json.load(words_file)

def translate_word(word, langcode):
	translator = Translator()
	translation = translator.translate(word, dest=langcode)

while True:
	word = input("Enter your word: ")
	word = word.strip().lower()
	