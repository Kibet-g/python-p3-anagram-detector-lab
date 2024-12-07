# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Store the word in lowercase

    def match(self, word_list):
        # Sort the letters in the original word
        sorted_word = sorted(self.word)

        # Return words from the list that are anagrams of the original word
        return [word for word in word_list if sorted(word.lower()) == sorted_word]
