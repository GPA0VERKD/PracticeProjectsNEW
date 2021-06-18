import math
import random

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    # all players get their next move
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        # recursive min-max algorithm
        else:
            square = self.minimax(game, self.letter)['position']
        return square
    
    # recursive function
    def minimax(self, state, player):
        # tracks 'Genius' bot
        max_player = self.letter
        # switches between player and bot every recursive call
        other_player = 'O' if player == 'X' else 'X'
        # base cases
        if state.current_winner == other_player:
            # return position AND score for min-max algorithm to work, use dictionary
            return {'position': None,
                    'score': 1 * (state.num_empty_squares()) + 1 if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)
                    }
        # no empty squares
        elif not state.empty_squares(): 
            return {'position': None,
                    'score': 0}
        
        # initialize dictionaries
        if player == max_player:
            # tracking the bot, so need to maximize score, default will be negative inf
            best = {'position': None,
                    'score': -math.inf}
        else:
            # tracking the player, so need to minimize the score, default will be pos inf
            best = {'position': None,
                    'score': math.inf}
        
        # recursive case for each possible square
        for possible_move in state.available_moves():
            # try a move
            state.make_move(possible_move, player)
            # use recursion to simiulate game
            sim_score = self.minimax(state, other_player)
            # undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move
            # update dictionary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best