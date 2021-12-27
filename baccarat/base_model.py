"""Model Interface."""
from dataclasses import dataclass, field
from typing import Protocol, Union
import random


class HandCard(Protocol):
    @property
    def total_points(self) -> int:
        ...


@dataclass
class Card:
    number: str
    suits: str
    point: int

    def __repr__(self) -> str:
        return self.number + self.suits


@dataclass
class Hand:
    cards: list[Card] = field(default_factory=list)

    @property
    def total_points(self) -> int:
        return sum([card.point for card in self.cards]) % 10

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, index):
        return self.cards[index]

    def __repr__(self) -> str:
        return ",".join([card.number + card.suits for card in self.cards])

    def __add__(self, card: Union[Card, list[Card]]):
        if isinstance(card, Card):
            return Hand([*self.cards, card])
        elif isinstance(card, list):
            return Hand([*self.cards, *card])
        else:
            raise TypeError(
                f"{type(card)} is not subclass of 'baccarat._base_model.Card' or 'baccarat._base_model.Hand'."
            )

    def __eq__(self, other: HandCard) -> bool:
        return self.total_points == other.total_points

    def __lt__(self, other: HandCard) -> bool:
        return self.total_points < other.total_points

    def __gt__(self, other: HandCard) -> bool:
        return self.total_points > other.total_points


class Deck:
    value = {
        "A": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 0,
        "J": 0,
        "Q": 0,
        "K": 0,
    }
    suits = "♡♠♢♣"

    @classmethod
    def make_deck(cls):
        return [
            Card(number, suit, point)
            for number, point in cls.value.items()
            for suit in cls.suits
        ]


@dataclass(repr=False)
class Dealer:
    def init(self, deck: list[Card]):
        self.deck = deck.copy()

    def draw(self):
        """Draw a card from the deck top."""
        return self.deck.pop(0)

    def shuffle(self):
        """Shuffle cards of deck."""
        random.shuffle(self.deck)
