import socket
import threading
import concurrent.futures
import colorama
from colorama import Fore
colorama.init()

print_lock = threading.Lock()

ip = input("Enter the IP to scan: ")

def scan(ip,port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((ip, port))
        scanner.close()
        with print_lock:
            print(Fore.WHIITE + f"[{port}]" + Fore.Green + " Opened")
    except:
        pass

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(1000):
        executor.submit(scan, ip, port)