import sys


class Inventory:
    SCARCE_IDS: list[str] = ['sword', 'shield', 'armor', 'helmet']

    def __init__(self, raw: list[str]) -> None:
        self.stock: dict[str, int] = {}
        self.total: int = 0

        for raw_item in raw:
            raw_splited = raw_item.strip().split(':')
            [name_raw, count_raw] = raw_splited
            name = name_raw.strip().lower()
            count = int(count_raw)
            self.total += count
            self.stock[name] = self.stock.get(name, 0) + count

    def show_system_analytics(self) -> None:
        print(f'Total items in inventory: {self.total}')
        items = set(self.stock.keys())
        print(f'Unique item types: {len(items)}')

    @staticmethod
    def get_unit(count: int) -> str:
        return f'{count} unit{"s" if count > 1 else ""}'

    def show_inventory(self) -> None:
        for name, count in sorted(
                    self.stock.items(),
                    reverse=True,
                    key=lambda x: x[1]
                ):
            print(f'{name}: {self.get_unit(count)}' +
                  f' ({count / self.total * 100:.1f}%)')

    def show_inv_stats(self) -> None:
        most = max(self.stock.items(), key=lambda x: x[1])
        least = min(self.stock.items(), key=lambda x: x[1])
        print(f'Most abundant: {most[0]} ({self.get_unit(most[1])})')
        print(f'Least abundant: {least[0]} ({self.get_unit(least[1])})')

    def show_item_categories(self) -> None:
        moderate = {
            name: count
            for name, count in self.stock.items()
            if name not in self.SCARCE_IDS
        }
        scarce = {
            name: count
            for name, count in self.stock.items()
            if name in self.SCARCE_IDS
        }
        print(f'Moderate: {moderate}')
        print(f'Scarce: {scarce}')

    def show_restock(self) -> None:
        need_restock = [
            name
            for name, count in self.stock.items()
            if count <= 1
        ]
        print(f'Restock needed: {need_restock}')

    def show_dict_props(self) -> None:
        print(f'Dictionary keys: {self.stock.keys()}')
        print(f'Dictionary values: {self.stock.values()}')
        print('Sample lookup - \'sword\' in inventory: ' +
              f'{("sword" in self.stock.keys())}')


def main() -> None:
    print('=== Inventory System Analysis ===')
    args: list[str] = sys.argv
    inv: Inventory
    try:
        if len(args) <= 1:
            raise ValueError()
        inv = Inventory(args[1:])
    except ValueError:
        print(f'Usage: python3 {args[0]} '
              'sword:1 potion:5 shield:2 armor:3 helmet:1')
        return

    inv.show_system_analytics()

    print('\n=== Current Inventory ===')
    inv.show_inventory()

    print('\n=== Inventory Statistics ===')
    inv.show_inv_stats()

    print('\n=== Item Categories ===')
    inv.show_item_categories()

    print('\n=== Management Suggestions ===')
    inv.show_restock()

    print('\n=== Dictionary Properties Demo ===')
    inv.show_dict_props()


if __name__ == '__main__':
    main()
