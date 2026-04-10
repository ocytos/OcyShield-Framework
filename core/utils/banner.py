import os

def show_ocy_banner():
    # ANSI escape codes for intense colors
    RED = '\033[1;31m'
    RESET = '\033[0m'
    
    # Optional screen clear for professional impact
    if os.name != 'nt':
        os.system('clear')

    # The New, Respectful, Aggrressive Logo
    banner_art = f"""{RED}
        .x000k:.                     .:k000x.
       c00Oxc,      __________       ,cxO00c
      d00x'      __/ _ __ _  _\\__      'x00d
     x00d       / O C Y S H I E L D \\      d00x
    x00d       /____ ____ ____ ____/       d00x
   x00d       //  _// _ // _ //  _//        d00x
   00O       //  / // / // / //  /          O00
   00O      ||  ( || ( || ( ||  (           O00
   00O       \\\\_ \\\\_ \\\\_ \\\\_ \\\\_            O00
   x00d       \\____\\____\\____\\____\\        d00x
    x00d                                  d00x
     x00d      [ G I T H U B . C O M / O C Y T O S ]
      d00x'                              'x00d
       c00Oxc,                          ,cxO00c
        'cx000k:.                    .:k000x'
    """
    
    # Reducimos los print() para un código más limpio
    print(banner_art)
    print(f"[{RED}+{RESET}] OcyShield Framework | v2.0 \"Viper\"")
    print(f"[{RED}+{RESET}] Educational Exploitation & Automation Suite")
    print("-" * 60)
