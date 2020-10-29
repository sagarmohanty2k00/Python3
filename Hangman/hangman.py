#!/usr/bin/python3
import random


def get_word():
    file = open('wordlist.txt')
    f = file.readlines()
    i = random.randrange(0, len(f) - 1)

    return f[i][:-1]


def display_hangman(tries):
    dis = ['''
    -------------
          |     |
        (o o)   |
          |     |
        / | \   |
       /  |  \  |
         / \    |
        /   \   |

            ''',
      
            '''
      -------------
          |     |
        (o o)   |
          |     |
        / | \   |
       /  |  \  |
           \    |
            \   |

            ''',
            '''
      -------------
          |     |
        (o o)   |
          |     |
        / | \   |
       /  |  \  |
                |
                |

            ''',
            '''
      -------------
          |     |
        (o o)   |
          |     |
          | \   |
          |  \  |
                |
                |

            ''',
            '''
      -------------
          |     |
        (o o)   |
          |     |
          |     |
          |     |
                |
                |

            ''',
            '''
      -------------        
          |     |
        (o o)   |
                |
                |
                |
                |
                |

            ''',
            '''
      -------------
          |     |
                |
                |
                |
                |
                |

            ''']
    print(dis[tries])



def play(word):
    word_completion  = "_"*len(word)

    word_as_list = list(word_completion)
    indices = [i for i, letter in enumerate(word) if letter == " "]
    for index in indices:
        word_as_list[index] = " "
    word_completion = "".join(word_as_list)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6


    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter",guess)
            elif guess not in word:
                print(guess,"is not in the word")
                tries = tries - 1
                guessed_letters.append(guess)
            else:
                print("Good Job ", guess, " is in the word")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word..",guess)
            elif guess in word:
                print(guess, "is not the word.")
                tries = tries-1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was ", word)





play(get_word())















