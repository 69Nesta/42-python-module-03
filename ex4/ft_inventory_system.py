#! python3

RAW_PLAYERS = {
    'alice': {
        'items': {
            'pixel_sword': 1,
            'code_bow': 1,
            'health_byte': 5,
            'quantum_ring': 3
        },
        'total_value': 1975,
        'item_count': 10
    },
    'bob': {
        'items': {
            'code_bow': 3,
            'pixel_sword': 2
        },
        'total_value': 900,
        'item_count': 5
    },
    'charlie': {
        'items': {
            'pixel_sword': 1,
            'code_bow': 1
        },
        'total_value': 350,
        'item_count': 2
    },
    'diana': {
        'items': {
            'code_bow': 3,
            'pixel_sword': 3,
            'health_byte': 3,
            'data_crystal': 3
        },
        'total_value': 4125,
        'item_count': 12
    }
}

ITEMS = {
    'pixel_sword': {
        'name': 'Pixel Sword',
        'type': 'weapon',
        'value': 150,
        'rarity': 'common'
    },
    'quantum_ring': {
        'name': 'Quantum Ring',
        'type': 'accessory',
        'value': 500,
        'rarity': 'rare'
    },
    'health_byte': {
        'name': 'Health Byte',
        'type': 'consumable',
        'value': 25,
        'rarity': 'common'
    },
    'data_crystal': {
        'name': 'Data Crystal',
        'type': 'material',
        'value': 1000,
        'rarity': 'legendary'
    },
    'code_bow': {
        'name': 'Code Bow',
        'type': 'weapon',
        'value': 200,
        'rarity': 'uncommon'
    }
}


t_inventory = dict[str, int | dict[str, int]]


t_transactions = list[tuple[str, str, int]]


def get_item(item_key: str) -> dict[str, int | str]:
    return ITEMS[item_key]


class Inventory:
    def __init__(self, name: str, raw: t_inventory):
        self.name = name.capitalize()
        self.items: dict[str, int] = raw['items']
        self.total_value = raw['total_value']
        self.item_count = raw['item_count']

    def get_item_values(self, item_key: str) -> dict[str, int | str]:
        item = get_item(item_key).copy()
        item.update({'count': self.items.get(item_key)})
        return item

    def remove_item(self, item_key: str,
                    transactions: t_transactions, quantity=1) -> None:
        item = self.items.get(item_key)
        if (quantity < 0):
            raise ValueError('Quantity cannot be negative')
        if (item and item >= quantity):
            self.items.update({item_key: item - quantity})
            transactions.append((self.name, item_key, item - quantity))
            self.update()
        else:
            raise ValueError('Not enough items')

    def add_item(self, item_key: str,
                 transactions: t_transactions, quantity=1) -> None:
        item = self.items.get(item_key)
        if (quantity < 0):
            raise ValueError('Quantity cannot be negative')
        if (item):
            self.items.update({item_key: item + quantity})
            transactions.append((self.name, item_key, item + quantity))
        else:
            self.items.update({item_key: quantity})
            transactions.append((self.name, item_key, quantity))
        self.update()

    def update(self) -> None:
        new_total_value = 0
        new_item_count = 0
        for item, count in self.items.items():
            new_item_count += count
            new_total_value += self.get_item_values(item).get('value') * count
        self.total_value = new_total_value
        self.item_count = new_item_count

    def display_inventory(self) -> None:
        print(f'=== {self.name}\'s Inventory ===')
        for item_key, count in self.items.items():
            stats = self.get_item_values(item_key)
            price = stats.get('value')
            if (count > 0):
                print(f'{stats.get('name')} ({stats.get('type')}, '
                      f'{stats.get('rarity')}): '
                      f'{count}x @ {price} gold each = {count * price} gold')
        print('')
        print(f'Inventory value: {self.total_value} gold')
        print(f'Item count: {self.item_count} items')

        items_list = list(map(self.get_item_values, self.items.keys()))
        categories = {}
        for item in items_list:
            if (categories.get(item.get('type'))):
                categories[item.get('type')] += item.get('count')
            else:
                categories[item.get('type')] = item.get('count')
        categories_str = ''
        for name, count in categories.items():
            categories_str += f'{name}({count}) '
        print(f'Categories: {categories_str}')


def give(inv_from: Inventory, inv_to: Inventory, item_key: str,
         transactions: t_transactions, quantity=1):
    item = get_item(item_key)
    if (quantity <= 0):
        raise ValueError('Quantity cannot be negative')
    print(f'=== Transaction: {inv_from.name} gives {inv_to.name} '
          f'{quantity} {item.get('name')} ===')
    try:
        inv_from.remove_item(item_key, transactions, quantity)
        print('Transaction successful!')
        inv_to.add_item(item_key, transactions, quantity)
    except ValueError as e:
        print(e)


def print_transactions(transactions: t_transactions) -> None:
    print('=== Updated Inventories ===')
    for transaction in transactions:
        print(f'{transaction[0]} {transaction[1]}: {transaction[2]}')


def inventories_report(players: dict[str, Inventory]):
    print('=== Inventory Analytics ===')
    richest = max(players.items(), key=lambda x: x[1].total_value)
    print(f'Most valuable player: {richest[1].name} '
          f'({richest[1].total_value} gold)')
    most_items = max(players.items(), key=lambda x: x[1].item_count)
    print(f'Most items: {most_items[1].name} '
          f'({most_items[1].item_count} items)')
    legendary_item_names = [
        item.get('name') for item in ITEMS.values() if (
            item['rarity'] == 'legendary'
        )
    ]
    print(f'Rarest items: {str(legendary_item_names).strip('[]')}')


def ft_inventory_system() -> None:
    players: dict[str, Inventory] = {}
    transactions: t_transactions = []
    for name, inventory in RAW_PLAYERS.items():
        players[name] = Inventory(name, inventory)

    print('=== Player Inventory System ===')
    print('')
    players['alice'].display_inventory()
    print('')
    give(players['alice'], players['bob'], 'pixel_sword', transactions, 1)
    print('')
    print_transactions(transactions)
    print('')
    inventories_report(players)


if __name__ == '__main__':
    ft_inventory_system()
