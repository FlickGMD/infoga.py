#!/usr/bin/env python
import urllib3, argparse, sys, os
from urllib3 import Timeout
from Colors import *
from signal import SIGINT, signal

os.system(command='clear')
def handler(sign, frame):
    print(f"\n{bright_red}[!] Deteniendo programa...{end}\n\n")
    sys.exit(1)

signal(SIGINT, handler)

timeout = Timeout(connect=2.0, read=7.0)
http = urllib3.PoolManager(timeout=timeout)

def print_banner():
    return f"""{bright_blue}
██╗███╗   ██╗███████╗ ██████╗  ██████╗  █████╗ 
██║████╗  ██║██╔════╝██╔═══██╗██╔════╝ ██╔══██╗
██║██╔██╗ ██║█████╗  ██║   ██║██║  ███╗███████║
██║██║╚██╗██║██╔══╝  ██║   ██║██║   ██║██╔══██║
██║██║ ╚████║██║     ╚██████╔╝╚██████╔╝██║  ██║
╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
{end}                     
📞 {bright_white}INFOGA - OSINT para números de teléfono{end} 📞
───────────────────────────────────────────
🔍 {bright_white}Encuentra información de un número en segundos{end}
👤 {bright_white}Autor: Flick | GitHub: https://github.com/FlickGMD {end}
    """

def main():
    parser = argparse.ArgumentParser(description="Herramienta de OSSINT")
    parser.add_argument('-p', '--phone', dest='phone', required=True, help=f'📞 Número de telefono a pasarle (ex: {sys.argv[0]} --phone +1 234 567 89)')
    parser.add_argument('-a', '--api', dest='api', required=True, help=f'🔑 API KEY a indicar, es necesario! (ex: {sys.argv[0]} --api abcd1234fghi789) | Para sacar una api y usarla aqui, visita https://apilayer.com')
    parser.add_argument('-o', '--output', dest='output', required=False, help=f'📄 Archivo a indicarle donde guardaras tu evidencia (ex: {sys.argv[0]} --output /tmp/file.txt)')
    parser.add_argument('-x', '--exclude_banner', dest='banner_off', required=False, action='store_true',help=' Excluir el banner al momento de mostrar información')

    options = parser.parse_args() 
    return options.phone, options.api, options.output, options.banner_off

def sendRequest(phone, api):
    headers = {
            'apikey': '%s' % (api)
            }

    url = "https://api.apilayer.com/number_verification/validate?number=%s" % (phone) 

    response = http.request(method='GET', url=url, headers=headers)
    if (response.status) == 200:
        return response.data.decode()

def sendOutput(data, output):
    if not output:
        return

    if not os.path.exists(output):
        with open(output, 'w') as file:
            (file.write(data))

if __name__ == "__main__":
    phone, api, output, banner_off = main()
    print(print_banner() if not banner_off else '\r')
    data = sendRequest(phone, api)
    (sendOutput(data, output))
    print(f"{bright_white}{data}{end}")
