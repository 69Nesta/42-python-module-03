#! python3

class PlayerList:
    def __init__(self, name, score, active=False):
        self.name = name
        self.score = score
        self.active = active


def demonstrate_list():
    print('=== List Comprehension Examples ===')
    players: list[PlayerList] = [
        PlayerList('Alice', 2300, True),
        PlayerList('Bob', 1800, True),
        PlayerList('Charlie', 1150, True),
        PlayerList('Diana', 2050, False)
    ]
    high_scores = [player.name for player in players if player.score > 2000]
    print(f'High Scorers (>2000): {high_scores}')
    scores_doubled = [player.score * 2 for player in players]
    print(f'Scores doubled: {scores_doubled}')
    actives_players = [player.name for player in players if player.active]
    print(f'Active Players: {actives_players}')


class PlayerDict():
    def __init__(self, score: int, achievements: list[str]):
        self.score = score
        self.achievements = set(achievements)


def demonstrate_dict():
    print('\n=== Dictionary Comprehension Examples ===')
    players: dict[str, PlayerDict] = {
        'Alice': PlayerDict(2300, ['First Win', 'Sharp Shooter', 'First Win']),
        'Bob': PlayerDict(1800, ['First Win']),
        'Charlie': PlayerDict(1150, []),
        'Diana': PlayerDict(2050, ['First Win', 'Marathon Runner'])
    }
    print(players)


def ft_analytics_dashboard():
    print('=== Game Analytics Dashboard ===\n')
    demonstrate_list()
    demonstrate_dict()


if __name__ == '__main__':
    ft_analytics_dashboard()
