'''
Part 1 of Day 2, Cube Conundrum
https://adventofcode.com/2023/day/2
'''

LIMIT = {'red': 12, 'green': 13, 'blue': 14}

def get_possible_games(games):
    '''Returns the index of games which are impossible.'''
    ans = []
    for i, game in enumerate(games):
        possible_game = True
        for round in game.split(';'):
            for result in round.split(','):
                cubes, color = result.split(' ')[1:]
                if int(cubes) > LIMIT[color]:
                    possible_game = False  # This could use a killswitch...
        if possible_game:
            ans.append(i+1)
    return ans

def read_game_results_file():
    '''Reads game results and pass it as lists of strings.'''
    results = []
    for line in open('Day2\input', mode='r').read().split('\n'):
        if not line:
            break
        game = line.split(':')[1]
        results.append(game)
    return results

def main():
    '''Process the game results.'''
    game_record = read_game_results_file()
    possible_games = get_possible_games(game_record)
    print(sum(possible_games))

if __name__ == "__main__":
    main()