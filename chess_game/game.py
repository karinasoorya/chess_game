import board, piece

class Game:

    players = {"White": True, "Black": False} #To keep track of whose turn it is
    board = None #Board for the game
    active = False #Is there a game in play?
    winner = None #Winner?
    current_player = "White"

    #Initialize a board for this game and set it to active!
    def __init__(self):
        self.active = True
        self.board = board.Board()

    #Checks to see if the move just made checkmated the other player or put them in check or if there are no moves left for the next player.
    def isThereAWinner(self):
        if(self.board.didICheckMate(self.current_player)):
            self.winner = self.current_player
            print("The winner is " + self.winner + "!")
            self.active = False
        elif(self.board.didICheck(self.current_player)):
            print("Check by " + self.current_player)
            if self.current_player == "White":
                print("Black! Your next turn has to save your king!")
            else:
                print("White! Your next turn has to save your king!")
        elif(self.board.noValidMoves(self.current_player)):
            print("Looks like we have a tie!")
            game.active = False

    #Castling logic - if the position input matches an appropriate Rook and the other castling conditions are met, and I'm not putting my king in trouble - castle.
    def castle(self, castle_x, castle_y):
        castle_y = int(castle_y) - 1
        p = self.board.positions[castle_x][castle_y]
        if type(p) == piece.Rook:
            if p.side == self.current_player:
                if p.hasNotMovedYet:
                    current_king = self.board.getKing(self.current_player)
                    if current_king.hasNotMovedYet:
                        num = int(current_king.posY)
                        if ord(castle_x) < ord(current_king.posX):
                            if type(self.board.positions['b'][num]) == str:
                                if type(self.board.positions['c'][num]) == str:
                                    if type(self.board.positions['d'][num]) == str:
                                        if not current_king.vuln(self.board.positions, current_king.posX, num):
                                            if current_king.isAllowed(self.board.positions, current_king.xmod(current_king.posX, -2), num):
                                                self.make_move(current_king.posX, num + 1, current_king.xmod(current_king.posX, -2), num + 1)
                                                self.make_move(p.posX, p.posY + 1, current_king.xmod(current_king.posX, 1), p.posY + 1)
                                                return True
                        else:
                            if type(self.board.positions['f'][num]) == str:
                                if type(self.board.positions['g'][num]) == str:
                                    if not current_king.vuln(self.board.positions, current_king.posX, num):
                                        if current_king.isAllowed(self.board.positions, current_king.xmod(current_king.posX, 2), num):
                                            self.make_move(current_king.posX, num + 1, current_king.xmod(current_king.posX, 2), num + 1)
                                            self.make_move(p.posX, p.posY + 1, current_king.xmod(current_king.posX, -1), p.posY + 1)
                                            return True
        return False

    #Flip turns
    def whoseTurn(self):
        if(self.players[self.current_player] == True):
            self.players[self.current_player] = False
            if self.current_player == "White":
                self.current_player = "Black"
            else:
                self.current_player = "White"
            self.players[self.current_player] = True

    #Call the board makeMove function
    def make_move(self, initialX, initialY, posX, posY):
        self.board.makeMove(initialX, initialY, posX, posY)
