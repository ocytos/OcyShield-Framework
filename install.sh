#!/bin/bash

# --- Colors ---
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}[*] OcyShield Framework - Installing...${NC}"

# 1. Check for root privileges
if [ "$EUID" -ne 0 ]; then
  echo -e "${RED}[!] Please run as root (use sudo)${NC}"
  exit
fi

# 2. Cleanup old installations
if [ -d "/opt/ocyshield" ]; then
    echo -e "${BLUE}[*] Removing previous version...${NC}"
    rm -rf /opt/ocyshield
fi

# 3. Clone repository
echo -e "${BLUE}[*] Cloning repository to /opt/ocyshield...${NC}"
git clone https://github.com/ocytos/OcyShield-Framework.git /opt/ocyshield

# 4. Install dependencies (PEP 668 Bypass for Kali)
echo -e "${BLUE}[*] Installing dependencies...${NC}"
if [ -f "/opt/ocyshield/requirements.txt" ]; then
    pip3 install -r /opt/ocyshield/requirements.txt --break-system-packages --quiet
fi

# 5. Fix permissions (To avoid Error: Permission denied logs)
echo -e "${BLUE}[*] Setting up permissions...${NC}"
chmod -R 777 /opt/ocyshield

# 6. Create global command
echo -e "${BLUE}[*] Creating global command 'ocysh'...${NC}"
echo -e "#!/bin/bash\npython3 /opt/ocyshield/main.py \"\$@\"" > /usr/local/bin/ocysh
chmod +x /usr/local/bin/ocysh

echo -e "${GREEN}[+] Installation finished! Type 'ocysh' to start.${NC}"
