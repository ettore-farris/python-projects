import socket

found_ports = False


def scan(target, ports):
    print("\n" + "[*] Iniziando la scan per " + target)
    for port in range(1, ports):
        port_scanner(target, port)
    if not(found_ports):
        print("Nessuna porta aperta trovata")


def port_scanner(ip, port):
    global found_ports
    try:
        scanner_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner_socket.connect((ip, port))
        scanner_socket.settimeout(.2)
        print(f"[+] La porta {port} è aperta")
        scanner_socket.close()
        found_ports = True
    except:
        pass


targets = input('Inserisci degli IP Target da scansionare (separati da ","): ')
ports = int(input("Inserisci il numero delle porte che vuoi scanzionare: "))

if "," in targets:
    print("[*] Scansionando target multipli...")
    for ip in targets.split(","):
        scan(ip.strip(" "), ports)
else:
    scan(targets, ports)
