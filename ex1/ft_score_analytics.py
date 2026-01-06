#! python3

import sys


def ft_score_analytics():
    '''
    Analyzes player scores provided as command-line arguments.
    '''
    args = sys.argv
    args_len = len(sys.argv)
    scores: list[int] = []
    print('=== Player Score Analytics ===')
    if (args_len <= 1):
        return print('No scores provided. Usage:'
                     f'python3 {args[0]} <score1> <score2> ...')
    for score in args[1:]:
        if (not score.isdigit()):
            return print(f'Error you have typed \'{score}\': its not a score!')
        scores.append(int(score))
    if (len(scores) < 1):
        return print('Not enough scores provied!')
    print(f'Scores processed: {scores}')
    scores_len = len(scores)
    print(f'Total players: {scores_len}')
    print(f'Total scores: {sum(scores)}')
    average_score = 0.0
    for score in scores:
        average_score += score / scores_len
    print(f'Average score: : {average_score}')
    print(f'High score: {max(scores)}')
    print(f'Low score: {min(scores)}')
    print(f'Score Range: {max(scores) - min(scores)}')
    print('')


if __name__ == '__main__':
    ft_score_analytics()
