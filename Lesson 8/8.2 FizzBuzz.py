#!/usr/bin/env python
# -*- coding: utf-8 -*-
while True:
    print "FizzBuzz"
    fb = raw_input("Please enter a number between 1 and 100: ")

    try:
        fb = int(fb)

        for num in range(1, fb + 2):
            if num % 3 == 0 and num % 5 == 0:
                print "fizzbuzz"
            elif num % 5 == 0:
                print "buzz"
            elif num % 3 == 0:
                print "fizz"
            else:
                print num
    except Exception as e:
        print "Please enter a number, not text!"



    choice = raw_input("Would you like to do another number (y/n): ")
    if choice.lower() != "y" and choice.lower() != "yes":
        break