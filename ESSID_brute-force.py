#!/bin/python
from colorama import Fore , Style
from scapy.all import *
import os
n = raw_input ( "\nchannel = " + Fore.YELLOW + Style.BRIGHT )
x = int ( raw_input ( Style.RESET_ALL + "count = " + Fore.YELLOW + Style.BRIGHT ) )
y = raw_input ( Style.RESET_ALL + "dictionary = " + Fore.YELLOW + Style.BRIGHT )
z = raw_input ( Style.RESET_ALL + "iface = " + Fore.YELLOW + Style.BRIGHT )
client_BSSID = "aa:aa:aa:aa:aa:aa"
broadcast_MAC = "ff:ff:ff:ff:ff:ff"
os.system ( 'iwconfig ' + z + ' channel ' + n )
for ESSID in open ( y , 'r' ).readlines ( ) :
    packet = RadioTap ( ) / Dot11 ( type = 0 , subtype = 4 , addr1 = broadcast_MAC , addr2 = client_BSSID , addr3 = broadcast_MAC ) / Dot11ProbeReq ( ) / Dot11Elt ( ID = 0 , info = ESSID.strip ( ) ) / Dot11Elt ( ID = 1 , info = "\x02\x04\x0b\x16" ) / Dot11Elt ( ID = 3 , info = "\x08" )
    print Fore.BLUE + Style.BRIGHT + "[*] " + Style.RESET_ALL + "Trying the following entry in the " + Fore.YELLOW + Style.BRIGHT + y + Style.RESET_ALL + " dictionary: " + Fore.YELLOW + Style.BRIGHT + ESSID + Style.RESET_ALL
    sendp ( packet , count = x , iface = z , inter = .256 , verbose = 0 )
