#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

secret = random.randint(1, 30)
print secret

def main():
    while True:
        guess = int(raw_input("Guess the secret number (between 1 and 30): "))
        if guess == secret:
            print "You guessed it - congratulations! It's number: " + str(secret)
            break

        else:
            print "Sorry, your guess is not correct... Secret number is not " + str(guess)

if __name__ == "__main__":
    main()