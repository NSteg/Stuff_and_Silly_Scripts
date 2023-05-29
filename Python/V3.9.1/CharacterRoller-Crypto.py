#!/usr/bin/python
# Python 3.9+
###############################################################################
## A script for 'rolling' character stats for D20 systems. 
# Pseudorandom numbers are generated using cryptographically compliant methods.
###############################################################################
## Provided as is. Distributable and extensible under GNU gpl 3.0
###############################################################################
## Author: Nicholas Stegelman
# Created: 2021-08-27


## Copyright: Copyright (C) 2021, CharacterRoller-Crypto

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


## Maintainers: Nicholas Stegelman
# Last Updated: 2022-05-16

## Version: 1.0.0

## Status: Development on Hold
###############################################################################

## System Imports
import argparse
import secrets
import string

# Set Up
parser = argparse.ArgumentParser()
parser.add_argument("--average", 
                    help="Use if you need a minimum average roll for a " + 
                    "character's stats.", type=int)
parser.add_argument("-c", help="Run once, roll more than one(1) Character", 
                    type=int)
parser.add_argument("--characters", 
                    help="Run once, roll more than one(1) Character", type=int)
argv = parser.parse_args()

# Main
rolls = [0, 1, 2, 3]
statBlock = [0, 1, 2, 3, 4, 5]


# Set variable for multiple rolls, if applicable
if argv.c:
    statArray = argv.c
elif argv.characters:
    statArray = argv.characters
else:
    statArray = 1

# Set a minimum average roll value, or use 0
threshold = 0
if argv.average:
    threshold = argv.average

# instantiate disposable iterator.
i = 0
# Create user specified number of stat blocks, or default to 1
while i < statArray:
    # Iterate through the six stats for each stat block
    for stat in range(len(statBlock)):
        # 'roll' 4d6 and store the values in List "rolls"
        for roll in range(len(rolls)):
            rolls[roll] = (secrets.randbits(64) % 6 + 1)
        # Sort list "rolls" from high to low
        rolls.sort(reverse=True)
        bestThree = 0
        # De facto drop lowest 'roll' and store sum of highest 3 in List
        #   "statBlock".
        for j in range(3):
            bestThree += rolls[j]
        statBlock[stat] = bestThree
    # Sort List "statBlock" for easier reading
    statBlock.sort(reverse=True)
    # Calculate average 'roll' in List "statBlock"
    aveRoll = 0
    for stat in statBlock:
        aveRoll += stat
    # Compare against user provided minimum, or use Default and 'reroll'
    #   if needed.
    if aveRoll//6 < threshold:
        continue
    else:
        # Print out aveRoll as both integer and floating division
        print("Crypto generated stats:", statBlock, '\n', "Average Roll:", 
            aveRoll//6, '(', round(aveRoll/6, 2), ")")
    i += 1

# TODO:
# Finish making GPL compliant --> print required paragraphs
# Consider reducing division operations on "aveRoll"
# Add timer?
# Better