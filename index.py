from functools import reduce
from random import randrange
import os


data = []

def read_words():
  with open("./files/data.txt", "r", encoding="utf-8") as f:
    [data.append(word.split("\n")[0]) for word in f]

def random_words():
  number = randrange(len(data))
  return data[number]

def validate_word(word):
  continue_game = True
  letters = []
  word_size = []
  verify_word = word

  while continue_game == True:
    separator = ""
    word_size = []
    os.system("clear")

    for word in verify_word:
      word_size.append("_ ")
    print(separator.join(word_size))
    print(letters)

    letter = input("Ingrese una letra: ")
    for word in verify_word:
      if letter == word:
        letters.append(letter)
        print(letters)
    # print(letters)

def run():
  read_words()
  word = random_words()
  validate_word(list(word))


if __name__ == "__main__":
  run()