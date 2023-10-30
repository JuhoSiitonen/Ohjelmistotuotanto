import unittest
from statistics_service import StatisticsService
from player import Player
from sortby import SortBy

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_konstruktori_toimii(self):
        self.assertAlmostEqual(len(self.stats._players), 5)

    def test_etsinta_toimii(self):
        loytyy = self.stats.search("Kurri")
        self.assertEqual(loytyy.name, "Kurri")

    def test_etsinta_toimii_none(self):
        loytyy = self.stats.search("pluurrjs")
        self.assertEqual(loytyy, None)

    def test_tiimit(self):
        tiimi = self.stats.team("EDM")
        self.assertAlmostEqual(len(tiimi), 3)

    def test_tiimit_none(self):
        tiimi = self.stats.team("qqq")
        self.assertAlmostEqual(len(tiimi), 0)

    def test_top_toimii_kolmella(self):
        parhaat = self.stats.top(3)
        self.assertAlmostEqual(len(parhaat), 4)

    def test_top_goals(self):
        parhaat = self.stats.top(3, SortBy.GOALS)
        self.assertAlmostEqual(parhaat[0].goals, 45)

    def test_top_assists(self):
        parhaat = self.stats.top(3, SortBy.ASSISTS)
        self.assertAlmostEqual(parhaat[0].assists, 89)
