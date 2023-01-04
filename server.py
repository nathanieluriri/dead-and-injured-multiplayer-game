import os
import socket
import threading
import time
connected = True
send_count = 0
count = 0
class Daiv1_01:
    GAMEOVER = False
    noofplayers = 0
    dead,injured = 0,0
    name2 = "player2"
    code2 = "1234"

    def __init__(self,players_name,players_code):
        self.playername = players_name
        self.playerscode = players_code
        self.string2intlist()

        os.system('cls')

    def strcon(self,playerscode):
        strconv=[]
        for i in range(len(playerscode)):
            num = int(playerscode[i])
            strconv.append(num)

        return strconv


    def string2intlist(self):
        self.duplicateremover = []

        self.playerscode = self.strcon(self.playerscode)
        for num in self.playerscode:
            if num not in self.duplicateremover:
                self.duplicateremover.append(num)

        self.playerscode =self.duplicateremover





    def __guess__(self,pg):
        if type(pg) is not str:
            print(pg)
        else:
            self.playersguess = pg
            self.playersguess = self.strcon(self.playersguess)
        return self.playersguess

    def guessing_result(self, PlayersGuess, OpponentsCode):
        global connected
        OpponentsCode = self.strcon(OpponentsCode)
        for i in range(4):
            if PlayersGuess[i] == OpponentsCode[i]:
                self.dead += 1
            if PlayersGuess[i] == OpponentsCode[0] and PlayersGuess[i] != OpponentsCode[i]:
                self.injured += 1

            elif PlayersGuess[i] == OpponentsCode[1] and PlayersGuess[i] != OpponentsCode[i]:
                self.injured += 1

            elif PlayersGuess[i] == OpponentsCode[2] and PlayersGuess[i] != OpponentsCode[i]:
                self.injured += 1
            elif PlayersGuess[i] == OpponentsCode[3] and PlayersGuess[i] != OpponentsCode[i]:
                self.injured += 1
            if self.dead == 4:
                self.GAMEOVER = True
                print(f'GAME OVERRR')
                connected = False
        return self.dead ,self.injured,self.GAMEOVER
    @staticmethod
    def game(pg):
        g = player1.__guess__(pg)
        d,i,j,=player1.guessing_result(g,Daiv1_01.code2)
        print(f'[{g}] -- {d} dead -- {i} injured')
        player1.dead ,player1.injured = 0,0
        if j:
            print(f'{name1} Congratulations you won')
            server_socket_e.close()


    @staticmethod
    def mygame(pg): # TODO check this out
        g = player2.__guess__(pg)
        d, i, j, = player2.guessing_result(g, code1)
        print(f'[{g}] -- {d} dead -- {i} injured')
        player2.dead, player2.injured = 0, 0

        if j:
            print(f'YOU LOSE and [{Daiv1_01.name2}] won the persons code was {Daiv1_01.code2}')
            time_waster = f'the code was [{Daiv1_01.code2}]'
            for i in time_waster:
                print(i, flush=True, end='')
                time.sleep(0.4)
            server_socket_e.close()

    @staticmethod
    def recieve_clients_messages(client):
        print(f'{Daiv1_01.name2} <!> turn')
        if count ==0:

            msg = client.recv(1024).decode(Format)
            Daiv1_01.name2 = msg

            print("collected [1/2]")

            return False
        elif count ==1:
            msg = client.recv(1024).decode(Format)
            Daiv1_01.code2 = msg

            print("collected [2/2]")


            return True

        elif count >1:
            msg = client.recv(1024).decode(Format)
            Daiv1_01.mygame(msg)


            return True

    @staticmethod
    def send_clients_messages(client):
        print(f"your <*> turn {name1}")

        if send_count == 0:
            os.system('cls')
            client.send(name1.encode(Format))
            print("sent [1/2]")

            time.sleep(5)
            os.system('cls')
            return True
        elif send_count == 1:
            client.send(code1.encode(Format))
            print("sent [2/2]")
            os.system('cls')
            time.sleep(3)
            return True
        elif send_count >1:
            msg = input(f"enter your guess {name1} :>>")
            Daiv1_01.game(msg)
            client.send(msg.encode(Format))


            return False


name1 = input("your name:")
code1 = input("your code:")
player1 = Daiv1_01(name1,code1)
player2 = Daiv1_01(Daiv1_01.name2,Daiv1_01.code2)



Format = 'utf-8'
private_ip = socket.gethostbyname(socket.gethostname())

PORT = 9999
server_socket_e = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ADDR = (private_ip,PORT)
server_socket_e.bind(ADDR)

server_socket_e.listen()

send1 = False




print(f'SERVER RUNNING --on-- [{private_ip}]')
search = True
while search:
    print("...[searching]...")

    connected_socket, client_addr = server_socket_e.accept() # get the socket to communicate with

    print(f'[CONNECTED TO]--[{client_addr}]') # just a display of the clients address
    search = False



while connected:

    if send1:
        send1= Daiv1_01.send_clients_messages(connected_socket)
        send_count +=1
        # print(count)
    else:
        send1= Daiv1_01.recieve_clients_messages(connected_socket)
        # print(count)
        count += 1




