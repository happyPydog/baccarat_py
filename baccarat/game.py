"""Play a Baccarat game."""
from .base_model import Hand, Deck, Dealer
from .rules import BaccaratRules, State
from .scoreboard import ScoreBoard


class BaccaratGame:
    def __init__(
        self,
        scoreboard: ScoreBoard,
        n_decks: int = 8,
        rounds: int = 1,
    ):
        self.scoreboard = scoreboard
        self.n_decks = n_decks
        self.rounds = rounds

    def init(self):
        """Initialize the game."""
        self.deck = Deck.make_deck() * self.n_decks
        self.dealer = Dealer()

    def play(self):
        self.dealer.init(self.deck)

        for _ in range(self.rounds):
            # shuffle and deal
            self.dealer.shuffle()
            first_card = self.dealer.draw()
            second_card = self.dealer.draw()
            third_card = self.dealer.draw()
            four_card = self.dealer.draw()
            player_cards = Hand([first_card, third_card])
            banker_cards = Hand([second_card, four_card])

            # check whether player and banker have two-pair
            self.scoreboard.player_two_pair.append(
                BaccaratRules.check_two_pair(player_cards)
            )
            self.scoreboard.banker_two_pair.append(
                BaccaratRules.check_two_pair(banker_cards)
            )

            # check whether check who wins immediately
            if player_cards.total_points in [8, 9] or banker_cards.total_points in [
                8,
                9,
            ]:
                result = BaccaratRules.check_who_win(player_cards, banker_cards)
                self.scoreboard.results.append(result)
                continue

            # see draw rules of player
            player_state = BaccaratRules.player(player_cards=player_cards)

            if player_state is State.DEAL:
                player_cards += self.dealer.draw()

            # see draw rules of banker
            banker_state = BaccaratRules.banker(
                banker_cards=banker_cards, player_cards=player_cards
            )

            if banker_state is State.DEAL:
                banker_cards += self.dealer.draw()

            # check who wins
            result = BaccaratRules.check_who_win(player_cards, banker_cards)
            self.scoreboard.results.append(result)

    def reset(self):
        self.dealer.init(self.deck)

    def info(self):
        self.scoreboard.info()
