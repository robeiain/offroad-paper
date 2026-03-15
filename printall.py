#!/usr/bin/env python3
# 
# $Id$
#
# Takes a CSV file with the following values and converts it to wristbands and printed disclaimers.  
# CSV file needs the following fields:
#       field_names = ["carnumber", "surname", "firstname", "address", "license", "expiry"]
#
#
# These are then saved to a PDF, one to a band, with car number -> firstname lastname and a separate PDF containing all the disclaimers.
#
# uses https://py-pdf.github.io/fpdf2/ for generation.
#
# to run:
# env python3 printall.py input.csv type
# where input.csv is formatted equivalent to the above and type is the type of wristband (eg Driver, Navi, Pitcrew, etc)
#
import sys
from wristbands import wristbands
from competitordisclaimer import competitordisclaimer

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.stderr.write("Error: incorrect usage\n")
        sys.stderr.write("Usage: " + sys.argv[0] + " input.csv type")
        exit(1)

    wristbands(sys.argv[1], sys.argv[2] + "wristbands.pdf", sys.argv[2].upper())
    competitordisclaimer(sys.argv[1], sys.argv[2] + "disclaimers.pdf", sys.argv[2].upper())
    exit(0)
else:
    raise ImportError("This file is not designed to be imported.")

