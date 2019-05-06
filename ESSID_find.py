#!/bin/python
from colorama import Fore , Style
from scapy.all import *
import os
k = raw_input ( "\nchannel = " + Fore.YELLOW + Style.BRIGHT )
m = raw_input ( Style.RESET_ALL + "count = " + Fore.YELLOW + Style.BRIGHT )
n = raw_input ( Style.RESET_ALL + "iface = " + Fore.YELLOW + Style.BRIGHT )
def packet_handler ( packet ) :
    if packet.haslayer ( Dot11Beacon ) :
        x = packet
        while x :
            x = x.getlayer ( Dot11Elt )
            if x and x.ID == 0 and ( x.info not in ESSIDs ) :
                ESSIDs.add ( x.info )
                print Fore.BLUE + Style.BRIGHT + "\t[*] " + Style.RESET_ALL + "The access point " + Fore.YELLOW + Style.BRIGHT + packet.addr3 + Style.RESET_ALL + " is a node on the " + Fore.YELLOW + Style.BRIGHT + x.info + Style.RESET_ALL + " WLAN."
                break
            if x == None :
                pass
            else :
                x = x.payload
ESSIDs = set ( )
os.system ( 'iwconfig ' + n + ' channel ' + k )
print Fore.BLUE + Style.BRIGHT + "\n[*] " + Style.RESET_ALL + "On channel " + Fore.YELLOW + Style.BRIGHT + str ( k ) + Style.RESET_ALL + ", the following access points and ESSIDs were detected:\n"
sniff ( count = m , iface = n , prn = packet_handler )
