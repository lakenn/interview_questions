from enum import Enum, auto
from typing import List

class Card:
    @property
    def card_value(self) -> int:
        raise NotImplementedError()

    def __lt__(self, other):
        return self.card_value < other.card_value

class Suit(Enum):
    CLUBS = auto()
    DIAMONDS = auto()
    HEARTS = auto()
    SPADES = auto()

class PlayingCard(Card):
    SUITS = {
        "Clubs": Suit.CLUBS,
        "Diamonds": Suit.DIAMONDS,
        "Hearts": Suit.HEARTS,
        "Spades": Suit.SPADES,
    }
    SUIT_NAMES = {e: n for n, e in SUITS.items()}
    VALUES = {
        "A": 1,
        **{str(i): i for i in range(2, 11)},
        "J": 11,
        "Q": 12,
        "K": 13,
    }
    VALUE_NAMES = {e: n for n, e in VALUES.items()}

    def __init__(self, suit: str, value: str):
        super().__init__()
        self.__suit = self.SUITS[suit]
        self.__value = self.VALUES[value]

    @property
    def card_value(self) -> int:
        return self.__value

    def __str__(self) -> str:
        value = self.VALUE_NAMES[self.__value]
        suit = self.SUIT_NAMES[self.__suit]
        return f"{value} of {suit}"

class Game:
    def __init__(self) -> None:
        self.__cards: List[Card] = []

    def add_card(self, suit: str, value: str) -> None:
        self.__cards.append(PlayingCard(suit, value))

    def card_string(self, card: int) -> str:
        return str(self.__cards[card])

    def card_beats(self, card_a: int, card_b: int) -> bool:
        return self.__cards[card_a] > self.__cards[card_b]

if __name__ == "__main__":
    game = Game()
    card = PlayingCard('Diamonds', '2')
    suit, value = input().split()
    game.add_card(suit, value)
    print(game.card_string(0))
    suit, value = input().split()
    game.add_card(suit, value)
    print(game.card_string(1))
    print("true" if game.card_beats(0, 1) else "false")