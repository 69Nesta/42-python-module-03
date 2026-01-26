#! python3

import sys
import math

t_coords = tuple[int, int, int]


def calculate_distance(point_a: t_coords, point_b: t_coords) -> float:
    '''
    Calculate the Euclidean distance between two 3D points.
    :params point_a: First point as a tuple (x, y, z).
    :params point_b: Second point as a tuple (x, y, z).
    :returns: The Euclidean distance as a float.
    '''
    x1, y1, z1 = point_a
    x2, y2, z2 = point_b

    return (math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))


def parse_coordinate(coord: str) -> tuple:
    '''
    Parse a coordinate string into  a tuple of integers.
    :param coord: Coordinate string in the format "(x,y,z)".
    :returns: A tuple of three integers representing the coordinate.
    :raises ValueError: If the coordinate format is invalid.
    '''
    coord = coord.strip('()')
    point = coord.split(',')
    if (len(point) != 3):
        raise ValueError(
            'Invalid coordinate format. Expected format: xx,xx,xx')
    return tuple(map(int, point))


def parse_coordinates(arg: str, player_coords: t_coords) -> list[tuple]:
    '''
    Parse multiple coordinates from a string and calculate distances.
    :param arg: String containing coordinates in the format
                "[(x1,y1,z1), (x2,y2,z2), ...]" or "x,y,z".
    :param player_coords: Current player coordinates as a tuple (x, y, z).
    :returns: A list of tuples representing the parsed coordinates.
    '''
    coords: list[tuple] = []
    string_to_parse = arg.strip('[]')
    string_to_parse = string_to_parse.replace(' ', '')

    string_coords = string_to_parse.split('),')

    for coord in string_coords:
        try:
            parsed_coords = parse_coordinate(coord)
            distance = calculate_distance(player_coords, parsed_coords)
            print(f'Parsing coordinates: "{coord.strip("()")}"')
            print(f'Parsed position: {parsed_coords}')
            print(f'Distance between {player_coords} and {parsed_coords}: '
                  f'{distance:.2f}')
            coords.append(parsed_coords)
            player_coords = parsed_coords
        except ValueError as e:
            print(f'Parsing invalid coordinates: "{coord.strip("()")}"')
            print(f'Error parsing coordinates: {e}')
            print(f'Error details - Type: {type(e).__name__}, Args {e.args}')
        finally:
            print('')
    return (coords)


def print_distance(point_a: t_coords, point_b: t_coords) -> None:
    distance = calculate_distance(point_a, point_b)
    print(f'Distance between {point_a} and {point_b}: '
          f'{distance:.2f}')


def ft_coordinate_system() -> None:
    '''
    Main function to demonstrate coordinate parsing and distance calculation.
    Accepts command-line arguments for coordinates and processes them.
    1. If no arguments are provided, it prints usage instructions.
    2. Parses the provided coordinates and calculates distances from the
       player's current position.
    3. Unpacks the final player coordinates and displays them.
    '''
    argv = sys.argv
    argc = len(sys.argv)
    if (not argc > 1):
        return print(f'No coords provided. Usage: '
                     f'python3 {argv[0]} xx,xx,xx or [(xx,xx,xx), ...]')
    print('=== Game Coordinate System ===\n')
    spawn_coords = (0, 0, 0)
    player_coords = (10, 20, 5)
    print(f'Positon created at : {player_coords}')
    print_distance(spawn_coords, player_coords)
    print()
    try:
        coords = parse_coordinates(argv[1], spawn_coords)
        if (len(coords) > 0):
            player_coords = coords.pop()
    except ValueError as e:
        return print(e)

    (x, y, z) = player_coords
    print('Unpacking demonstration:')
    print(f'Player at x={x}, y={y}, z={z}')
    print(f'Coordinates: X={x}, Y={y}, Z={z}')


if __name__ == '__main__':
    ft_coordinate_system()
