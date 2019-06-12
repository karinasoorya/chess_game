import piece

class Board():

    letters = ['a','b','c','d','e','f','g','h'] #The letters to index our board horizontally
    positions = {} #The main data structure for storing the board
    pieces = [] #Tracker of pieces
    white_pawn_goal = 7 #End of the line for white to get promoted
    black_pawn_goal = 0 #End of the line for black to get promoted

    #Constructor for Board class, initializes the positions structure that represents the board.
    def __init__(self):
        for letter in self.letters:
            self.positions[letter] = ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
        self.populate()

    #Get the king of the current player so we can use him to check game state and if a move is allowed or it puts you in check.
    def getKing(self, current_player):
        for key in self.positions.keys():
            for p in self.positions[key]:
                if type(p) != str:
                    if p.side == current_player and type(p) == piece.King:
                        return p

    #Update the pieces (gets called when a piece is killed or promoted)
    def update_pieces(self):
        self.pieces.clear()
        for key in self.positions.keys():
            for p in self.positions[key]:
                if type(p) != str:
                    self.pieces.append(p)

    #Populate the board
    def populate(self):
        self.positions['a'][7] = piece.Rook('bR', 'Black', 'a', '7')
        self.positions['b'][7] = piece.Knight('bKn', 'Black', 'b', '7')
        self.positions['c'][7] = piece.Bishop('bB', 'Black', 'c', '7')
        self.positions['d'][7] = piece.Queen('bQ', 'Black', 'd', '7')
        self.positions['e'][7] = piece.King('bK', 'Black', 'e', '7')
        self.positions['f'][7] = piece.Bishop('bB', 'Black', 'f', '7')
        self.positions['g'][7] = piece.Knight('bKn', 'Black', 'g', '7')
        self.positions['h'][7] = piece.Rook('bR', 'Black', 'h', '7')
        self.positions['a'][0] = piece.Rook('wR', 'White', 'a', '0')
        self.positions['b'][0] = piece.Knight('wKn', 'White', 'b', '0')
        self.positions['c'][0] = piece.Bishop('wB', 'White', 'c', '0')
        self.positions['d'][0] = piece.Queen('wQ', 'White', 'd', '0')
        self.positions['e'][0] = piece.King('wK', 'White', 'e', '0')
        self.positions['f'][0] = piece.Bishop('wB', 'White', 'f', '0')
        self.positions['g'][0] = piece.Knight('wKn', 'White', 'g', '0')
        self.positions['h'][0] = piece.Rook('wR', 'White', 'h', '0')
        for letter in self.letters:
            self.positions[letter][6] = piece.Pawn('bP', 'Black', letter, '6')
            self.positions[letter][1] = piece.Pawn('wP', 'White', letter, '1')
        for letter in self.letters:
            for num in self.positions[letter]:
                if type(num) != str:
                    self.pieces.append(num)

    #Move making logic, if the program gets here, the move has been validated.
    def makeMove(self, initialX, initialY, posX, posY):
        posY = int(posY) - 1
        initialY = int(initialY) - 1
        #Get the piece in question and update its knowledge of its location, make the move. If there was a piece in the new spot, update the piece tracker.
        current_soldier = self.positions[initialX][initialY]
        current_soldier.posX = posX
        current_soldier.posY = posY
        old_soldier = self.positions[posX][posY]
        self.positions[posX][posY] = current_soldier
        self.positions[initialX][initialY] = ' '
        if type(old_soldier) != str:
            self.update_pieces()
        #Update logic for individual pieces with special cases
        if type(current_soldier) == piece.King or type(current_soldier) == piece.Rook:
            current_soldier.hasNotMovedYet = False
        if type(current_soldier) == piece.Pawn:
            if current_soldier.first_turn:
                current_soldier.first_turn = False
            #Handle promotion logic for pawns and update piece tracker to reflect this.
            if current_soldier.posY == self.white_pawn_goal and current_soldier.side == "White":
                picked = False
                while not picked:
                    promotion = input("Enter what kind of piece you want your pawn to be promoted to - your options are Q, Kn, R or B: ")
                    if promotion == "Kn":
                        self.positions[current_soldier.posX][current_soldier.posY] = piece.Knight('wKn', 'White', current_soldier.posX, current_soldier.posY)
                        picked = True
                    elif promotion == "Q":
                        self.positions[current_soldier.posX][current_soldier.posY] = piece.Queen('wQ', 'White', current_soldier.posX, current_soldier.posY)
                        picked = True
                    elif promotion == "R":
                        self.positions[current_soldier.posX][current_soldier.posY] = piece.Rook('wR', 'White', current_soldier.posX, current_soldier.posY)
                        picked = True
                    elif promotion == "B":
                        self.positions[current_soldier.posX][current_soldier.posY] = piece.Bishop('wB', 'White', current_soldier.posX, current_soldier.posY)
                        picked = True
                    else:
                        self.printer()
                        print("Issue with the piece name you're inputting")
                self.update_pieces()
            elif current_soldier.posY == self.black_pawn_goal and current_soldier.side == "Black":
                picked = False
                while not picked:
                    promotion = input("Enter what kind of piece you want your pawn to be promoted to - your options are Q, Kn, R or B: ")
                    if promotion == "Kn":
                        self.positions[current_soldier.posX][current_soldier.posY] = piece.Knight('bKn', 'Black', current_soldier.posX, current_soldier.posY)
                        picked = True
                    elif promotion == "Q":
                        self.positions[current_soldier.posX][current_soldier.posY] = piece.Queen('bQ', 'Black', current_soldier.posX, current_soldier.posY)
                        picked = True
                    elif promotion == "R":
                        self.positions[current_soldier.posX][current_soldier.posY] = piece.Rook('bR', 'Black', current_soldier.posX, current_soldier.posY)
                        picked = True
                    elif promotion == "B":
                        self.positions[current_soldier.posX][current_soldier.posY] = piece.Bishop('bB', 'Black', current_soldier.posX, current_soldier.posY)
                        picked = True
                    else:
                        print("Issue with the piece name you're inputting")
                self.update_pieces()

    #Board printer
    def printer(self):
        print(" ")
        print("Chess Game!")
        print(" ")
        print("  ", end = " ")
        for letter in self.letters:
            flag = False
            for item in self.positions[letter]:
                if(type(item) != str):
                    if 'wKn' in item.name or 'bKn' in item.name:
                        print(letter, end = " | ")
                        flag = True
                        break
            if not flag:
                print(letter, end = " | ")
        print(" ")
        for num in range(8):
            print(num + 1, end = " ")
            for letter in self.letters:
                if(type(self.positions[letter][num])!= str):
                    if(self.positions[letter][num].name == "wKn" or self.positions[letter][num].name == "bKn"):
                        print(self.positions[letter][num].name, end = "|")
                    else:
                        print(self.positions[letter][num].name, end = " |")
                elif num == 0 or num == 1 or num == 6 or num == 7:
                    print(self.positions[letter][num], end = "  |")
                else:
                    self.positions[letter][num] = '  '
                    print(self.positions[letter][num], end = " |")
            print(" ")
            print("---------------------------------")

    #Input validation - checks if a position and piece are in line with the game and whose turn it is, also makes sure
    #A move is allowed and doesn't put your king in danger or disobey piece rules.
    def input_validate(self, side, the_piece, initialX, initialY, posX, posY):
        posY = int(posY)
        initialY = int(initialY)
        keeper = " "
        flag = False
        if posX in self.letters and posY in range(1,9):
            if (the_piece[0] == 'w' and side == "White") or (the_piece[0] == 'b' and side == "Black"):
                if the_piece[1:] in ['Kn', 'K', 'Q', 'B', 'R', 'P']:
                    for soldier in self.pieces:
                        if soldier.name == the_piece and soldier.posX == initialX and int(soldier.posY) == initialY - 1:
                            if soldier.canMove(self.positions):

                                for move in soldier.allowed_moves:
                                    move = list(move)
                                    if move[0] == posX and move[1] == str(posY - 1):
                                        king = self.getKing(soldier.side)

                                        if self.positions[posX][posY - 1] != str:
                                            keeper = self.positions[posX][posY - 1]
                                        else:
                                            continue

                                        self.positions[soldier.posX][soldier.posY] = ' '
                                        self.positions[posX][posY - 1] = soldier
                                        soldier.posX = posX
                                        soldier.posY = posY - 1

                                        if king.vuln(self.positions, king.posX, king.posY):
                                            print("You're putting your king in danger!")
                                        else:
                                            flag = True

                                        soldier.posX = initialX
                                        soldier.posY = initialY - 1
                                        self.positions[initialX][initialY - 1] = soldier
                                        self.positions[posX][posY - 1] = keeper

        return flag

    #Check for checkmate - see if the king can move to a safe space, or if someone can save him.
    def didICheckMate(self, current_player):
        enemy = "White"
        if current_player == "White":
            enemy = "Black"
        potential_interference = []
        if self.didICheck(current_player):
            for key in self.positions:
                for a_piece in self.positions[key]:
                    if type(a_piece) != str:
                        if type(a_piece) == piece.King and a_piece.side == enemy:
                            king_in_trouble = a_piece
                        elif a_piece.side == enemy:
                            potential_interference.append(a_piece)
            if king_in_trouble.canMove(self.positions):
                return False
            elif(self.canSaveKing(potential_interference, king_in_trouble)):
                return False
            else:
                return True

    #Check to see if someone can save the king by making a move - simulate their turn to see if the king ends up not vulnerable.
    def canSaveKing(self, interference, king):
        keeper = " "
        old_location_x = ""
        old_location_y = ""
        for a_piece in interference:
            if a_piece.canMove(self.positions):
                old_location_x = a_piece.posX
                old_location_y = int(a_piece.posY)
                for pos in a_piece.allowed_moves:
                    pos = list(pos)
                    new_x = pos[0]
                    new_y = int(pos[1])
                    if self.positions[new_x][new_y] != str:
                        keeper = self.positions[new_x][new_y]
                    self.makeMove(a_piece.posX, int(a_piece.posY) + 1, new_x, new_y + 1)
                    if not king.vuln(self.positions, king.posX, int(king.posY)):
                        self.makeMove(a_piece.posX, int(a_piece.posY) + 1, old_location_x, old_location_y + 1)
                        self.positions[new_x][new_y] = keeper
                        return True
                    else:
                        self.makeMove(a_piece.posX, int(a_piece.posY + 1), old_location_x, old_location_y + 1)
                        self.positions[new_x][new_y] = keeper
        return False

    #Check helper function to see if the enemy king is now vulnerable.
    def didICheck(self, current_player):
        enemy = "White"
        if current_player == "White":
            enemy = "Black"
        king = self.getKing(enemy)
        if king.vuln(self.positions, king.posX, king.posY):
            return True
        return False

    #Check to see if there are no more moves for the next player.
    def noValidMoves(self, current_player):
        thinker = "White"
        if current_player == "White":
            thinker = "Black"
        for key in self.positions.keys():
            for a_piece in self.positions[key]:
                if type(a_piece) != str:
                    if a_piece.side == thinker:
                        if a_piece.canMove(self.positions):
                            return False
        return True
