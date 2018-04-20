import re
import at
import imsi_table

pattern = re.compile("(([0-9][0-9][0-9])([0-9][0-9])([0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]))\r\n")

def read():
	imsi  	= ""
	mcc   	= ""
	mnc   	= ""
	carrier = ""

	lines = at.read("AT+CIMI")

	matchOB = re.match(pattern, lines[1])

	if matchOB:
		imsi = matchOB.group(1)
		mcc  = matchOB.group(2)
		mnc  = matchOB.group(3)
		if imsi in imsi_table.imsi_table:
			carrier = imsi_table.imsi_table[imsi]["carrier"]
		elif mcc+mnc in imsi_table.mccmnc_table:
			carrier = imsi_table.mccmnc_table[mcc+mnc]["carrier"]
	return {"imsi": imsi, "mcc": mcc, "mnc": mnc, "carrier": carrier}

if __name__ == '__main__':
	result = read()
	print result
