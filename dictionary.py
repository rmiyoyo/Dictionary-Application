import json
from difflib import get_close_matches
from googletrans import Translator

# load dictionary file
with open("data.json") as words_file:
    data = json.load(words_file)


def word_definition(word):
    """
    function to return meaning of word from the json file.
    """

    # if word in data, return the word
    if word in data:
        if len(data[word]) == 1:
            return f"1. {data[word][0]}."
        else:
            definitions = data[word]
            multiple_meanings = "\n".join(
                [f"{i+1}. {definition}" for i, definition in enumerate(definitions)]
            )
            return multiple_meanings

    # if word not in data, get close matches
    elif len(get_close_matches(word, data.keys())) > 0:
        closest_word = get_close_matches(word, data.keys())[0]
        user_confirmation = input(
            f"Did you mean {closest_word}? Enter Y if yes, N if No: "
        )
        user_confirmation = user_confirmation.upper()

        if user_confirmation == "Y":
            if len(data[closest_word]) == 1:
                return f"1. {data[closest_word][0]}"
            else:
                definitions = data[closest_word]
                multiple_meanings = "\n".join(
                    [f"{i+1}. {definition}" for i, definition in enumerate(definitions)]
                )
                return multiple_meanings
        elif user_confirmation == "N":
            return f"{word.upper()} is not available."
        else:
            return "Answer not understood."
    else:
        return "This word does not exist in our dictionary."


def word_translator(word, dest="es"):
    """
    function that accepts two inputs, a word and the language it is to
    be translated to and returns the translation.
    """
    translate_variable = Translator()
    translation = translate_variable.translate(word, dest="es")
    return translation.text


def main():
    """
    main function to get user choices and call the appropriate
    functions depending on user choices.
    """
    print("Welcome to Our Dictionary Program.")
    print("\tMenu")
    print("1. Dictionary\n2. Translator")
    user_choice = input("Enter your choice: ")

    if int(user_choice) == 1:
        user_input = input("Enter word to be searched:")
        definition = word_definition(user_input)
        print(definition)
    elif int(user_choice) == 2:
        word_translation = input("Enter word to be translated: ")
        word_translator(word_translation)
    else:
        print("Sorry, we did not understand your choice.")


if __name__ == "__main__":
    main()
