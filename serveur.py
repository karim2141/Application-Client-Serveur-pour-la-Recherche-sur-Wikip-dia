import socket
import wikipediaapi
def search_wikipedia(keyword):
    try:
        wiki = wikipediaapi.Wikipedia(
            language='fr',  
            user_agent="WikipediaClient/1.0 (https://fr.wikipedia.org/;)"
        )
        page = wiki.page(keyword)  
        if page.exists():
            return page.summary[:800]  
        else:
            return "Désolé, aucun résultat n'est disponible pour ce mot."
    except Exception as e:
        return f"Erreur lors de la recherche: {str(e)}"
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 8080))  
    server_socket.listen(5)
    print("Le serveur est prêt, en attente de connexions...")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Contacté de : {client_address}")
        try:  
            keyword = client_socket.recv(1024).decode('utf-8')
            print(f"Mot réceptif : {keyword}")    
            result = search_wikipedia(keyword)
            client_socket.send(result.encode('utf-8'))
        except Exception as e:
            print(f"Erreur lors du traitement avec le client : {str(e)}")
            client_socket.send("Une erreur de serveur s'est produite.".encode('utf-8'))
        finally:
            client_socket.close()

if __name__ == "__main__":
    start_server()
