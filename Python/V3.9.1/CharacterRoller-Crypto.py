#!/usr/bin/python
# Python 3.9+
###############################################################################
## A script for 'rolling' character stats for D20 systems. 
# Psudorandom numbers are generated using cryptographically compliant methods.
###############################################################################
## Provided as is. Distributable and extensible under GNU gpl 3.0
###############################################################################
## Author: Nicholas Stegelman
# Created: 2021-08-27
# Version: 0.5


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

## Ver.0.1.0

## Maintainers: Nicholas Stegelman
# Last Updated: 2022-05-16

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
    # print("average caught\n") # Debug Print
    threshold = argv.average
# print("Target Average: ", threshold, '\n') # Debug Print

i=0
while i < statArray:
    for stat in range(len(statBlock)):
        # print(stat) # Debug Print
        for roll in range(len(rolls)):
            # print("Roll: ", roll+1) # Debug Print
            rolls[roll] = (secrets.randbits(64) % 6 + 1)
        # print("Before Sort: ", rolls) # Debug Print
        rolls.sort(reverse=True)
        # print("After Sort: ", rolls) # Debug Print
        bestThree = 0
        for j in range(3):
            bestThree += rolls[j]
        #print(bestThree) # Debug Print
        statBlock[stat] = bestThree
    statBlock.sort(reverse=True)
    aveRoll = 0
    for stat in statBlock:
        aveRoll += stat
    # print("For", i, ": aveRoll is ", aveRoll//6) # Debug Print
    if aveRoll//6 < threshold:
        continue
    else:
        # aveRoll = aveRoll // 6 # Integer Division
        print("Crypto generated stats:", statBlock, '\n', "Average Roll:", 
            aveRoll//6, '(', round(aveRoll/6, 2), ")\n")
    i += 1

# TODO:
# Add timer?
# Better