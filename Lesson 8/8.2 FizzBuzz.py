#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "FizzBuzz"
for x in range(3):
  FB = raw_input("Please enter a number between 1 and 100: ")


try:
    FB = int(FB)

    for num in range(1, FB+1):
        if num % 3 == 0:
            print "fizz"
        elif num % 5 == 0:
            print "buzz"
        elif num % 3 == 0 and num % 5 == 0:
            print "fizzbuzz"

        else:
            print num

except Exception as e:
        print "Please enter a number, not text!"

choice = raw_input("Would you like to do another number (y/n): ")

if choice.lower() != "y" and choice.lower() != "yes":
break
