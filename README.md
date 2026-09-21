# iPhone Hacker Toolkit - Built on iSH

I built a full penetration testing toolkit that runs entirely on iPhone using iSH (Alpine Linux). No laptop needed.

### Tools Included
- **Port Scanner** - TCP scan for open services (Found 22 OPEN ssh, 80 OPEN http on scanme.nmap.org)
- **Directory Brute** - Finds hidden endpoints (/admin, /login)
- **Hash Cracker** - MD5 dictionary attack (Cracked: hello)

### Proof (Real Terminal Output)
Target: scanme.nmap.org (45.33.32.156)
22 OPEN - ssh
80 OPEN - http
/ 200 OK
Cracked: hello

### Tech Stack
Python3, socket, hashlib - No root, no jailbreak

### Ethical Use Only
This tool is for educational purposes and authorized testing only (scanme.nmap.org).

Built by Dennywise - 2026
Certified: iPhone Hacker Toolkit Level III
