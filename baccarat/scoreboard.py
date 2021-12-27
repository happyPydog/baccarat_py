"""Store result of game."""
from dataclasses import dataclass, field
from prettytable import PrettyTable
from .rules import Wins


@dataclass
class ScoreBoard:

    betting_odds: dict[str, float]
    results: list[str] = field(default_factory=list, repr=False)
    player_two_pair: list[bool] = field(default_factory=list, repr=False)
    banker_two_pair: list[bool] = field(default_factory=list, repr=False)

    def info(self):
        """All information about the results of games."""
        prob = self.get_prob()
        rate_of_return = self.rate_of_return()

        table = PrettyTable()
        print(f"{'='* 32} Results of {self.total_rounds}/rounds {'='* 31}")
        table.field_names = [
            "",
            "Player",
            "Banker",
            "Tie",
            "Player Two Pair",
            "Banker Two Pair",
        ]
        table.add_row(
            [
                "Probability of Wins",
                prob["player"],
                prob["banker"],
                prob["tie"],
                prob["player_two_pair"],
                prob["banker_two_pair"],
            ]
        )
        table.add_row(
            [
                "Rate of Return",
                rate_of_return["player"],
                rate_of_return["banker"],
                rate_of_return["tie"],
                rate_of_return["player_two_pair"],
                rate_of_return["banker_two_pair"],
            ]
        )
        print(table)
        print()

    def get_prob(self):
        """Calculate the probability of all events win."""
        player_wins = self.results.count(Wins.PLAYER)
        banker_wins = self.results.count(Wins.BANKER)
        tie = self.results.count(Wins.TIE)
        return {
            "player": player_wins / self.total_rounds,
            "banker": banker_wins / self.total_rounds,
            "tie": tie / self.total_rounds,
            "player_two_pair": sum(self.player_two_pair) / self.total_rounds,
            "banker_two_pair": sum(self.banker_two_pair) / self.total_rounds,
        }

    def rate_of_return(self):
        """Calculate the rate of return."""
        player_wins = self.results.count(Wins.PLAYER)
        banker_wins = self.results.count(Wins.BANKER)
        tie = self.results.count(Wins.TIE)
        return {
            "player": (player_wins * self.betting_odds["player"] + tie)
            / self.total_rounds,
            "banker": (banker_wins * self.betting_odds["banker"] + tie)
            / self.total_rounds,
            "tie": (tie * self.betting_odds["tie"]) / self.total_rounds,
            "player_two_pair": sum(self.player_two_pair)
            * self.betting_odds["player_two_pair"]
            / self.total_rounds,
            "banker_two_pair": sum(self.banker_two_pair)
            * self.betting_odds["banker_two_pair"]
            / self.total_rounds,
        }

    @property
    def total_rounds(self):
        return len(self.results)

    def get_result(self, index: int):
        assert index >= 1, "index at least 1."
        return self.results[index - 1]
