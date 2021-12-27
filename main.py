"""Main"""
from tqdm import tqdm
import hydra
from baccarat.game import BaccaratGame
from baccarat.scoreboard import ScoreBoard


@hydra.main(config_path="conf", config_name="config")
def main(cfg):

    ####################
    # With Replacement #
    ####################
    scoreboard = ScoreBoard(cfg.betting_odds)
    game = BaccaratGame(scoreboard, cfg.number_of_decks, rounds=1)
    game.init()

    for _ in tqdm(range(int(cfg.with_replacement_rounds))):
        game.play()
        game.reset()

    print(f"{'='* 35} With Replacement {'='*35}")
    game.info()

    #######################
    # Without Replacement #
    # #####################
    scoreboard = ScoreBoard(cfg.betting_odds)
    game = BaccaratGame(scoreboard, cfg.number_of_decks, rounds=60)
    game.init()

    for _ in tqdm(range(cfg.without_replacement_rounds)):
        game.play()
        game.reset()

    print(f"{'='* 34} Without Replacement {'='* 33}")
    game.info()


if __name__ == "__main__":
    main()
