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
# Last Updated: 2021-08-27

## Status: In Development
###############################################################################

## System Imports
import string
import secrets

# Main
rolls = [0, 1, 2, 3]
statBlock = [0, 1, 2, 3, 4, 5]

for stat in statBlock:
    # print(stat) # Debug Print
    for roll in range(4):
        # print("Roll: ", roll+1) # Debug Print
        rolls[roll] = (secrets.randbits(64) % 6 + 1)
    # print("Before Sort: ", rolls) # Debug Print
    rolls.sort(reverse=True)
    # print("After Sort: ", rolls) # Debug Print
    bestThree = 0
    for i in range(3):
        bestThree += rolls[i]
    #print(bestThree) # Debug Print
    statBlock[stat] = bestThree
statBlock.sort(reverse=True)
print("Crypto generated stats: ", statBlock)

# TODO:
# Reroll Threshhold
# Generate Multiple Statblocks