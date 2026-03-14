#!/usr/bin/env python3
# 
# $Id$
#
# Takes a CSV file with the following values and converts it to wristbands.  Wrist band size is 297mm by 21mm - 10 to an A4 sheet (landscape).
# car_number, surname, firstname
# These are then saved to a PDF, one to a band, with car number -> firstname lastname 
# Typeface is Helvetica, font size is 28 points.
# Laserbands are 250mm long and 20.5mm wide (10 to a sheet)
# uses https://py-pdf.github.io/fpdf2/ for generation.
# 
# to run:
# env python3 wristbands.py input.csv output.pdf type
# where input.csv is formatted equivalent to the above; output.pdf is self explanatory; and type is the type of wristband (eg Driver, Navi, Pitcrew, etc)
#
from fpdf import FPDF
import sys
import csv 

if len(sys.argv) != 4:
    sys.stderr.write("Error: incorrect usage\n")
    sys.stderr.write("Usage: " + sys.argv[0] + " input.csv output.pdf type")
    exit(1)

pdf = FPDF(format=(250, 205))
pdf.set_margin(0)
pdf.add_page()

with open(sys.argv[1], newline='') as csvfile:
    field_names = ["carnumber", "surname", "firstname"]
    entries = csv.DictReader(csvfile, fieldnames=field_names)
    for row in entries:
        height = 20.5
        pdf.set_font("helvetica", size=26, style="B")
        line = row["carnumber"] + "\t" + row["firstname"] + " " + row["surname"]
        pdf.cell(w=200, h=height, text=line.upper(), align="C")
        pdf.set_font("helvetica", size=12, style="B")
        pdf.cell(w=50, h=height, text=sys.argv[3].upper(), align="C", new_x="LMARGIN", new_y="NEXT")


pdf.output(sys.argv[2])


exit(0)