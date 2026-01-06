#! python3

RAW_PLAYERS = {
    'alice': {
        'items': {
            'pixel_sword': 1,
            'code_bow': 1,
            'health_byte': 1,
            'quantum_ring': 3
        },
        'total_value': 1875,
        'item_count': 6
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
        'type': 'weapon',
        'value': 150,
        'rarity': 'common'
    },
    'quantum_ring': {
        'type': 'accessory',
        'value': 500,
        'rarity': 'rare'
    },
    'health_byte': {
        'type': 'consumable',
        'value': 25,
        'rarity': 'common'
    },
    'data_crystal': {
        'type': 'material',
        'value': 1000,
        'rarity': 'legendary'
    },
    'code_bow': {
        'type': 'weapon',
        'value': 200,
        'rarity': 'uncommon'
    }
}


t_inventory = dict[str, int | dict[str, int]]


class Inventory:
    def __init__(self, name: str, raw: t_inventory):
        self.name = name.capitalize()
        self.items: dict[str, int] = raw['items']
        self.total_value = raw['total_value']
        self.item_count = raw['item_count']

    def get_item_values(self, item_key: str) -> dict[str, int | str]:
        item = ITEMS[item_key].copy()
        item.update({'count': self.items.get(item_key)})
        return item

    def remove_item(self, item_key: str, quantity=1) -> None:
        item = self.items.get(item_key)
        if (item and item >= quantity):
            self.items.update({item_key: item - quantity})

    def add_item(self, item_key: str, quantity=1) -> None:
        item = self.items.get(item_key)
        if (item):
            self.items.update({item_key: item - quantity})
        else:
            self.items.update({item_key: quantity})

    def update(self) -> None:
        new_total_value = 0
        for item, count in self.items.items():
            new_total_value += self.get_item_values(item).get('value') * count
        print(self.total_value)
        print(new_total_value)
        self.total_value = new_total_value
        self.item_count = len(self.items)

    def display_inventory(self) -> None:
        print(f'=== {self.name}\'s Inventory ===')
        for item_key, count in self.items.items():
            stats = self.get_item_values(item_key)
            price = stats.get('value')
            print(f'{item_key} ({stats.get('type')}, {stats.get('rarity')}): '
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
        print(f'Categories: {categories}')


def ft_inventory_system() -> None:
    players: dict[str, Inventory] = {}
    for name, inventory in RAW_PLAYERS.items():
        players[name] = Inventory(name, inventory)

    print(*(name for name, inventory in players.items()))

    players['alice'].remove_item('pixel_sword', 2)
    print('\nInventory')
    print(players['alice'].display_inventory())
    print('')


if __name__ == '__main__':
    ft_inventory_system()
