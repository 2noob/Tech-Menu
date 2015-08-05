#!/usr/local/bin/python -w
###############################################################################
# tech_menu:	On-Site Technician Menu for Optical Retail SOE
#
#               This script is launched when the tech user account logs in on
#		Retail Hypervisor
###############################################################################
# Author:       Timothy Stramyk
# Created:      26 Jun 2015
###############################################################################
# Changelog:
#
# 1st  July 2015 H.L     Helped to add comments in and reformatting
# 26th June 2015 T.S     Initial version for Tech Menu
###############################################################################
import os
#looping menu now working until input for "q"
# maybe the "elif"  could work here?
#tried   if selection == 'q' or 'Q' or '3':  but this didnt run correctly.

selection = "ABC"
while ( selection != "q") :
    os.system('clear')
    #need to work out how to make sure this is case sensitive... 
    print("#####Luxottica Retail######################################")
    print("##                    - TECH MENU -                      ##")
    print("###########################################################") 
    print("\n\n\n")
    print("1.    Hardware Configuration Menu")
    print("2.    Linux Command Line")
    print("\n")
    print("q.    Quit")
    print("\n\n")
    selection = raw_input("Enter Selection ( q = quit/logout) :")

#Still trying to make the menu clear during incorrect inputs so its clean for page refresh
# Will need to incorperate - str()/len()/.upper()/.lower(). This should help me with tidying up the code.

# need to work out how to link the selections to the actual inputs
#grabbed the below menu code from (/usr/local/share/lrapsoe/bin/deviceconfig) to get a better
#understanding of the menus used by Hao/Speedy
#the below grab, may be totally useless... leaving here for now.

#Config_menu
#            BANNER "LRAP Retail SOE Configuration System"
#                echo "1)  Server Name and IP Address (${STORENAME} ${SERVERIP})"
#                echo "2)  Brand Name (${BRAND})"
#                echo "3)  Wireless Access Points (${WAP} defined)"
#                echo "4)  Point Of Sale Terminals (${TCS} defined)"
#                echo "5)  Non-POS Workstations (${WSTS} defined)"
#                echo "6)  Printers (${PRS} defined)"
#               echo "7)  Cashdrawers (${CASHD} defined)"
#                echo "8)  DHCP Server (${DHCPS})"
#                echo "9)  TimeZone (${STORETZ})"
#                echo "10) Set store locale (${LOCALE})"
#                echo "11) Enable Remote Terminal Mode"
#                echo "p)  Purge Printer queues"
#                echo "a)  Apply changes to the server"
#                echo "e)  Exit this program"
os.system('clear')
print("Exiting the program...")
exit(0)
