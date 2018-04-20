sleep 2
/usr/bin/python /home/pi/modem/getinfos.py > /tmp/modem.ini
sleep 2
/usr/bin/wvdial `python /home/pi/modem/getimsi.py -carrier` &
