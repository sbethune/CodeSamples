
##############################################
# DEMO - Player Leaderboard
# Author: (@sbethune)
# Date: 03-23-2020
# Description:
#   Take a list of player id numbers (int) and print top (n) players
#   sorted by count of games won.
#   game_won = [1,2,1,3,3,2,2,1,1,1,4,4,4]
#   returns each player id and count of instances won. 
##############################################

# Import libraries
import operator
import itertools
import numpy as np

# Function to count wins and print player leaderboard
def count_wins(player_game_wins: [], n: int = 10)-> int:
    if len(player_game_wins) < 1:
        return 0

    else:        
        # Enumerate through list and store count in dict
        d = {}
        [ d.update( {i:d.get(i, 0)+1} ) for i in player_game_wins ]

        # Sort dict desc
        sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1),reverse=True))
     
        # Select top (n) player leaderboard
        leaders = dict(itertools.islice(sorted_d.items(), n))

        print ("{:<8} {:<15}".format('Player', 'Wins'))
        for k, v in leaders.items():
            print ("{:<8} {:<15}".format(k, v))

    return 1

if __name__ == '__main__':

    # Generate random list of game wins
    g = np.random.randint(low=1, high=10, size=100)
    res = count_wins(g, 5)

# END
    
