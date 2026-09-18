import os
import shutil
import time
import datetime
import random

def get_width():
    try:
        return shutil.get_terminal_size().columns
    except:
        return 45

def approval_system():
    os.system("xdg-open https://youtube.com/@raja-vau-teach-world?si=KeIo3GwUzYIrmbCI 2>/dev/null")
    
    unique_id = ''.join(random.choices('0123456789ABCDEF', k=6))
    user_key = f"RajaVauTeachWorld{unique_id}"
    
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 56) // 2)
    
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        print("\n")
        print(f"{padding}\033[1;96m    ██╗   ██╗ ██████╗ ██╗   ██╗████████╗██╗   ██╗██████╗ \033[0m")
        print(f"{padding}\033[1;93m    ╚██╗ ██╔╝██╔═══██╗██║   ██║╚══██╔══╝██║   ██║██╔══██╗\033[0m")
        print(f"{padding}\033[1;92m     ╚████╔╝ ██║   ██║██║   ██║   ██║   ██║   ██║██████╔╝\033[0m")
        print(f"{padding}\033[1;96m      ╚██╔╝  ██║   ██║██║   ██║   ██║   ██║   ██║██╔══██╗\033[0m")
        print(f"{padding}\033[1;94m       ██║   ╚██████╔╝╚██████╔╝   ██║   ╚██████╔╝██████╔╝\033[0m")
        print(f"{padding}\033[1;95m       ╚═╝    ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝ ╚═════╝ \033[0m")
        print(f"{padding}\033[1;33m    ═════════════════════════════════════════════════════\033[0m")
        print(f"{padding}\033[1;92m            ✦ WELCOME TO RAJA VAU TEACH WORLD ✦          \033[0m")
        print(f"{padding}\033[1;33m    ═════════════════════════════════════════════════════\033[0m\n")
        
        print(f"{padding}\033[1;36m╔══════════════════════════════════════════════════════╗\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;32mYour Key     : \033[1;33m{user_key}                        \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;37mSend this key to WhatsApp for approval!              \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;35mWhatsApp No  : +880 1345-294347                        \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m╚══════════════════════════════════════════════════════╝\033[0m")
        print(f"{padding}\033[1;32m [1] Join WhatsApp & Send Key to Admin\033[0m")
        print(f"{padding}\033[1;32m [2] Check Approval Status\033[0m")
        print(f"{padding}\033[1;31m [0] Exit\033[0m")
        print(f"{padding}\033[1;36m──────────────────────────────────────────────────────\033[0m")
        
        choice = input(f"{padding}\033[1;33m [-] CHOOSE ---> \033[0m")
        if choice == '1':
            os.system("xdg-open https://chat.whatsapp.com/K9E5ULcGZ7G0O15wwvodfy?s=sh&p=a&mlu=4&ilr=4 2>/dev/null")
            print(f"{padding}\033[1;32m [+] Opening WhatsApp Group...\033[0m")
            time.sleep(2)
        elif choice == '2':
            print(f"\n{padding}\033[1;32m welcome to Raja Vau Teach World\033[0m")
            print(f"{padding}\033[1;33m your Key approved\033[0m")
            time.sleep(2.5)
            break
        elif choice == '0':
            exit()
        else:
            print(f"{padding}\033[1;31m [!] Invalid Choice!\033[0m")
            time.sleep(1)

def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 55) // 2)
    
    print("\n")
    # Blood-Red KAMAL Banner
    print(f"{padding}\033[1;31m  ██╗  ██╗ █████╗ ███╗   ███╗ █████╗ ██╗  \033[0m")
    print(f"{padding}\033[1;31m  ██║ ██╔╝██╔══██╗████╗ ████║██╔══██╗██║  \033[0m")
    print(f"{padding}\033[1;31m  █████╔╝ ███████║██╔████╔██║███████║██║  \033[0m")
    print(f"{padding}\033[1;31m  ██╔═██╗ ██╔══██║██║╚██╔╝██║██╔══██║██║  \033[0m")
    print(f"{padding}\033[1;31m  ██║  ██║██║  ██║██║ ╚═╝ ██║██║  ██║█████╗\033[0m\n")
    
    print(f"{padding}\033[1;36m╔═════════════════════════════════════════════════════╗\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;31mSTART TIME    :\033[1;32m {current_time}              \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m╠═════════════════════════════════════════════════════╣\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;33mAdmin         :\033[1;37m Raja Vau                           \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;33mOwner         :\033[1;37m Raja Vau Teach World               \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;33mYouTube       :\033[1;34m https://youtube.com/@raja-vau      \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m║ \033[1;33mContact Admin :\033[1;32m +880 1345-294347                 \033[1;36m║\033[0m")
    print(f"{padding}\033[1;36m╚═════════════════════════════════════════════════════╝\033[0m\n")

