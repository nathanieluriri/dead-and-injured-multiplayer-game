import random as rd
import time


class Player:

    GAMEOVER = False
    dead,injured = 0,0

    def __init__(self):
        self.playername =self.getname()
        self.playerscode =self.getcode()
        self.string2intlist()

    def getname(self):
        name = input("enter your name:")
        return name

    def getcode(self):
        code = input("enter your code:")
        return code

    def strcon(self,playerscode):
        strconv=[]
        for i in range(len(playerscode)):
            num = int(playerscode[i])
            strconv.append(num)
        return strconv

    def string2intlist(self, guess = None):
        if guess==None:
            self.duplicateremover = []
            self.playerscode = self.strcon(self.playerscode)
            for num in self.playerscode:
                if num not in self.duplicateremover:
                    self.duplicateremover.append(num)
            self.playerscode =self.duplicateremover
            self.strcon(self.playerscode)
        else:
            self.duplicateremover = []
            self.playersguess = self.strcon(self.playersguess)
            for num in self.playersguess:
                if num not in self.duplicateremover:
                    self.duplicateremover.append(num)
            self.playersguess = self.duplicateremover
            self.strcon(self.playersguess)

    def guess(self):
        self.dead,self.injured=0,0
        guess = input("enter your guess:")
        result=self.__guess__(guess)
        return result

    def __guess__(self,pg):
        if type(pg) is not str:
            raise TypeError
        else:
            self.playersguess = pg
            self.string2intlist(guess=self.playersguess)

        return self.playersguess

    def guessing_result(self, PlayersGuess, OpponentsCode):
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
        return self.dead ,self.injured,self.GAMEOVER
    @staticmethod
    def start():
        game = True
        g1,g2 =False,False
        t1 = True
        while game == True and (g1 == False and g2 == False):
            while g1 == False and t1 ==True:
                t1 = False
                guess = player.guess()
                d1,i1,g1 = player.guessing_result(guess,computer.playerscode)
                print(f'{player.playername} guessed {guess}')
                print(f'{d1} - dead {i1} - injured')
            while g2 == False and t1 == False:
                time.sleep(1)
                t1 = True
                com_guess = computer.guess()
                d2,i2,g2 = computer.guessing_result(com_guess,player.playerscode)
                print(f'{computer.playername} guessed {com_guess}')
                print(f'{d2} - dead {i2} - injured')



class Computer(Player):
    def getname(self):
        return "computer"

    def getcode(self):
        set_of_string = ['0', '1', '2', '3', '4', "5", '6', '7', '8', '9']
        code_in_list = rd.sample(set_of_string, 4)
        code_in_string = str()
        for i in range(len(code_in_list)):
            code_in_string += code_in_list[i]
        return code_in_string

    def guess(self):
        self.injured,self.dead =0,0
        set_of_string = [0,1,2,3,4,5,6,7,8,9]
        guess= rd.sample(set_of_string,4)
        return guess







player = Player()
computer = Computer()
Player.start()

