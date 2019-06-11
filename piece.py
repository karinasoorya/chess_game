#King movement issues? Make sure the logic is sounds there. I think something is a little off. Particularly when in check.

class Piece:

    posX = 0
    posY = 0

    validMoves = True
    howManyDidIKill = 0
    dead = False
    side = None
    name = ""


    def __init__(self, name, side, posX, posY):
        self.name = name
        self.side = side
        self.posX = posX
        self.posY = posY
        self.allowed_moves = []

    def posIsVal(self, positions, a, b):
        if(a in positions.keys()):
            if b in range(len(positions[a])):
                return True

    def spotTaken(self, posX, posY, positions):
        if type(positions[posX][posY]) == str:
            return False
        return True

    def spotTakenByFriend(self, positions, posX, posY):
        soldier = positions[posX][posY]
        if type(soldier) != str:
            if soldier.side == self.side:
                return True
        return False

    def isAllowed(self, positions, posX, posY):
        if self.posIsVal(positions, posX, posY):
            if not self.spotTakenByFriend(positions, posX, posY):
                if type(self) == King:
                    if not self.vuln(positions, posX, posY):
                        return True
                    else:
                        return False
                else:
                    return True
        return False

    def enemyHere(self, posX, posY, positions):
        enemy_side = "White"
        if self.side == "White":
            enemy_side = "Black"
        if type(positions[posX][posY]) != str:
            p = positions[posX][posY]
            if p.side == enemy_side:
                return True
        return False

    def xmod(self, posX, changeX):
        ans = chr(ord(posX) + changeX)
        if ans in ['a', 'b', 'c', 'd', 'e', 'f' , 'g' ,'h']:
            return ans

    def vuln(self, positions, posX, posY):
        pos = str(posX) + str(posY)
        enemy_side = "White"

        if self.side == "White":
            enemy_side = "Black"

        for key in positions.keys():
            for p in positions[key]:
                if type(p) != str:
                    if p.side == enemy_side:
                        if type(p) == King:
                            if posX == p.xmod(posX, 1) or posX == p.xmod(posX, -1) or posX == p.posX:
                                if posY == int(p.posY) + 1 or posY == int(p.posY) - 1 or posY == int(p.posY):
                                    return True
                        else:
                            if p.canMove(positions):
                                if pos in p.allowed_moves:
                                    return True
        return False

    def pathFinder(self, positions, changeX, changeY):
        if changeX == True:
            if changeY == True:
                for i in range(1, 8):
                    if self.posIsVal(positions, self.xmod(self.posX, i), self.posY + i):
                        if(self.spotTakenByFriend(positions, self.xmod(self.posX, i), self.posY + i)):
                            break
                        elif self.enemyHere(self.xmod(self.posX, i), self.posY + i, positions):
                            self.allowed_moves.append(str(self.xmod(self.posX, i))+str(self.posY + i))
                            break
                        else:
                            self.allowed_moves.append(str(self.xmod(self.posX, i))+str(self.posY + i))
                    else:
                        break

                for i in range(1, 8):
                    if self.posIsVal(positions, self.xmod(self.posX, -1 * i), self.posY - i):
                        if(self.spotTakenByFriend(positions, self.xmod(self.posX, -1 * i), self.posY - i)):
                            break
                        elif self.enemyHere(self.xmod(self.posX, -1 * i), self.posY - i, positions):
                            self.allowed_moves.append(str(self.xmod(self.posX, -1 * i))+str(self.posY - i))
                            break
                        else:
                            self.allowed_moves.append(str(self.xmod(self.posX, -1 * i))+str(self.posY - i))
                    else:
                        break

                for i in range(1, 8):
                    if self.posIsVal(positions, self.xmod(self.posX, -1 * i), self.posY + i):
                        if(self.spotTakenByFriend(positions, self.xmod(self.posX, -1 * i), self.posY + i)):
                            break
                        elif self.enemyHere(self.xmod(self.posX, -1 * i), self.posY + i, positions):
                            self.allowed_moves.append(str(self.xmod(self.posX, -1 * i))+str(self.posY + i))
                            break
                        else:
                            self.allowed_moves.append(str(self.xmod(self.posX, -1 * i))+str(self.posY + i))
                    else:
                        break


                for i in range(1, 8):
                    if self.posIsVal(positions, self.xmod(self.posX,  i), self.posY - i):
                        if(self.spotTakenByFriend(positions, self.xmod(self.posX, i), self.posY - i)):
                            break
                        elif self.enemyHere(self.xmod(self.posX, i), self.posY - i, positions):
                            self.allowed_moves.append(str(self.xmod(self.posX, i))+str(self.posY - i))
                            break
                        else:
                            self.allowed_moves.append(str(self.xmod(self.posX, i))+str(self.posY - i))
                    else:
                        break

            else:
                for i in range(1, 8):
                    if(self.posIsVal(positions, self.xmod(self.posX, -1 * i), self.posY)):
                        if(self.enemyHere(self.xmod(self.posX, -1 * i), self.posY, positions)):
                            self.allowed_moves.append(str(self.xmod(self.posX, -1 * i)) + str(self.posY))
                            break
                        elif(self.spotTakenByFriend(positions, self.xmod(self.posX, -1 * i), self.posY)):
                            break
                        else:
                            self.allowed_moves.append(str(self.xmod(self.posX, -1 * i)) + str(self.posY))
                    else:
                        break

                for i in range(1, 8):
                    if self.posIsVal(positions, self.xmod(self.posX, i), self.posY):
                        if(self.spotTakenByFriend(positions, self.xmod(self.posX, i), self.posY)):
                            break
                        elif self.enemyHere(self.xmod(self.posX, i), self.posY, positions):
                            self.allowed_moves.append(str(self.xmod(self.posX, i))+str(self.posY))
                            break
                        else:
                            self.allowed_moves.append(str(self.xmod(self.posX, i))+str(self.posY))
                    else:
                        break

        else:
            if changeY == True:
                for i in range(1, 8):
                    if(self.posIsVal(positions, self.posX, self.posY + i)):
                        if(self.enemyHere(self.posX, self.posY + i, positions)):
                            self.allowed_moves.append(str(self.posX) + str(self.posY + i))
                            break
                        elif(self.spotTakenByFriend(positions, self.posX, self.posY + i)):
                            break
                        else:
                            self.allowed_moves.append(str(self.posX) + str(self.posY + i))
                    else:
                        break

                for i in range(1, 8):
                    if(self.posIsVal(positions, self.posX, self.posY - i)):
                        if(self.enemyHere(self.posX, self.posY - i, positions)):
                            self.allowed_moves.append(str(self.posX) + str(self.posY - i))
                            break
                        elif(self.spotTakenByFriend(positions, self.posX, self.posY - i)):
                            break
                        else:
                            self.allowed_moves.append(str(self.posX) + str(self.posY - i))
                    else:
                        break

