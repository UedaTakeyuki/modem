import re
import at
import imsi_table

pattern = re.compile("(([0-9][0-9][0-9])([0-9][0-9])([0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]))\r\n")

def read():
	imsi  = ""
	mcc   = ""
	mnc   = ""

	lines = at.read("AT+CIMI")

	matchOB = re.match(pattern, lines[1])

	if matchOB:
		imsi = matchOB.group(1)
		mcc  = matchOB.group(2)
		mnc  = matchOB.group(3)
	return {"imsi": imsi, "mcc": mcc, "mnc": mnc}

if __name__ == '__main__':
	result = read()
	print result
	if result["imsi"] in imsi_table.imsi_table:
		print imsi_table.imsi_table[result["imsi"]]
