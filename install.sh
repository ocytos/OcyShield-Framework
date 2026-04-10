#!/bin/bash
RED='\033[0;31m'
NC='\033[0m'
echo -e "${RED}[*] Configurando OcyShield como comando global...${NC}"
DIR_ACTUAL=$(pwd)
# Creamos el lanzador en /usr/local/bin
echo -e "#!/bin/bash\ncd $DIR_ACTUAL && python3 main.py \"\$@\"" | sudo tee /usr/local/bin/ocysh > /dev/null
sudo chmod +x /usr/local/bin/ocysh
chmod +x main.py
echo -e "${RED}[+] LISTO! Ahora puedes usar 'ocysh' en cualquier terminal.${NC}"
