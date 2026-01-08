#! python3


class Player:
    '''
    Unified Player class combining name, score, active flag,
    achievements (as a set), score categories (dict) and region.
    '''
    def __init__(
        self,
        name: str,
        score: int,
        active: bool = False,
        achievements: list[str] = None,
        scores_categories: dict[str, int] = None,
        region: str = None,
    ) -> None:
        self.name = name
        self.score = score
        self.active = active
        self.achievements = set(achievements or [])
        self.scores_categories = scores_categories or {}
        self.region = region


def demonstrate_list(players: list[Player]) -> None:
    print('=== List Comprehension Examples ===')

    high_scores = [player.name for player in players if player.score > 2000]
    print(f'High Scorers (>2000): {high_scores}')
    scores_doubled = [player.score * 2 for player in players]
    print(f'Scores doubled: {scores_doubled}')
    active_players = [player.name for player in players if player.active]
    print(f'Active Players: {active_players}')


def demonstrate_dict(l_players: list[Player]) -> None:
    print('\n=== Dictionary Comprehension Examples ===')
    players = {player.name: player for player in l_players}
    players_scores = {name: player.score for name, player in players.items()}
    print(f'Players scores: {players_scores}')

    score_categories: dict[str, int] = {}
    for _, player in players.items():
        for key, value in player.scores_categories.items():
            score_categories[key] = score_categories.get(key, 0) + value
    print(f'Score Categories: {score_categories}')

    achievements_count = {
        name: len(player.achievements)
        for name, player in players.items()
    }
    print(f'Achievement counts: {achievements_count}')


def demonstrate_set(players: list[Player]) -> None:
    print('\n=== Set Comprehension Examples ===')

    unique_players = {player.name for player in players}
    print(f'Unique player: {unique_players}')

    unique_achievements = set().union(
        *(player.achievements for player in players)
    )
    print(f'Unique achievements: {unique_achievements}')

    active_regions = {player.region for player in players if player.region}
    print(f'Active regions: {active_regions}')


def demonstrate_combined(players: list[Player]):
    print('\n=== Combined Analysis ===')

    total_players = len(players)
    print(f'Total Players: {total_players}')

    total_unique_achievments = len(set().union(*[
        player.achievements for player in players
    ]))
    print(f'Total Unique Achievements: {total_unique_achievments}')

    average_score = sum(player.score for player in players) / total_players
    print(f'Average Score: {average_score:.2f}')

    best_player = max(players, key=lambda player: player.score)
    print(f'Best Player: {best_player.name} with score {best_player.score}')


def ft_analytics_dashboard() -> None:
    print('=== Game Analytics Dashboard ===\n')
    players: list[Player] = [
        Player(
            'Alice',
            2300,
            True,
            achievements=['First Win', 'Sharp Shooter', 'First Win'],
            scores_categories={'high': 1, 'medium': 1, 'low': 1},
            region='nord',
        ),
        Player(
            'Bob',
            1800,
            True,
            achievements=['First Win'],
            scores_categories={'high': 0, 'medium': 2, 'low': 0},
            region='central',
        ),
        Player(
            'Charlie',
            2150,
            True,
            achievements=[],
            scores_categories={'high': 0, 'medium': 1, 'low': 1},
            region='central',
        ),
    ]
    demonstrate_list(players)
    demonstrate_dict(players)
    demonstrate_set(players)
    demonstrate_combined(players)


if __name__ == '__main__':
    ft_analytics_dashboard()
