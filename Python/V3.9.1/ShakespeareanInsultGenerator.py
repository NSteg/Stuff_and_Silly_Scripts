#!/usr/bin/python
# Python 3.9+
###############################################################################
## An upgraded version of the common Prime number finding introductory 
# programming assignment.
###############################################################################
## Provided as is. Distributable and extensible under GNU gpl 3.0
###############################################################################
## Author: Nicholas Stegelman
# Created: 2022-02-26
# Version: 0.1


## Copyright: Copyright (C) 2022, profileXX

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
# Last Updated: 2022-02-26

## Status: In Development
###############################################################################

## System Imports
import string
import secrets
import codecs

parts = [0, 0, 0]

part1 = []
part2 = []
part3 = []

s1Object = open("TextFiles/Shakes1.txt", mode='r', encoding="UTF-8")
s2Object = open("TextFiles/Shakes2.txt", mode='r', encoding="UTF-8")
s3Object = open("TextFiles/Shakes3.txt", mode='r', encoding="UTF-8")

for line in s1Object:
    part1.append(line.rstrip())

for line in s2Object:
    part2.append(line.rstrip())

for line in s3Object:
    part3.append(line.rstrip())

s1Object.close()
s2Object.close()
s3Object.close()

while (True):

    arg = input("<ENTER> For Next Insult or <Q> to exit: ")
    if arg == '':
        pass
    elif arg[0].capitalize() == 'Q':
        quit()

    for i in range(0,3):
       parts[i] = secrets.randbits(64) % 50

    print("Thou art a", part1[parts[0]], part2[parts[1]], part3[parts[2]], '\n')

