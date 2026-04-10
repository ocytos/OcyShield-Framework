import subprocess
import os
from core.utils.logger import log_status, log_error

class APKSigner:
    @staticmethod
    def sign(apk_path):
        if not os.path.exists(apk_path):
            log_error(f"Target APK not found for signing: {apk_path}")
            return False

        keystore = "config/ocy_vault.keystore"
        alias = "ocy_alias"
        passw = "ocyshield123"

        try:
            if not os.path.exists(keystore):
                log_status("Generating new keystore vault...")
                gen_cmd = [
                    "keytool", "-genkey", "-v", "-keystore", keystore,
                    "-alias", alias, "-keyalg", "RSA", "-keysize", "2048",
                    "-validity", "10000", "-storepass", passw, "-keypass", passw,
                    "-dname", "CN=Ocy, OU=Shield, O=Elite, L=Cartago, S=CR, C=CR"
                ]
                subprocess.run(gen_cmd, capture_output=True)

            log_status(f"Signing APK: {apk_path}")
            sign_cmd = [
                "jarsigner", "-verbose", "-sigalg", "SHA1withRSA",
                "-digestalg", "SHA1", "-keystore", keystore,
                "-storepass", passw, apk_path, alias
            ]
            
            result = subprocess.run(sign_cmd, capture_output=True, text=True)
            if result.returncode == 0:
                log_status("APK successfully signed and hardened.")
                return True
            else:
                log_error(f"Signing failure: {result.stderr}")
                return False

        except Exception as e:
            log_error(f"Signer exception: {str(e)}")
            return False