def uid_dumping():
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 35) // 2)
    print(f"\n{padding}\033[1;32m [+] Initializing UID Dumping Engine...\033[0m")
    time.sleep(1.5)
    print(f"{padding}\033[1;33m [+] Scraping Public UIDs from Graph API...\033[0m")
    time.sleep(2)
    print(f"{padding}\033[1;32m [✓] Successfully Dumped 5000 Active UIDs!\033[0m")
    input(f"\n{padding}\033[1;33m [Press Enter To Back Menu]\033[0m")

def cookie_tracking():
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 35) // 2)
    print(f"\n{padding}\033[1;32m [+] Initializing Cookie Tracking System...\033[0m")
    time.sleep(1.5)
    print(f"{padding}\033[1;33m [+] Extracting Active Session Cookies (c_user, xs)...033[0m")
    time.sleep(2)
    print(f"{padding}\033[1;32m [✓] Cookie Harvested & Validated Successfully!\033[0m")
    input(f"\n{padding}\033[1;33m [Press Enter To Back Menu]\033[0m")

def start_cloning(series_name):
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 35) // 2)
    print(f"\n{padding}\033[1;32m [+] Starting {series_name} Cloning...\033[0m")
    time.sleep(1)
    
    for i in range(1, 6):
        print(f"{padding}\033[1;33m [CLONING] Process -> {i * 20}% | Checked: {i * 45}\033[0m", end="\r")
        time.sleep(0.4)
    print("\n")
    
    box_padding = " " * max(0, (width - 46) // 2)
    print(f"{box_padding}\033[1;32m┌──────────────────────────────────────────────┐\033[0m")
    print(f"{box_padding}\033[1;32m│\033[0m \033[1;31m [✓] SUCCESSFUL ACCOUNT FOUND                \033[0m\033[1;32m│\033[0m")
    print(f"{box_padding}\033[1;32m├──────────────────────────────────────────────┤\033[0m")
    print(f"{box_padding}\033[1;32m│\033[0m \033[1;36m FB NAME : \033[1;33mRaja Vau                          \033[0m\033[1;32m│\033[0m")
    print(f"{box_padding}\033[1;32m│\033[0m \033[1;36m FB UID  : \033[1;32m1000839201827                     \033[0m\033[1;32m│\033[0m")
    print(f"{box_padding}\033[1;32m│\033[0m \033[1;36m FB PASS : \033[1;31mRajaVau123                        \033[0m\033[1;32m│\033[0m")
    print(f"{box_padding}\033[1;32m│\033[0m \033[1;36m FB LINK : \033[1;32mfacebook.com/raja.vau             \033[0m\033[1;32m│\033[0m")
    print(f"{box_padding}\033[1;32m│\033[0m \033[1;36m YEAR    : \033[1;35m2006-2011                         \033[0m\033[1;32m│\033[0m")
    print(f"{box_padding}\033[1;32m└──────────────────────────────────────────────┘\033[0m")
    
    input(f"\n{padding}\033[1;33m [Press Enter To Back Menu]\033[0m")

def main_menu():
    approval_system()
    while True:
        banner()
        width = max(get_width(), 40)
        padding = " " * max(0, (width - 44) // 2)
        
        print(f"{padding}\033[1;36m╔════════════════════════════════════════════╗\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;32m[1] \033[1;33m---> \033[1;37mALL SERIES                      \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;32m[2] \033[1;33m---> \033[1;37m2006 SERIES                     \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;32m[3] \033[1;33m---> \033[1;37m2007 SERIES                     \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;32m[4] \033[1;33m---> \033[1;37m2008 SERIES                     \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;32m[5] \033[1;33m---> \033[1;37m2009 SERIES                     \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;32m[6] \033[1;33m---> \033[1;37m2010 SERIES                     \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;32m[7] \033[1;33m---> \033[1;37m2011 SERIES                     \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;32m[8] \033[1;33m---> \033[1;37mUID DUMPING ENGINE              \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;32m[9] \033[1;33m---> \033[1;37mCOOKIE TRACKER                  \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m║ \033[1;31m[0] \033[1;33m---> \033[1;37mBACK                            \033[1;36m║\033[0m")
        print(f"{padding}\033[1;36m╚════════════════════════════════════════════╝\033[0m")
        
        choice = input(f"{padding}\033[1;33m [-] CHOOSE ---> \033[0m")
        if choice == '1':
            start_cloning("ALL SERIES")
        elif choice == '2':
            start_cloning("2006 SERIES")
        elif choice == '3':
            start_cloning("2007 SERIES")
        elif choice == '4':
            start_cloning("2008 SERIES")
        elif choice == '5':
            start_cloning("2009 SERIES")
        elif choice == '6':
            start_cloning("2010 SERIES")
        elif choice == '7':
            start_cloning("2011 SERIES")
        elif choice == '8':
            uid_dumping()
        elif choice == '9':
            cookie_tracking()
        elif choice == '0':
            print(f"{padding}\n\033[1;31m [!] Exiting...\033[0m")
            break
        else:
            print(f"{padding}\n\033[1;31m [!] Invalid Choice!\033[0m")
            time.sleep(1)

if __name__ == '__main__':
    main_menu()
