import colorama
from colorama import Style, Fore, Back
import requests
import socket

colorama.init()

def ip_lookup(ip_address):
    try:
        url = f"https://ipinfo.io/{ip_address}/json"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; )'}
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            return f"""
{Fore.WHITE}[{Fore.BLUE}+{Fore.WHITE}] IP Address  : {data.get('ip')}
{Fore.WHITE}[{Fore.BLUE}+{Fore.WHITE}] City        : {data.get('city')}
{Fore.WHITE}[{Fore.BLUE}+{Fore.WHITE}] Region      : {data.get('region')}
{Fore.WHITE}[{Fore.BLUE}+{Fore.WHITE}] Country     : {data.get('country')}
{Fore.WHITE}[{Fore.BLUE}+{Fore.WHITE}] Location    : {data.get('loc')}
{Fore.WHITE}[{Fore.BLUE}+{Fore.WHITE}] Organization: {data.get('org')}
{Fore.WHITE}[{Fore.BLUE}+{Fore.WHITE}] Timezone    : {data.get('timezone')}
"""
        else:
            return f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] Error: Unable to fetch information"
    except Exception as e:
        return f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] Error: {e}"

def get_local_ip_port():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            local_ip, local_port = s.getsockname()
            return local_ip, local_port
    except Exception as e:
        return "Error", str(e)

def get_ip_from_url(url):
    try:
        return socket.gethostbyname(url)
    except socket.error:
        return None

def lookup_site(url):
    ip = get_ip_from_url(url)
    
    if ip:
        geo_info = ip_lookup(ip)
        print(f"{Fore.WHITE}[{Fore.BLUE}+{Fore.WHITE}] URL     : {url}")
        print(f"{Fore.WHITE}[{Fore.BLUE}+{Fore.WHITE}] IP      : {ip}")
        print(geo_info)
    else:
        print(f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] Error: Unable to resolve URL to IP")

logo = f'''{Fore.BLUE}
   _      _____     _   _            _ _ _     _   
 _| |_   |   __|___|_|_| |___ ___   | | | |___| |_ 
|_   _|  |__   | . | | . | -_|  _|  | | | | -_| . |
  |_|    |_____|  _|_|___|___|_|    |_____|___|___|
               |_|                                 
              {Fore.WHITE}< C0ded By : A8Fit'aLRuqi >
'''

print(logo)

command = input(f"{Fore.WHITE}A8Fit{Fore.BLUE}@{Fore.WHITE}SpiderWeb : ").lower()

if command == "lookup":
    choice = input(f"{Fore.WHITE}[{Fore.BLUE}+{Fore.WHITE}] Lookup (IP/URL) : ").lower()
    if choice == "ip":
        ip_address = input(f"{Fore.WHITE}[{Fore.BLUE}+{Fore.WHITE}] Set IP Address : ")
        result = ip_lookup(ip_address)
        print(result)
    elif choice == "url":
        url = input(f"{Fore.WHITE}[{Fore.BLUE}+{Fore.WHITE}] Set URL : ").lower()
        lookup_site(url)
    else:
        print(f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] Error: Unknown choice")
elif command in ["help", "-h", "HELP", "-H", "Help"]:
    print(f"{Fore.WHITE}[{Fore.BLUE}+{Fore.WHITE}] Help Command's :")
    print(f"{Fore.WHITE}[{Fore.BLUE}+{Fore.WHITE}] Command : Lookup ")
else:
    print(f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] Unknown command")

local_ip, local_port = get_local_ip_port()
if local_ip != "Error":
    print('---------------------------------')
    print(f"{Fore.WHITE}[{Fore.BLUE}+{Fore.WHITE}] Local IP    : {local_ip}")
    print(f"{Fore.WHITE}[{Fore.BLUE}+{Fore.WHITE}] Local Port  : {local_port}")
else:
    print(f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] Error: {local_port}")
