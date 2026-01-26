#! python3

import sys


def ft_score_analytics() -> None:
    '''
    Analyzes player scores provided as command-line arguments.
    '''
    args: list[str] = sys.argv
    args_len: int = len(sys.argv)
    scores: list[int] = []
    print('=== Player Score Analytics ===')
    if (args_len <= 1):
        print('No scores provided. Usage: '
              f'python3 {args[0]} <score1> <score2> ...')
        return
    for arg in args[1:]:
        try:
            parsed_score: int = int(arg)
            scores.append(parsed_score)
        except Exception:
            print(f"Error you have typed '{arg}': its not a score!")
            return
    if len(scores) < 1:
        print('Not enough scores provided!')
        return
    print(f'Scores processed: {scores}')
    scores_len: int = len(scores)
    print(f'Total players: {scores_len}')
    print(f'Total scores: {sum(scores)}')

    average_score: float = 0.0

    for score in scores:
        average_score += score / scores_len

    print(f'Average score: : {average_score:.1f}')
    print(f'High score: {max(scores)}')
    print(f'Low score: {min(scores)}')
    print(f'Score Range: {max(scores) - min(scores)}')
    print('')


if __name__ == '__main__':
    ft_score_analytics()
