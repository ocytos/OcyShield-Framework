import os
import subprocess
import sys
from core.utils.logger import log_status, log_error

def check_and_install_dependencies():
    """
    Checks for missing system binaries and installs them automatically.
    """
    print("\n[!] OcyShield-Framework: Starting System Environment Setup...")
    
    # Required system binaries
    required_tools = {
        "jarsigner": "default-jdk",
        "zipalign": "zipalign",
        "msfvenom": "metasploit-framework"
    }
    
    missing_packages = []

    for tool, package in required_tools.items():
        check_cmd = subprocess.run(f"command -v {tool}", shell=True, capture_output=True)
        if check_cmd.returncode != 0:
            print(f"[-] Missing component: {tool}")
            missing_packages.append(package)
        else:
            print(f"[+] Component found: {tool}")

    if missing_packages:
        print(f"[*] Installing required packages: {', '.join(missing_packages)}...")
        # Concatenating all missing packages into one apt command
        install_cmd = f"sudo apt update && sudo apt install -y {' '.join(missing_packages)}"
        
        try:
            subprocess.check_call(install_cmd, shell=True)
            print("[+] System dependencies installed successfully.")
        except subprocess.CalledProcessError:
            print("[X] Critical Error: Failed to install packages automatically.")
            sys.exit(1)
    else:
        print("[+] Environment is fully compatible. No action needed.")

def install_python_requirements():
    """
    Installs Python libraries from requirements.txt
    """
    print("[*] Syncing Python requirements...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "--break-system-packages"])
        print("[+] Python libraries synced.")
    except Exception as e:
        print(f"[X] Pip sync failed: {str(e)}")

if __name__ == "__main__":
    # Ensure script is run with root privileges for apt
    if os.geteuid() != 0:
        print("[!] Warning: Root privileges required for system updates. Use 'sudo'.")
        sys.exit(1)

    check_and_install_dependencies()
    install_python_requirements()
    print("\n[#] Setup Complete. OcyShield is ready for deployment.\n")
