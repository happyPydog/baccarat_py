"""Rule of Baccarat."""
from enum import Enum, auto
from .base_model import Hand


class State(Enum):
    DEAL = auto()
    STOP = auto()
    NATURAL = auto()

class Wins(Enum):
    PLAYER = auto()
    BANKER = auto()
    TIE = auto()


class BaccaratRules:
    """Baccart rules."""

    @staticmethod
    def player(player_cards: Hand) -> str:
        match player_cards.total_points:
            case 0 | 1 | 2 | 3 | 4 | 5:
                return State.DEAL
            case 6 | 7:
                return State.STOP

    @staticmethod
    def banker(banker_cards: Hand, player_cards: Hand) -> str:
        player_thrid_card_point = (
            player_cards[2].point if len(player_cards) == 3 else None
        )
        match (banker_cards.total_points, player_thrid_card_point):
            case ((0 | 1 | 2), _):
                return State.DEAL
            case ((3 | 4 | 5), None):
                return State.DEAL
            case (3, (0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 9)):
                return State.DEAL
            case (3, 8):
                return State.STOP
            case (4, (2 | 3 | 4 | 5 | 6 | 7)):
                return State.DEAL
            case (4, (8 | 9 | 0 | 1)):
                return State.STOP
            case (5, (4 | 5 | 6 | 7)):
                return State.DEAL
            case (5, (8 | 9 | 0 | 1 | 2 | 3)):
                return State.STOP
            case (6, (6 | 7)):
                return State.DEAL
            case (6, (8 | 9 | 0 | 1 | 2 | 3 | 4 | 5)):
                return State.STOP
            case (6, None):
                return State.STOP
            case (7, _):
                return State.STOP

    @staticmethod
    def check_natural(hand_cards: Hand) -> bool:
        """Check player and banker whether determine who wins at the beginning of the game."""
        return hand_cards.total_points == 8 or hand_cards.total_points == 9

    @staticmethod
    def check_two_pair(hand_cards: Hand) -> bool:
        """Check player and banker whether two-pair at the beginning of the game."""
        return hand_cards[0].number == hand_cards[1].number
    
    @staticmethod
    def check_who_win(player_cards: Hand, banker_cards: Hand):
        """Check who win the game."""
        if player_cards.total_points > banker_cards.total_points:
            return Wins.PLAYER
        elif player_cards.total_points < banker_cards.total_points:
            return Wins.BANKER
        elif player_cards.total_points == banker_cards.total_points:
            return Wins.TIE
