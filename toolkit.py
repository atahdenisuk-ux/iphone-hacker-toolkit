#!/usr/bin/env python3
# iPhone Hacker Toolkit - Level VI MASTER
# Author: Dennywise (atahdenisuk-ux)
# Built entirely on iPhone using iSH
# For educational & ethical use only

import socket
import hashlib
import sys

def banner():
    print("""
╔════════════════════════════════════╗
║ iPhone Hacker Toolkit - VI ║
║ By Dennywise | Ethical Only ║
╚════════════════════════════════════╝
    """)

def port_scanner():
    target = input("[+] Enter target IP/domain: ").strip()
    print(f"\n[+] Scanning {target}...")
    for port in [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 8080]:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.8)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[OPEN] Port {port}")
            s.close()
        except:
            pass
    print("[*] Scan done.")

def hash_cracker():
    hash_input = input("[+] Enter MD5 hash: ").strip()
    wordlist = ["123456", "password", "admin", "letmein", "qwerty", "dennywise", "iphone", "root"]
    print("[*] Cracking with small built-in wordlist...")
    for word in wordlist:
        if hashlib.md5(word.encode()).hexdigest() == hash_input:
            print(f"[FOUND] Password is: {word}")
            return
    print("[FAILED] Not found in wordlist. Try bigger wordlist on PC.")

def dir_brute():
    target = input("[+] Enter target URL (e.g. example.com): ").strip()
    dirs = ["admin", "login", "dashboard", "api", "backup", "test", "dev", "uploads"]
    print(f"[*] Checking common paths on {target}...")
    for d in dirs:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            # simple check - we just print attempt (full HTTP needs requests lib)
            print(f" -> /{d}")
            s.close()
        except:
            pass
    print("[*] Done. Use with permission only.")

def main():
    banner()
    while True:
        print("\n[1] Port Scanner\n[2] MD5 Hash Cracker\n[3] Dir Brute (common paths)\n[4] Exit")
        choice = input("Select > ").strip()
        if choice == "1":
            port_scanner()
        elif choice == "2":
            hash_cracker()
        elif choice == "3":
            dir_brute()
        elif choice == "4":
            print("Bye - Dennywise")
            sys.exit(0)
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
