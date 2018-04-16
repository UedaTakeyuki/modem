import re
import at

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
	return [imsi, mcc, mnc]

if __name__ == '__main__':
	print read()