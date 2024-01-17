from Controller.tictactoe import TicTacToe

def main():
    game = TicTacToe()
    game.initialize_game()
    print("Game winner is:", game.start_game())

if __name__ == "__main__":
    main()
