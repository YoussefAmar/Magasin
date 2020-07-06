from socket import *
serverName = '192.168.0.101'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
MessageClient = None
MessageServer = None


def Menu():

    global MessageClient
    global MessageServer

    while MessageClient != "0" or MessageClient != "1":

        Recoit()  # Recoit le menu
        Envoi()  # Envoi une réponse au menu

    if MessageClient == "1":

        Recoit()  # Recoit la demande de choix de produit

        Envoi()  # Envoi le choix du produit

        Recoit()  # Recoit une liste de produit

        Envoi()  # Envoi le choix de l'aliment

        Recoit()  # Recoit le prix de l'aliment

        Envoi()  # Quantité envoyée

        Recoit()  # Recoit le prix total

        Menu()  # Retour au menu

    elif MessageClient == "0":
        Sortie()


def Recoit():

    global MessageServer
    MessageServer = clientSocket.recv(1024).decode()
    print(MessageServer)
    Sortie()
    return


def Envoi():

    global MessageClient

    MessageClient = input()  # envoi 0 ou 1 comme demande de requête
    clientSocket.send(MessageClient.encode('utf-8'))
    return


def Sortie():

    if MessageServer == "Au revoir":

        clientSocket.close()
        exit()

    elif MessageServer == "Non répertorié" or MessageServer == "Veuillez utiliser des nombres" or "Votre commande total vaut : " in MessageServer :
        Menu()

print("Veuillez entrer votre Identifiant")

Envoi()  # Envoi du message d'introduction

Menu()






