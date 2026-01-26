#! python3

PLAYER_RAW = {
    'alice': [
        'first_blood',
        'pixel_perfect',
        'speed_runner',
        'first_blood',
        'first_blood',
        'level_master'
    ],
    'bob': [
        'level_master',
        'boss_hunter',
        'treasure_seeker',
        'level_master',
        'level_master'
    ],
    'charlie': [
        'treasure_seeker',
        'boss_hunter',
        'combo_king',
        'first_blood',
        'level_master',
        'boss_hunter',
        'first_blood',
        'boss_hunter',
        'first_blood'
    ],
    'diana': [
        'first_blood',
        'combo_king',
        'level_master',
        'treasure_seeker',
        'speed_runner',
        'combo_king',
        'combo_king',
        'level_master'
    ],
    'eve': [
        'level_master',
        'treasure_seeker',
        'first_blood',
        'treasure_seeker',
        'first_blood',
        'treasure_seeker'
    ],
    'frank': [
        'explorer',
        'level_master',
        'boss_hunter',
        'first_blood',
        'explorer',
        'first_blood',
        'boss_hunter'
    ]
}


class Player:
    '''
    Class representing a player with a name and a set of achievements.
    '''
    def __init__(self, name: str, achievements: list[str]):
        '''
        Initialize a Player instance.
        :param name: Name of the player.
        :param achievements: List of achievement strings.
        '''
        self.name = name.capitalize()
        self.achievements = set(achievements)

    def get_achievements(self) -> set[str]:
        '''
        Get the set of achievements for the player.
        :returns: A set of achievement strings.
        '''
        return self.achievements

    def get_name(self) -> str:
        '''
        Get the name of the player.
        :returns: The player's name as a string.
        '''
        return self.name

    def get_display(self) -> str:
        '''
        Get a display string for the player and their achievements.
        :returns: A formatted string displaying the player's name and
        achievements.
        '''
        return f'Player {self.get_name()} achievements: {self.achievements}'


def ft_achievement_tracker() -> None:
    '''
    Main function to demonstrate achievement tracking and analytics.
    '''
    print('=== Achievement Tracker System ===\n')
    players: list[Player] = []
    for name, achievements in PLAYER_RAW.items():
        players.append(Player(name, achievements))
    for player in players:
        print(player.get_display())
    print('\n=== Achievement Analytics ===\n')

    if (len(players) == 0):
        return print('Not enough players!')

    all_achievements: list[set[str]] = [
        player.get_achievements() for player in players
    ]

    all_unique_achievements: set[str] = set.union(*all_achievements)
    print(f'All unique achievements: {all_unique_achievements}')
    print(f'Total unique achievements: {len(all_unique_achievements)}\n')

    common_to_all_player: set[str] = set.intersection(*all_achievements)
    print(f'Common to all players: {common_to_all_player}\n')

    rare_achievements: set[str] = set.difference(*all_achievements)
    print(f'Rare achievements (1 player): {rare_achievements}\n')

    player1 = players[0]
    player2 = players[1]
    print(f'{player1.get_name()} vs {player2.get_name()} common: '
          f'{player1.achievements.intersection(player2.achievements)}')
    print(f'{player1.get_name()} unique: '
          f'{player1.achievements.difference(player2.achievements)}')
    print(f'{player2.get_name()} unique: '
          f'{player2.achievements.difference(player1.achievements)}')


if __name__ == '__main__':
    ft_achievement_tracker()
