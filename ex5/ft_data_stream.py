#! python3

from datetime import datetime
from typing import Generator


t_event = tuple[int, str, int, str]
t_stats = dict[str, int]


def generate_event(numbers) -> Generator[tuple[int, str, int, str]]:
    '''
    Generate a stream of game events
    '''

    players = ['Alice', 'Bob', 'Charlie', 'Eve']
    players_len = len(players)
    levels = [1, 41, 4, 15, 51, 543, 43]
    levels_len = len(levels)
    events = ['killed monster', 'leveled up', 'found treasure']
    events_len = len(events)

    for i in range(0, numbers):
        yield (
            i,
            players[i % players_len],
            levels[i % levels_len],
            events[i % events_len]
        )


def process_event(event: t_event, stats: t_stats) -> None:
    '''
    Process a single game event and update statistics
    '''

    event_id, name, lvl, event_type = event
    print(f'Event {event_id}: Player {name} (Level {lvl}) {event_type}')
    if (lvl >= 10):
        stats.update({
            'high_level_players': stats.get('high_level_players', 0) + 1
        })
    if (event_type == 'killed monster'):
        stats.update({
            'monsters_killed': stats.get('monsters_killed', 0) + 1
        })
    if (event_type == 'found treasure'):
        stats.update({
            'treasures_found': stats.get('treasures_found', 0) + 1
        })
    if (event_type == 'leveled up'):
        stats.update({
            'level_ups': stats.get('level_ups', 0) + 1
        })
    stats.update({
        'events_processed': stats.get('events_processed', 0) + 1
    })


def fibonacci(n: int) -> Generator[int]:
    '''
    Generate first n Fibonacci numbers
    '''

    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b = b, b + a


def primes(n: int) -> Generator[int]:
    '''
    Generate first n prime numbers
    '''

    nbr = 0
    for _ in range(n):
        is_prime = False
        while not is_prime:
            for i in range(2, nbr + 1):
                if (i == nbr):
                    is_prime = True
                    yield nbr
                    nbr += 1
                    break
                if (nbr % i == 0):
                    break
            if (not is_prime):
                nbr += 1


def ft_data_stream() -> None:
    '''
    Main function to process game data stream and demonstrate generators
    '''
    print('=== Game Data Stream Processor ===')
    print('')
    print('Prossesing 1000 game events...\n')
    events = generate_event(1000)
    stats: t_stats = {}
    start_time = datetime.now()
    for event in events:
        process_event(event, stats)
    end_time = datetime.now()
    print('\n=== Summary Statistics ===')
    for stat, value in stats.items():
        print(f'{stat.replace("_", " ").capitalize()}: {value}')
    print(f'Total processing time: '
          f'{(end_time - start_time).total_seconds()} seconds')

    print('\n=== Generator Demonstration ===')
    fibonacci_sequance = ''
    for value in fibonacci(10):
        fibonacci_sequance = ', '.join([fibonacci_sequance, str(value)])
    print(f'First 10 Fibonacci numbers: '
          f'{fibonacci_sequance.lstrip(",")}')
    primes_sequance = ''
    for value in primes(5):
        primes_sequance = ', '.join([primes_sequance, str(value)])
    print(f'First 5 prime numbers: {primes_sequance.lstrip(",")}')
    print('')


if __name__ == '__main__':
    ft_data_stream()
