'''
Part 2 of Day 2, Cube Conundrum
https://adventofcode.com/2023/day/2
'''

LOCATION = {'red': 0, 'green': 1, 'blue': 2}

def get_minimum_cubes(games):
    '''Returns the minimum of each cube that are needed per game.'''
    ans = []
    for game in games:
        cur_ans = [0, 0, 0]
        for round in game.split(';'):
            for result in round.split(','):
                cubes, color = result.split(' ')[1:]
                cur_ans[LOCATION[color]] = max(cur_ans[LOCATION[color]], int(cubes))
        ans.append(cur_ans)
    return ans

def get_powers(set_list):
    '''Returns a list containing the power of each list inside.'''
    ans = []
    for _set in set_list:
        ans.append(_set[0]*_set[1]*_set[2])
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
    minimum_cubes = get_minimum_cubes(game_record)
    powers = get_powers(minimum_cubes)
    print(sum(powers))

if __name__ == "__main__":
    main()