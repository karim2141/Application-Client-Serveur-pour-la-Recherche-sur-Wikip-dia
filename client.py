import socket
import socket
def start_client():
    server_ip = "127.0.0.1"  
    server_port = 8080  # 
    while True:  
        keyword = input("Entrez le mot à rechercher dans Wikipédia (entrez « exit » pour quitter) : ")
        if keyword.lower() == 'exit':
            break
        try:   
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((server_ip, server_port))
            print("Le serveur a été connecté.")   
            client_socket.send(keyword.encode('utf-8'))
            result = client_socket.recv(4096).decode('utf-8')
            print(f"Résultat de la recherche :\n{result}")
        except Exception as e:
            print(f"erreur: {str(e)}")
        finally:
            client_socket.close()
if __name__ == "__main__":
    start_client()