class King(Piece):

    hasNotMovedYet = True

    def __init__(self, name, side, posX, posY):
        super().__init__(name, side, posX, posY)

    def canMove(self, positions):

        self.allowed_moves.clear()

        self.posY = int(self.posY)
        if(self.isAllowed(positions, self.xmod(self.posX, 1), self.posY)):
            self.allowed_moves.append(self.xmod(self.posX, 1) + str(self.posY))
        if(self.isAllowed(positions, self.xmod(self.posX, - 1), self.posY)):
            self.allowed_moves.append(self.xmod(self.posX, -1) + str(self.posY))
        if(self.isAllowed(positions, self.posX, self.posY - 1)):
            self.allowed_moves.append(self.posX + str(self.posY - 1))
        if(self.isAllowed(positions, self.posX, self.posY + 1)):
            self.allowed_moves.append(self.posX + str(self.posY + 1))
        if(self.isAllowed(positions, self.xmod(self.posX, - 1), self.posY - 1)):
            self.allowed_moves.append(self.xmod(self.posX, -1) + str(self.posY - 1))
        if(self.isAllowed(positions, self.xmod(self.posX,  1), self.posY + 1)):
            self.allowed_moves.append(self.xmod(self.posX, 1) + str(self.posY + 1))
        if(self.isAllowed(positions, self.xmod(self.posX, 1), self.posY - 1)):
            self.allowed_moves.append(self.xmod(self.posX, 1) + str(self.posY - 1))
        if self.isAllowed(positions, self.xmod(self.posX, -1), self.posY + 1):
            self.allowed_moves.append(self.xmod(self.posX, -1) + str(self.posY + 1))

        if len(self.allowed_moves) == 0:
            self.validMoves = False
        else:
            self.validMoves = True

        return self.validMoves

class Queen(Piece):

    def __init__(self, name, side, posX, posY):
        super().__init__(name, side, posX, posY)

    def canMove(self, positions):

        self.allowed_moves.clear()
        self.posY = int(self.posY)

        self.pathFinder(positions, False, True)
        self.pathFinder(positions, True, False)
        self.pathFinder(positions, True, True)

        if len(self.allowed_moves) == 0:
            self.validMoves = False
        else:
            self.validMoves = True

        return self.validMoves

class Rook(Piece):

    hasNotMovedYet = True

    def __init__(self, name, side, posX, posY):
        super().__init__(name, side, posX, posY)

    def canMove(self, positions):

        self.allowed_moves.clear()
        self.posY = int(self.posY)

        self.pathFinder(positions, False, True)
        self.pathFinder(positions, True, False)

        if len(self.allowed_moves) == 0:
            self.validMoves = False
        else:
            self.validMoves = True

        return self.validMoves

