#! python3

from enum import Enum


class Rarity(Enum):
    COMMON = 'common'
    UNCOMMON = 'uncommon'
    RARE = 'rare'


class Item:
    def __init__(self, name: str, price: int, rarity: Rarity, category: str) -> None:
        self.set_name(name)
        self.set_price(price)
        self.set_rarity(rarity)
        self.set_category(category)

    def set_name(self, name: str) -> None:
        if (not name):
            raise ValueError('Name cannot be empty!')
        self._name = name

    def set_price(self, price: int) -> None:
        if (price < 0):
            raise ValueError('Price cannot be negative!')
        self._price = price

    def set_rarity(self, rarity: Rarity) -> None:
        if (type(rarity) is not Rarity):
            raise ValueError('Cannot set unknow type to rarity!')
        self._rarity = rarity

    def set_category(self, category: str) -> None:
        if (not category):
            raise ValueError('Category cannot be empty!')
        self._category = category.lower()

    def get_name(self) -> str:
        return self._name

    def get_price(self) -> int:
        return self._price

    def get_rarity(self) -> Rarity:
        return self._rarity

    def get_category(self) -> str:
        return self._category


# Category subclasses for specific item types
class Waypon(Item):
    def __init__(self, name: str, price: int, rarity: Rarity) -> None:
        super().__init__(name, price, rarity, 'Waypon')


class Consumable(Item):
    def __init__(self, name: str, price: int, rarity: Rarity) -> None:
        super().__init__(name, price, rarity, 'Consumable')


class Armor(Item):
    def __init__(self, name: str, price: int, rarity: Rarity) -> None:
        super().__init__(name, price, rarity, 'Armor')


# Specific item implementations
class LaserSword(Waypon):
    def __init__(self) -> None:
        super().__init__('Laser Sword', 500, Rarity.RARE)


class HealthPotion(Consumable):
    def __init__(self) -> None:
        super().__init__('Health Potion', 50, Rarity.COMMON)


class Shield(Armor):
    def __init__(self) -> None:
        super().__init__('Shield', 200, Rarity.UNCOMMON)


def ft_inventory_system() -> None:
    laser_sword = LaserSword()
    print(f'Item: {laser_sword.get_name()}, '
          f'Price: {laser_sword.get_price()}, '
          f'Rarity: {laser_sword.get_rarity().value}, '
          f'Category: {laser_sword.get_category()}')

if __name__ == '__main__':
    ft_inventory_system()
