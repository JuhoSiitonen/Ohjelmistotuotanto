from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, HasFewerThan, Not, All, Or
from querybuilder import QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    """
    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(20, "assists"),
        PlaysIn("PHI")
    )
    
    matchert = And(
        HasFewerThan(2, "goals"),
        PlaysIn("NYR")
    )

    matcherv = And(
        Not(HasAtLeast(2, "goals")),
        PlaysIn("NYR")
    )

    matcherq = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
    )

    matcherw = And(
        HasAtLeast(70, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("FLA"),
            PlaysIn("BOS")
        )
    )
    """

    query = QueryBuilder()
    #matcher = query.playsIn("NYR").hasAtLeast(10, "goals").hasFewerThan(20, "goals").build()
    #matcher = query.hasAtLeast(10, "goals").build()
    #matcher = query.hasFewerThan(2, "goals").build()

    m1 = (
        query
            .playsIn("PHI")
            .hasAtLeast(10, "assists")
            .hasFewerThan(5, "goals")
            .build()
        )

    m2 = (
        query
            .playsIn("EDM")
            .hasAtLeast(50, "points")
            .build()
        )

    matcher = query.oneOf(m1, m2)
    for player in stats.matches(matcher):
        print(player)

    #for player in stats.matches(matcherw):
    #    print(player)

    #filtered_with_all = stats.matches(All())
    #print(len(filtered_with_all))


if __name__ == "__main__":
    main()
