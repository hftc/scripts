#!/bin/python
from colorama import Fore , Style
from scapy.all import *
import os
x = raw_input ( "\nchannel = " + Fore.YELLOW + Style.BRIGHT )
y = raw_input ( Style.RESET_ALL + "count = " + Fore.YELLOW + Style.BRIGHT )
z = raw_input ( Style.RESET_ALL + "iface = " + Fore.YELLOW + Style.BRIGHT )
os.system ( 'iwconfig ' + z + ' channel ' + x )
print ''
def packet_handler ( packet ) :
    if packet.haslayer ( Dot11Beacon ) :
        if not packet.info :
            if packet.addr3 not in APs_with_hidden_SSIDs :
                APs_with_hidden_SSIDs.add ( packet.addr3 )
                print Fore.RED + Style.BRIGHT + "[-] " + Style.RESET_ALL + "The ESSID of the access point " + Fore.YELLOW + Style.BRIGHT + packet.addr3 + Style.RESET_ALL + " is hidden." + Style.RESET_ALL
    elif packet.haslayer ( Dot11ProbeResp ) and ( packet.addr3 in APs_with_hidden_SSIDs ) :
        print Fore.GREEN + Style.BRIGHT + "[+] " + Style.RESET_ALL + "The decloaked ESSID of the access point " + Fore.YELLOW + Style.BRIGHT + packet.addr3 + Style.RESET_ALL + " is " + Fore.GREEN + Style.BRIGHT + packet.info + Style.RESET_ALL + "."
while True :
    try :
        APs_with_hidden_SSIDs = set ( )
        sniff ( count = y , iface = z , prn = packet_handler )
    except :
        continue
