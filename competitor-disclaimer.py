#!/usr/bin/env python3
# 
# $Id$
#
# Takes a CSV file with the following values and converts it to pre-filled disclaimers & the sign on sheet.  
# CSV format:
# car_number, surname, firstname, address, license_number, expiry_date
# These are then saved to a PDF, one to a band, with car number -> firstname lastname 
# Typeface is Helvetica, font size is 28 points.
# uses https://py-pdf.github.io/fpdf2/ for generation.
# 
# to run:
# env python3 competitor-disclaimer.py input.csv output.pdf type
# where input.csv is formatted equivalent to the above; output.pdf is self explanatory; and type is the type of competitor (eg Driver, Navi, Pitcrew, etc)
#
from fpdf import FPDF
import sys
import csv 

def competitor_disclaimer(csv_file, output_file, disclaimer_type, disclaimer_heading ="", disclaimer_subheading = "", disclaimer_warning = "", disclaimer = ""):
    pdf = FPDF(orientation="landscape", format="A4")
    pdf.set_margin(10)
    pdf.set_font("helvetica", size=12)

    if disclaimer_heading == "":
        disclaimer_heading = "RELEASE AND WAIVER OF LIABILITY"
    if disclaimer_subheading == "":
        disclaimer_subheading = "ASSUMPTION OF RISK AND INDEMNITY AGREEMENT (Queensland)"
    if disclaimer_warning == "":
        disclaimer_warning = "\nWARNING!  \t  MOTOR RACING IS DANGEROUS\n\nAccidents can and do happen.\nAll care is taken to protect you, but you are warned that there is a possibility of an accident causing personal injury or death."
    if disclaimer == "":
        disclaimer = """
Subject to that warranty, if applicable and IN CONSIDERATION of being permitted to compete, officiate, observe, work for, or participate in any way in the EVENT(S) or being permitted to enter for any purpose any RESTRICTED AREA (defined as any area requiring special authorisation, credentials, or permission to enter any area to which admission by the general public is restricted or prohibited), EACH OF THE UNDERSIGNED, for himself/herself, his/her personal representatives, heirs and next of kin.
1. Acknowledges, agrees and represents that he/she enters and he/she further agrees and warrants that, if at any time, he/she is in or about RESTRICTED AREAS and he/she feels anything to be unsafe, he/she will immediately advise the officials of such and will leave the RESTRICTED AREAS and/or refuse to participate further in the EVENT(S).
2. HEREBY RELEASES, WAIVES, DISCHARGES AND COVENANTS NOT TO SUE Australian Auto-Sport Alliance Pty. Ltd., the Organisers, the landowners, promoters, participants, racing associations, sanctioning organisations or any subdivision thereof, track operators, officials, car owners, drivers, pit crews, rescue personnel, any persons in any RESTRICTED AREA, promoters, sponsors, advertisers, owners and lessees of premises used to conduct the EVENT(S), premises and Event inspectors, surveyors, underwriters, consultants and others who give recommendations, directions or instructions or engage in risk evaluation or loss control activities regarding the premises or EVENT(S) and each of them, their directors, officers, agents and employees, all for the purposes as herein referred to as "Releases", FROM ALL LIABILITY, TO THE UNDERSIGNED, his/her personal ON ACCOUNT OF INJURY TO THE PERSON OR RESULTING IN DEATH OF THE UNDERSIGNED ARISING OUT OR RELATED TO THE EVENT(S), WHETHER CAUSED BY THE NEGLIGENCE OF THE RELEASEES OR OTHERWISE.
3. HEREBY ASSUMES FULL RESPONSIBILITY FOR ANY RISK OF PERSONAL INJURY or DEATH arising out of or related to the EVENT(S) whether caused by the NEGLIGENCE OF RELEASEES or otherwise.
4. HEREBY acknowledges that THE ACTIVITIES OF THE EVENT(S) ARE VERY DANGEROUS and involve the risk of personal injury and/or death Each of the UNDERSIGNED also expressly acknowledges that INJURIES RECEIVED MAY BE COMPOUNDED OR INCREASED BY NEGLIGENT RESCUE OPERATIONS OR PROCEDURES OF THE RELEASEES.
5. Hereby assumes full responsibility for the preparation and safety of the vehicle to be used and further give an assurance that the vehicle has been checked for safety and is in a condition fit to be used for motor racing.
6. Hereby agrees that this Release and Waiver of Liability, Assumption of risk and Indemnity Agreement extends to all acts of negligence by the Releases, INCLUDING NEGLIGENT RESCUE OPERATIONS and is intended to be as broad and inclusive as is permitted by the Fair Trading Act 2012 (Vic) and the Australian Consumer Law and that if any portion thereof is held invalid, it is agreed that the balance shall, notwithstanding, continue in full legal force and effect.

**COMMUNICABLE DISEASE EXCLUSION**

1. Notwithstanding any provision to the contrary within this policy, this policy does not cover all actual or alleged loss, liability, damage, compensation, injury, sickness, disease, death, medical payment, defence cost, cost, expense or any other amount, directly or indirectly and regardless of any other cause contributing concurrently or in any sequence, originating from, caused by, arising out of, contributed to by, resulting from, or otherwise in connection with a Communicable Disease or the fear or threat (whether actual or perceived) of a Communicable Disease.
2. For the purposes of this endorsement, loss, liability, damage, compensation, injury, sickness, disease, death, medical payment, defence cost, cost, expense or any other amount, includes, but is not limited to, any cost to clean-up, detoxify, remove, monitor or test for a Communicable Disease.
3. As used herein, a Communicable Disease means any disease which can be transmitted by means of any substance or agent from any organism to another organism where:
3.1. the substance or agent includes, but is not limited to, a virus, bacterium, parasite or other organism or any variation thereof, whether deemed living or not, and
3.2. the method of transmission, whether direct or indirect, includes but is not limited to, airborne transmission, bodily fluid transmission, transmission from or to any surface or object, solid, liquid or gas or between organisms, and
3.3. the disease, substance or agent can cause or threaten bodily injury, illness, emotional distress, damage to human health, human welfare or property damage.
"""

    with open(csv_file, newline='') as csvfile:
        # car_number, surname, firstname, address, license_number, expiry_date
        field_names = ["carnumber", "surname", "firstname", "address", "license", "expiry"]
        entries = csv.DictReader(csvfile, fieldnames=field_names)
        for row in entries:
            pdf.add_page()
            license_number = row["license"]
            expiry_date = row["expiry"]
            firstname = row["firstname"]
            surname = row["surname"]
            address = row["address"]
            car_number = row["carnumber"]

            pdf.set_font("helvetica", size=8, style="B")
            pdf.cell(w=277, text=disclaimer_type + " " + car_number + " " + surname.upper(), align="C", new_x="LMARGIN", new_y="NEXT")
            pdf.image("./AORRA.png", y=5, w=71, h=32)
            pdf.image("./AASA.png", x=202, y=5, w=85, h=32)
            pdf.cell(w=277, h=22, new_x="LMARGIN", new_y="NEXT")
            pdf.set_font("helvetica", size=12, style="B")
            pdf.multi_cell(w=277, text=disclaimer_heading, align="C", new_x="LMARGIN", new_y="NEXT")
            pdf.set_font("helvetica", size=10, style="B")
            pdf.cell(w=277, h=3, align="C", new_x="LMARGIN", new_y="NEXT")
            pdf.multi_cell(w=277, text=disclaimer_subheading, align="C", new_x="LMARGIN", new_y="NEXT")
            pdf.set_font("helvetica", size=10, style="B")
            pdf.cell(w=277, h=3, align="C", new_x="LMARGIN", new_y="NEXT")
            pdf.multi_cell(w=277, text=disclaimer_warning, align="C", new_x="LMARGIN", new_y="NEXT")
            pdf.set_font("helvetica", size=6, style="")
            pdf.cell(w=277, h=3, align="C", new_x="LMARGIN", new_y="NEXT")
            pdf.multi_cell(w=277, text=disclaimer, align="L", new_x="LMARGIN", new_y="NEXT", markdown=True)
            pdf.cell(w=277, h=10, align="C", new_x="LMARGIN", new_y="NEXT")

            pdf.set_font("helvetica", size=12, style="")
            driver_disclaimer = "License Number:\t**" + license_number + "** License Expiry Date: **" + expiry_date + "**\n\nI, **" + firstname + " " + surname + "** of address **" + address + "**\nhave read this Release and Waiver of Liability, assumption of risk and Indemnity Agreement, fully understand its terms, understand that I have given up substantial rights by signing it, and hve signed it freely and voluntarily without any inducement, assurance or guarantee made to me and intend my signature to be a complete and unconditional release of all liability to the greatest extent allowed by law."
            pdf.multi_cell(w=277, h=6, text=driver_disclaimer, align="L", new_x="LMARGIN", new_y="NEXT", markdown=True)
            pdf.cell(w=277, h=10, new_x="LMARGIN", new_y="NEXT")
            pdf.cell(w=139, h=12, text="___________________________________________")
            pdf.cell(w=138, h=12, text="___________________________________________", new_x="LMARGIN", new_y="NEXT")
            pdf.cell(w=139, text="(Signature)")
            pdf.cell(w=138, text="(Date)", new_x="LMARGIN", new_y="NEXT")

    pdf.output(output_file)
    return(0)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.stderr.write("Error: incorrect usage\n")
        sys.stderr.write("Usage: " + sys.argv[0] + " input.csv output.pdf type")
        exit(1)

    competitor_disclaimer(sys.argv[1], sys.argv[2], sys.argv[3].upper())

    exit(0)