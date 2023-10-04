# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Import the MastermindGame and Player classes from the mastermind module
# from mastermind import MastermindGame, Player
#
# # Import the MastermindAgent class from the my_agent module
# from my_agent import MastermindAgent
#
# # Import the game_settings dictionary from the settings module
# from settings import game_settings
#
# # Get the settings from the game_settings dictionary
# agent_file = game_settings['agentFile']
# code_length = game_settings['codeLength']
# num_colours = game_settings['numberOfColours']
# num_guesses = game_settings['maxNumberOfGuesses']
# num_games = game_settings['totalNumberOfGames']
#
# # Initialize the Mastermind game environment
# game_env = MastermindGame(code_length=code_length, num_colours=num_colours, verbose=game_settings['verbose'])
#
# # Initialize the Player
# player = Player(playerFile=agent_file, code_length=code_length, colours=game_env.colours, num_guesses=num_guesses)
#
# results = []
#
# # Run the agent on the game for a certain number of iterations
# for i in range(num_games):
#     # Generate a random target code
#     target = np.random.choice(game_env.colours, game_env.code_length)
#
#     # Play the game and get the score
#     score = game_env.play(player, target, num_guesses=num_guesses)
#
#     # Record the results of the game
#     results.append({
#         'game': i + 1,
#         'score': score,
#         'code': ''.join(target),
#     })
#
# # Convert the results to a pandas DataFrame
# df = pd.DataFrame(results)
#
# # Export the DataFrame to an Excel file
# df.to_excel('/Users/marionmillard/cosc343report 3/figures/file.xlsx', index=False)
#
# # Create a histogram of the scores
# plt.hist(df['score'], bins=np.arange(1, df['score'].max() + 1))
# plt.title('Histogram of Scores')
# plt.xlabel('Score')
# plt.ylabel('No of Games')
# plt.savefig('/Users/marionmillard/cosc343report 3/figures/Histogram.png')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

# Import the MastermindGame and Player classes from the mastermind module
from mastermind import MastermindGame, Player

# Import the MastermindAgent class from the my_agent module
from my_agent import MastermindAgent

# Import the game_settings dictionary from the settings module
from settings import game_settings

# Get the settings from the game_settings dictionary
agent_file = game_settings['agentFile']
code_length = game_settings['codeLength']
num_colours = game_settings['numberOfColours']
num_guesses = game_settings['maxNumberOfGuesses']
num_games = game_settings['totalNumberOfGames']

# Initialize the Mastermind game environment
game_env = MastermindGame(code_length=code_length, num_colours=num_colours, verbose=game_settings['verbose'])

# Initialize the Player
player = Player(playerFile=agent_file, code_length=code_length, colours=game_env.colours, num_guesses=num_guesses)

results = []

# Run the agent on the game for a certain number of iterations
for i in range(num_games):
    # Generate a random target code
    target = np.random.choice(game_env.colours, game_env.code_length)

    # Record the start time
    start_time = time.time()

    # Play the game and get the score
    score = game_env.play(player, target, num_guesses=num_guesses)

    # Calculate the game duration
    duration = time.time() - start_time

    # Record the results of the game
    results.append({
        'game': i + 1,
        'score': score,
        'code': ''.join(target),
        'duration': duration,
    })

# Convert the results to a pandas DataFrame
df = pd.DataFrame(results)

# Export the DataFrame to an Excel file
df.to_excel('/Users/marionmillard/cosc343report 3/figures/filescatter5codes.xlsx', index=False)

# Create a scatter plot of the scores against the game durations
plt.scatter(df['duration'], df['score'], alpha=0.5)

# # Add an average line
# mean_score = df['score'].mean()
# plt.axhline(mean_score, color='red', linestyle='--')

plt.title('Scores vs Game Durations')
plt.xlabel('Game Duration (seconds)')
plt.ylabel('Score')
plt.savefig('/Users/marionmillard/cosc343report 3/figures/Scattorplot5codes.png')
