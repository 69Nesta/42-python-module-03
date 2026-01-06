#! python3

import sys


def ft_command_quest():
    args = sys.argv
    args_len = len(args)
    print('=== Command Quest ===')
    if (not args_len > 1):
        print('No arguments provided!')
    if (args_len > 0):
        print(f'Program name: {args[0]}')
    if (args_len > 1):
        print(f'Arguments received: {args_len - 1}')
        for index, arg in enumerate(args[1:]):
            print(f'Argument {index + 1}: {arg}')
    print(f'Total arguments: {args_len}')


if __name__ == '__main__':
    ft_command_quest()
