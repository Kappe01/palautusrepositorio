from statistics_1 import Statistics
from player_reader import PlayerReader
from matchers import QueryBuilder, And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()

    matcher = (
  query
    .oneOf(
      query.hasAtLeast(10, "assists").playsIn("PHI")
          .build(),
      query.hasAtLeast(50, "points").playsIn("EDM")
          .build()
    )
    .build()
)

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
