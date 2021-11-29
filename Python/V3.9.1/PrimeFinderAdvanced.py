#!/usr/bin/python
# Python 3.9+
###############################################################################
## An upgraded version of the common Prime number finding introductory 
# programming assignment.
###############################################################################
## Provided as is. Distributable and extensible under GNU gpl 3.0
###############################################################################
## Author: Nicholas Stegelman
# Created: 2021-08-29
# Version: 0.5


## Copyright: Copyright (C) 2021, profileXX

## License: GNU GPL 3.0 : https://www.gnu.org/licenses/gpl-3.0.en.html

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

## Ver.0.1.0

## Maintainers: Nicholas Stegelman
# Last Updated: 2021-09-02

## Status: In Development
###############################################################################

## System Imports
import math
import secrets


## Variables
opening = '''\nEnter a number (x) and this program will tell you how many prime 
numbers there are between 1 and x. The program will also print the prime 
numbers to a file and save it to the desktop/workspace.\n'''

xPrompt = "Enter a whole number greater than 1: "


# A quasi brute force function intended to find the primes below 101
def quickPrime(n):
    primes100 = []
    primes100.append(2)
    # Test all numbers between 2 and n
    for i in range(2, n):
        # print("LÖÖP") # Test print()
        #
        pVal = True
        j = 2
        while j < (math.sqrt(i) + 1):
            if i % j == 0:
                pVal = False
                break
            # end IF
            j += 1
        # end While LOOP
        if pVal == True:
            primes100.append(i)
        # end for LOOP
    return primes100

# A better function that tests using prime factors, up to the square root of
# the number (n) being tested for primeness.
def slowPrime(n, primes[]):
    # The itterative storage variable for √(101) .. √(n) 
    targetRoot = sqrt(101)
    # The closest Prime Factor above the √(n)
    upperPrimeRoot = 11
    # The closest Prime Factor below the √(n)
    lowerPrimeRoot = 7


# Main -- Pure Python Heresy, I know. 
# I strongly prefer compiled languages, and not having some kind of main() 
# is just wrong. 
# I'm not apologizing.
def main():

    primeList = []

    print(opening)
    while True:
        xVal = input(xPrompt)
        # Type check for non-numerical input
        try:
            xVal = int(xVal)
        except ValueError:
            print("*X* That wasn't a number. \n\n")
            continue # Back to the top of the loop
        else:
            if xVal <= 1:
                print('''*X* Primes are explicitly positive
                 and greater than 1.\n\n''')
                continue  # Back to the top of the loop
            else:
                break # Exit loop and continue execution
            # End of IF
        # End of TRY block
    # End of While LOOP
    # print(xVal) # Test print()
    if xVal < 101:
        primeList = quickPrime(xVal)
    else:
        primeList = quickPrime(100)
        print("Testing for 100")
        pass
    # end IF/ELSE
    print("There are ", len(primeList), " between 1 and ", xVal, ".", sep="")
    print("They are:", primeList)

    # end For LOOP
# end of MAIN()

  
# Completing the Blasphamy
if __name__ == "__main__":
    main()

# Because I needed a quick place to store this : Deathwish Coffee Referal Code
# http://i.refs.cc/pvIFfH19?smile_ref=eyJzbWlsZV9zb3VyY2UiOiJzbWlsZV91aSIsInNtaWxlX21lZGl1bSI6IiIsInNtaWxlX2NhbXBhaWduIjoicmVmZXJyYWxfcHJvZ3JhbSIsInNtaWxlX2N1c3RvbWVyX2lkIjpudWxsfQ%3D%3D