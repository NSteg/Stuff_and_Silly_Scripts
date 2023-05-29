#!/usr/bin/python
# Python 3.9+
###############################################################################
## A script for naming random, throw-away Taverns,
#   for use in TTRPGs and other purposes.
###############################################################################
## Provided as is. Distributable and extensible under GNU gpl 3.0
###############################################################################
## Author: Nicholas Stegelman
# Created: 2021-09-02
# Version: 1.0.0


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

## Ver.1.0.0

## Maintainers: Nicholas Stegelman
# Last Updated: 2021-09-02

## Status: Needing Improvement
###############################################################################

## System Imports
import string
import secrets
import os

## Python Heresy
def main():
    adjectives = []
    nouns = []
    nNouns = 0
    nAdjectives = 0
    
    ## Alternate Method(?)    
    # cur_path = os.path.dirname(__file__)
    # nounFile = os.path.relpath("..\\TextFiles\\nouns.txt", cur_path)
    # adjectiveFile = os.path.relpath("..\\TextFiles\\adjectives.txt",
        # cur_path)
    # with open(new_path, 'w') as f:
    #     # f.write(data)

    nounFile = "TextFiles/nouns.txt"
    adjectiveFile = "TextFiles/adjectives.txt"
    nounObject = open(nounFile, 'r')
    adjectiveObject = open(adjectiveFile, 'r')

    # Read in nouns
    for line in nounObject:
        nouns.append(line.rstrip())
    nNouns = len(nouns)
    # Read in adjectives
    for line in adjectiveObject:
        adjectives.append(line.rstrip())
    nAdjectives = len(adjectives)

    # Close Files before exit
    nounObject.close()
    adjectiveObject.close()

    while True:
        arg = input("<ENTER> For Next Tavern Name or <Q> to exit: ")
        if arg == '':
            pass
        elif arg[0].capitalize() == 'Q':
            quit()
        for i in range(10):
            print("\n|*****The", secrets.choice(adjectives).capitalize(),
                sep=' ', end=" ")
            print(secrets.choice(nouns).capitalize(), "*****|\n",
                sep='', end='\n')
## End of MAIN()

# Complete Blasphemy
if __name__ == "__main__":
    main() 

# TODO:
# 1)
#   Clean up nouns.txt and cull options that are thematically wrong
#   or just don't make sense.
# 2)
#   Add the requisite GNU GPL print outs and options. If you're going to use
#   it, don't half ass it.
# 3)
#   Add an option to generate a set number of names and another
#   flag to print-to-file on user desktop/workspace 
#   [rand8-TavernNames-ISO8601.txt]