class Pawn(Piece):

    first_turn = True

    def __init__(self, name, side, posX, posY):
        super().__init__(name, side, posX, posY)

    def canMove(self, positions):
        self.allowed_moves.clear()
        self.posY = int(self.posY)
        if(self.first_turn):
            if(self.side == "Black"):
                if(self.posIsVal(positions, self.posX, self.posY - 2)):
                    if(not self.spotTaken(self.posX, self.posY - 2, positions)):
                        self.allowed_moves.append(str(self.posX) + str(self.posY - 2))
            else:
                if(self.posIsVal(positions, self.posX, self.posY + 2)):
                    if(not self.spotTaken(self.posX, self.posY + 2, positions)):
                        self.allowed_moves.append(str(self.posX) + str(self.posY + 2))

        if(self.posIsVal(positions, self.posX,self.posY - 1)):
            if self.side == "Black":
                if(not self.spotTaken(self.posX, self.posY - 1, positions)):
                    self.allowed_moves.append(str(self.posX) + str(self.posY - 1))
        if(self.posIsVal(positions, self.posX, self.posY + 1)):
            if self.side == "White":
                if(not self.spotTaken(self.posX, self.posY + 1, positions)):
                    self.allowed_moves.append(str(self.posX) + str(self.posY + 1))
        if(self.posIsVal(positions,self.xmod(self.posX, 1), self.posY + 1)):
            if self.side == "White":
                if self.enemyHere(self.xmod(self.posX, 1), self.posY + 1, positions):
                    self.allowed_moves.append(str(self.xmod(self.posX, 1)) + str(self.posY + 1))
        if(self.posIsVal(positions, self.xmod(self.posX, - 1), self.posY - 1)):
            if self.side == "Black":
                if self.enemyHere(self.xmod(self.posX, - 1), self.posY - 1, positions):
                    self.allowed_moves.append(str(self.xmod(self.posX, - 1)) + str(self.posY - 1))
        if(self.posIsVal(positions, self.xmod(self.posX, 1), self.posY - 1)):
            if self.side == "Black":
                if self.enemyHere(self.xmod(self.posX, 1), self.posY - 1, positions):
                    self.allowed_moves.append(str(self.xmod(self.posX, 1)) + str(self.posY - 1))
        if(self.posIsVal(positions, self.xmod(self.posX, -1), self.posY + 1)):
            if self.side == "White":
                if self.enemyHere(self.xmod(self.posX, - 1), self.posY + 1, positions):
                    self.allowed_moves.append(str(self.xmod(self.posX, - 1)) + str(self.posY + 1))

        if len(self.allowed_moves) == 0:
            self.validMoves = False
        else:
            self.validMoves = True

        return self.validMoves

class Knight(Piece):

    def __init__(self, name, side, posX, posY):
        super().__init__(name, side, posX, posY)


    def canMove(self, positions):
        self.allowed_moves.clear()
        self.posY = int(self.posY)

        if(self.isAllowed(positions, self.xmod(self.posX, 2), self.posY - 1)):
            self.allowed_moves.append(str(self.xmod(self.posX, 2)) + str(self.posY - 1))
        if(self.isAllowed(positions, self.xmod(self.posX, 2), self.posY + 1)):
            self.allowed_moves.append(str(self.xmod(self.posX, 2)) + str(self.posY + 1))
        if(self.isAllowed(positions, self.xmod(self.posX, -2), self.posY - 1)):
            self.allowed_moves.append(str(self.xmod(self.posX, -2)) + str(self.posY - 1))
        if(self.isAllowed(positions, self.xmod(self.posX, -2), self.posY + 1)):
            self.allowed_moves.append(str(self.xmod(self.posX, -2)) + str(self.posY + 1))
        if(self.isAllowed(positions, self.xmod(self.posX, 1), self.posY - 2)):
            self.allowed_moves.append(str(self.xmod(self.posX, 1)) + str(self.posY - 2))
        if(self.isAllowed(positions, self.xmod(self.posX, 1), self.posY + 2)):
            self.allowed_moves.append(str(self.xmod(self.posX, 1)) + str(self.posY + 2))
        if(self.isAllowed(positions, self.xmod(self.posX, -1), self.posY - 2)):
            self.allowed_moves.append(str(self.xmod(self.posX, -1)) + str(self.posY - 2))
        if(self.isAllowed(positions, self.xmod(self.posX, -1), self.posY + 2)):
            self.allowed_moves.append(str(self.xmod(self.posX, -1)) + str(self.posY + 2))

        if len(self.allowed_moves) == 0:
            self.validMoves = False
        else:
            self.validMoves = True

        return self.validMoves

class Bishop(Piece):
    def __init__(self, name, side, posX, posY):
        super().__init__(name, side, posX, posY)

    def canMove(self, positions):

        self.allowed_moves.clear()

        self.posY = int(self.posY)

        self.pathFinder(positions, True, True)

        if len(self.allowed_moves) == 0:
            self.validMoves = False
        else:
            self.validMoves = True

        return self.validMoves
