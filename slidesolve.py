from random import choice


class Game:
    def __init__(self, matrix_size=3):
        """Creates new instance of Game. Matrix size can be used to specify number of columns and rows."""
        # Currently the last cell of the last row is the empty cell
        # I may change to have empty cell chosen at random. In which case I will probably reimplement as dictionary.
        self.board = []

        num_cells = matrix_size ** 2

        values = list(range(1, num_cells))

        for i in range(matrix_size):
            self.board.append([])

        fill_row = 0
        iterations = 0
        while fill_row < matrix_size:
            while iterations < matrix_size:
                if fill_row == matrix_size - 1 and iterations == matrix_size - 1:
                    # "Empty cell" is represented as the integer 0
                    self.board[fill_row].append(0)
                    iterations += 1
                else:
                    temp = choice(values)
                    values.remove(temp)
                    self.board[fill_row].append(temp)
                    iterations += 1
            iterations = 0
            fill_row += 1

    def Play(self):
        """Enters 'play mode', creates a temporary copy of the game board, which can be manipulated, saved, or deleted. Exiting without saving will delete temporary board. Solving the puzzle will result in a win and will require the creation of a new game instance."""
        def is_valid_move(move_from, move_to):
            pass

        board_clone = self.board.copy()
        solved = False
