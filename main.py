import game as g

if __name__ == "__main__":
    game = g.Game()
    print("To play a move, enter a piece like 'wP' followed by its position like 'c2' and its desired end location like 'c4'. To castle, enter the word 'castle' followed by the position of the castle you would like to castle with your King.")
    while game.active:
        game.board.printer()
        entered = input(game.current_player + ", enter a piece followed by its initial position and a new position: ")
        entered = entered.split()
        try:
            if entered[0] == 'castle':
                castle_posX = entered[1][0]
                castle_posY = entered[1][1]
                oot = game.castle(castle_posX, castle_posY)
                if not oot:
                    print("\n\nThere's an issue with your situation that doesn't allow for castling at the moment.")
                else:
                    print("Successfully castled!")
                    game.isThereAWinner()
                    game.whoseTurn()
            else:
                p = entered[0]
                initialX = entered[1][0]
                initialY = entered[1][1]
                posX = entered[2][0]
                posY = entered[2][1]
                if game.board.input_validate(game.current_player, p, initialX, initialY, posX, posY):
                    game.make_move(initialX, initialY, posX, posY)
                    game.isThereAWinner()
                    game.whoseTurn()
                else:
                    print("Invalid move! Either you're not allowed to move in this way or your king is in danger.")
        except:
            print("\n\n" + "    There was an issue with your input. Please try again!")
