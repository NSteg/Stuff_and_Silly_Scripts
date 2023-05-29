#!/usr/bin/python
# Python 3.9+
###############################################################################
## A script for randomly generating Alphanumeric IDs for Mobile Task Forces
# from the fictional Secure-Contain-Protect universe.
###############################################################################
## Provided as is. Distributable and extensible under GNU gpl 3.0
###############################################################################
## Author: Nicholas Stegelman
# Created: 2022-05-18


## Copyright: Copyright (C) 2021, MTFBanger

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
# Last Updated: 2022-05-18

## Version: 0.1.0

## Status: In Development
###############################################################################

## System Imports
import argparse
import secrets
import string

## Python Heresy
# I'm a C/Go programmer, and I won't apologize.
def main():
    print('') # Create space between command and output
    greek = ["ALPHA", "BETA", "GAMMA", "DELTA", "EPSILON", "ZETA", "ETA",
            "THETA", "IOTA", "KAPPA", "LAMBDA", "MU", "NU", "XI", "OMICRON",
            "PI", "RHO", "SIGMA", "TAU", "UPSILON", "PHI", "CHI", "PSI",
            "OMEGA"]
    existing = ["MTF ALPHA-1", "MTF ALPHA-4", "MTF ALPHA-9",
                "MTF BETA-4", "MTF BETA-7", "MTF BETA-777",
                "MTF GAMMA-5", "MTF GAMMA-6", "MTF GAMMA-13",
                "MTF DELTA-5", "MTF EPSILON-6", "MTF EPSILON-9",
                "MTF EPSILON-11", "MTF ZETA-9", "MTF ETA-4",
                "MTF ETA-5", "MTF ETA-10", "MTF ETA-11", "MTF ETA-77",
                "MTF THETA-4", "MTF THETA-90", "MTF IOTA-10",
                "MTF KAPPA-10", "MTF LAMBDA-4", "MTF LAMBDA-5",
                "MTF LAMBDA-12", "MTF LAMBDA-14", "MTF MU-3", "MTF MU-4",
                "MTF MU-13", "MTF OMICRON RHO", "MTF PI-1",
                "MTF RHO-1", "MTF RHO-9", "MTF RHO-19",
                "MTF SIGMA-3", "MTF SIGMA-66", "MTF TAU-5", "MTF TAU-9",
                "MTF PHI-2", "MTF PSI-7", "MTF PSI-8",
                "MTF OMEGA-0", "MTF OMEGA-7", "MTF OMEGA-12",
                "MTF STIGMA-9"] # Filter out existing units
    
    #TODO# $$$$$$$$$$ Special case for double letter $$$$$$$$$$
    # 'STIGMA' (?) - I hate breaks in convention.

    i = 0
    i2 = 20
    while i < i2:
        idLetter = greek[(secrets.randbits(64) % 24)]
        idNumber = (secrets.randbits(64) % 100) + 1
        taskForce = "MTF " + idLetter + "-" + str(idNumber)
        if taskForce in existing: 
            # print("Found:", taskForce, "at",
            # existing.index(taskForce)) # Debug Print
            continue
        else:
            print(taskForce)
        i += 1

## End of MAIN()

# Complete Blasphemy
if __name__ == "__main__":
    main() 