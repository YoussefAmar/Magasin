from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
MessageClient = None
MessageServer = None
Pomme = [3, "Pomme"]
Poire = [10, "Poire"]
Banane = [20, "Banane"]
Fruits = "Choississez un fruit : " + "1 : " + Pomme[1] + "/ 2 : " + Poire[1] + " / 3 : " + Banane[1] + " / 0 pour quitter "
Eau = [2, "Eau"]
Coca = [8, "Coca"]
Sprite = [250, "Sprite"]
Boissons = "Choississez une boisson : " + "1 : " + Eau[1] + " / 2 : " + Coca[1] + " / 3 : " + Sprite[1] + " / 0 pour quitter "
Total = 0
MessageAchat = "Combien vous en voulez ?"


def Achat():

    global MessageServer
    global MessageClient

    MessageServer = "Envoyez 1 pour acheter des fruits / 2 pour des boissons / 0 pour quitter / Autre chose pour retourner au menu"
    connectionSocket.send(MessageServer.encode())

    Recoit()

    if MessageClient == "1":

        connectionSocket.send(Fruits.encode())

        Recoit()

        if MessageClient == "3":
            MessageServer = Banane[1] + " -- Prix : " + str(Banane[0]) + " €"
            MessageServer = MessageServer + " -- " + MessageAchat
            connectionSocket.send(MessageServer.encode())
            Recoit()
            Ajout(Banane[0], MessageClient)
            connectionSocket.send(MessageServer.encode())
            choix_menu()

        elif MessageClient == "1":
            MessageServer = Pomme[1] + " -- Prix : " + str(Pomme[0]) + " €"
            MessageServer = MessageServer + " -- " + MessageAchat
            connectionSocket.send(MessageServer.encode())
            Recoit()
            Ajout(Pomme[0], MessageClient)
            connectionSocket.send(MessageServer.encode())
            choix_menu()

        elif MessageClient == "2":
            MessageServer = Poire[1] + " -- Prix : " + str(Poire[0]) + " €"
            MessageServer = MessageServer + " -- " + MessageAchat
            connectionSocket.send(MessageServer.encode())
            Recoit()
            Ajout(Poire[0], MessageClient)
            connectionSocket.send(MessageServer.encode())
            choix_menu()

        if MessageClient == "0":
            Sortie()

        else:
            MessageServer = "Non répertorié"
            connectionSocket.send(MessageServer.encode())
            choix_menu()

    if MessageClient == "2":

        connectionSocket.send(Boissons.encode())

        Recoit()

        if MessageClient == "1":
            MessageServer = Eau[1] + " -- Prix : " + str(Eau[0]) + " €"
            MessageServer = MessageServer + " -- " + MessageAchat
            connectionSocket.send(MessageServer.encode())
            Recoit()
            Ajout(Eau[0], MessageClient)
            connectionSocket.send(MessageServer.encode())
            choix_menu()

        elif MessageClient == "2":
            MessageServer = Coca[1] + " -- Prix : " + str(Coca[0]) + " €"
            MessageServer = MessageServer + " -- " + MessageAchat
            connectionSocket.send(MessageServer.encode())
            Recoit()
            Ajout(Coca[0], MessageClient)
            connectionSocket.send(MessageServer.encode())
            choix_menu()

        elif MessageClient == "3":
            MessageServer = Sprite[1] + " -- Prix : " + str(Sprite[0]) + " €"
            MessageServer = MessageServer + " -- " + MessageAchat
            connectionSocket.send(MessageServer.encode())
            Recoit()
            Ajout(Sprite[0], MessageClient)
            connectionSocket.send(MessageServer.encode())
            choix_menu()

        if MessageClient == "0":
            Sortie()

        else:
            MessageServer = "Non répertorié"
            connectionSocket.send(MessageServer.encode())
            choix_menu()

    if MessageClient == "0":
        Sortie()
    else:
        choix_menu()


def choix_menu():

    global Total
    global MessageServer
    global MessageClient

    flag = True

    while flag:

        MessageServer = "Bonjour " + Id + ", envoyez 1 pour faire un achat ou 0 pour quitter (Facture actuel : " + str(Total) + " €)"  # premier choix offert au client
        connectionSocket.send(MessageServer.encode())

        Recoit()  # reception du 1er choix

        if MessageClient == "0":
            flag = False
            Sortie()

        elif MessageClient == "1":
            flag = False
            Achat()
        else:
            flag = True


def Ajout(prix, x):

    global MessageServer
    global Total

    try:
        int(Total)
        Total = int(Total) + int(prix) * int(x)
        MessageServer = "Votre commande total vaut : " + str(Total) + " €"

    except ValueError:
        MessageServer = "Veuillez utiliser des nombres"


def Recoit():

    global MessageClient
    MessageClient = connectionSocket.recv(1024).decode()
    print(MessageClient)

    return


def Sortie():

    global MessageServer
    MessageServer = "Au revoir"
    connectionSocket.sendto(MessageServer.encode(), clientAddress)
    exit()

    return


while 1:

    connectionSocket, clientAddress = serverSocket.accept()

    Recoit()  # reçoit un message du client

    Id = MessageClient

    choix_menu()
