import os
import socket
import time

count = 0
connected = True

class Daiv1_01:
    GAMEOVER = False
    noofplayers = 0
    dead, injured = 0, 0
    name2 = "player2"
    code2 = "1234"

    def __init__(self, players_name, players_code):
        self.playername = players_name
        self.playerscode = players_code
        self.string2intlist()

    def strcon(self, playerscode):
        strconv = []
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

        self.playerscode = self.duplicateremover

    def __guess__(self, pg):
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
            connected = False
            self.GAMEOVER = True


            print('GAME OVER')

        return self.dead, self.injured, self.GAMEOVER


    @staticmethod
    def game(pg):
        g = player1.__guess__(pg)
        d, i, j, = player1.guessing_result(g, Daiv1_01.code2)
        print(f'[{g}] -- {d} dead -- {i} injured')
        player1.dead, player1.injured = 0, 0
        if j:
            print(f'{name} WON congratulations ')
            client_socket_e.close()

    @staticmethod
    def mygame(pg): # TODO check this out
        g = player2.__guess__(pg)
        d, i, j, = player2.guessing_result(g, code)
        print(f'[{g}] -- {d} dead -- {i} injured')
        player2.dead, player2.injured = 0, 0
        if j:
            print(f'YOU lost and {Daiv1_01.name2} WON better luck next time')
            time_waster = f'the code was [{Daiv1_01.code2}]'
            for i in time_waster:
                print(i, flush=True, end='')
                time.sleep(0.2)
            client_socket_e.close()



HOST = input("Enter Host ip address :>>")
PORT = 9999
Format = 'utf-8'
name = input("enter your name please:")
code = input("enter your code please:")
player1 = Daiv1_01(name, code)
player2 = Daiv1_01(Daiv1_01.name2, Daiv1_01.code2)

client_socket_e = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_addr = (HOST, PORT)

client_socket_e.connect(client_addr)


def handle_recieved_messages(scket):
    print(f'{Daiv1_01.name2} <!> turn')
    if count == 0:


        os.system('cls')
        Daiv1_01.name2 = scket.recv(1024).decode(Format)
        print("collected [1/2]")
        return False
    elif count == 1:

        Daiv1_01.code2 = scket.recv(1024).decode(Format)
        print("collected [2/2]")
        return False

    elif count > 1:
        r_msg = scket.recv(1024).decode(Format)
        print(f"{Daiv1_01.name2} played --[{r_msg}] the result is")
        Daiv1_01.mygame(r_msg)

        return True


def handle_sent_messages(scket):
    print(f" your <*> turn {name}")
    if send_count == 0:
        scket.send(name.encode(Format))

        print("sent [1/2]")

        time.sleep(3)
        os.system('cls')

        return True
    elif send_count == 1:
        scket.send(code.encode(Format))

        print("sent [2/2]")
        time.sleep(3)
        os.system('cls')
        return False

    elif send_count > 1:
        msg = input(f"{name} guess :>> ")
        Daiv1_01.game(msg)
        scket.send(msg.encode(Format))

        return False


send1 = True
send_count = 0
while connected:
    if send1:

        send1 = handle_sent_messages(client_socket_e)
        send_count += 1
    else:

        send1 = handle_recieved_messages(client_socket_e)
        count += 1
