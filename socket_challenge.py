import socket
import math

#dati dell'host: indirizzo del server e porta in ascolto
SERVER_HOST = "INSERISCI INDIRIZZO" 
LPORT = 0000 #INSERISCI PORTA

#creazione del socket TCP di rete composto dall'indirizzo IP del server e dalla porta
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#richiesta di connessione al server
sock.connect((SERVER_HOST, LPORT))

#messaggio inviato dal server una volta effettuata la connessione 
msg = sock.recv(1024).decode("utf-8")
print(msg)

#estrapolazione dei numeri dal testo e conversione in integer
num_1 = int(msg.split()[27])
num_2 = int(msg.split()[31])

#calcolo del risultato e arrotondamento per due cifre decimali
result = round((math.sqrt(num_1) * num_2), 2)

#invio risposta al server (aggiungere "\n" alla stringa per evitare errori di buffer)
sock.send((str(result) + "\n").encode('utf-8'))

#conferma di avvenuta risposta
confirmation = sock.recv(1024).decode('utf-8')
print(confirmation)

#chiusura connessione
sock.close()

