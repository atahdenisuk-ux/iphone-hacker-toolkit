# iPhone Hacker Toolkit - Built on iSH
# Author: Dennywise
# For educational use only - test on scanme.nmap.org only

import socket
import hashlib

def port_scanner(target):
    print(f"[+] Scanning {target}")
    for port in [22, 
