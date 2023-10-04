__author__ = "<Marion Millard-Grelet>"
__organization__ = "COSC343, University of Otago"
__email__ = "<milma737@student.otago.ac.nz>"

from itertools import product
import random
from mastermind import evaluate_guess


class MastermindAgent():
    """
                A class that encapsulates the code dictating the
                 behaviour of the agent playing the game of Mastermind.

                 ...

                 Attributes
                ----------
                code_length: int
                   the length of the code to guess
                 colours : list of char
                     a list of colours represented as characters
                 num_guesses : int
                    the max. number of guesses per game

                 Methods
                -------
                AgentFunction(percepts)
                     Returns the next guess of the colours on the board
                 """

    def __init__(self, code_length,  colours, num_guesses):
        """
               :param code_length: the length of the code to guess
               :param colours: list of letter representing colours used to play
               :param num_guesses: the max. number of guesses per game
              """
        self.code_length = code_length
        self.colours = colours
        self.num_guesses = num_guesses
        self.all_codes = [''.join(p) for p in product(self.colours, repeat=self.code_length)]
        self.possible_codes = self.all_codes.copy()

    def score(self, guess, possibilities):
        """
            Computes the score for a given guess against the list of possible codes.

            Parameters:
            guess (str): The guess code to be evaluated.
            possibilities (list): A list of possible codes.

            Returns:
            int: The score indicating the number of codes that have the same evaluation result as the guess.
            """
        scores = []
        for code in possibilities:
            in_place, in_colour = evaluate_guess(guess, code)
            scores.append((in_place, in_colour))
        return scores.count(max(scores, key=scores.count))

    def best_guess(self):
        """
            Determine the best guess code based on the current list of possible codes.

            Returns:
            str: The best guess code to be used for the next move.
            """
        best_score = -1
        # Randomly sample a certain number of codes to consider
        num_samples = min(100, len(self.possible_codes))
        sampled_codes = random.sample(self.possible_codes, num_samples)
        for guess in sampled_codes:  # only consider a subset of possible_codes as guesses
            score = self.score(guess, self.possible_codes)
            if score > best_score:
                best_score = score
                best_guess = guess
        return best_guess

    def AgentFunction(self, percepts):
        """
        Determine the next action (guess) of the agent based on the current percepts.

        Parameters:
        percepts (tuple): A tuple containing the current guess counter, the last guess,
        and the feedback for the last guess.

        Returns:
        list: The next guess of the agent.
        """
        guess_counter, last_guess, in_place, in_colour = percepts

        if guess_counter == 0:
            self.possible_codes = self.all_codes.copy()  # reset possible_codes at start of each game
            if self.code_length == 3:
                actions = [self.colours[0]] * 2 + [self.colours[1]]  # pair of first color + one of second color
            elif self.code_length == 4:
                actions = [self.colours[0]] * 2 + [self.colours[1]] * 2  # two pairs of colors
            elif self.code_length == 5:
                actions = [self.colours[0]] * 2 + [self.colours[1]] * 2 + [
                    self.colours[2]]  # two pairs of colors + one third color
            elif self.code_length == 6:
                actions = [self.colours[0]] * 2 + [self.colours[1]] * 2 + [self.colours[2]] * 2  # three pairs of colors
            else:
                actions = [random.choice(self.colours) for _ in
                           range(self.code_length)]  # for other lengths, choose random colors
        else:
            last_guess_list = list(last_guess)
            self.possible_codes = [code for code in self.possible_codes if
                                   evaluate_guess(list(code), last_guess_list) == (in_place, in_colour)]
            if not self.possible_codes:  # if no possible codes left
                self.possible_codes = self.all_codes.copy()  # reset to all codes
            actions = list(self.best_guess())
        return actions


