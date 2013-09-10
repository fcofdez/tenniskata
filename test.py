import unittest
import mock
import random


class Player(object):


    def __init__(self):
       self._points = 0

    def points(self):
        return self._points

    def annotate(self, points):
         self._points += points

class TennisMatch(object):

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.turn = player1

    def num_players(self):
        return 2

    def play_point(self):
        point_winner = getattr(self, "player%d" % random.randint(1,2))
        point_winner.annotate(15)

    def scoreboard(self):
        return "%i-%i" % (self.player1.points(), self.player2.points())



class TennisTest(unittest.TestCase):

    def setUp(self):
        self.sut = Player()

    def test_player_has_zero_points_at_init(self):
        self.assertEquals(0, self.sut.points())

    def test_player_first_annotate_point(self):
        self.sut.annotate(15)
        self.assertEquals(15, self.sut.points())

    def test_player_second_annotate_point(self):
        self.sut.annotate(15)
        self.sut.annotate(15)
        self.assertEquals(30, self.sut.points())


class TennisMatchTest(unittest.TestCase):

    def test_match_has_two_players(self):
        player1_mock = Player()#mock.Mock()
        player2_mock = Player()#mock.Mock()
        self.sut = TennisMatch(player1_mock, player2_mock)
        self.assertEquals(2, self.sut.num_players())

    def test_match_play_point(self):
        player1_mock = Player()#mock.Mock()
        player2_mock = Player()#mock.Mock()
        self.sut = TennisMatch(player1_mock, player2_mock)
        before_scoreboard = self.sut.scoreboard()
        self.sut.play_point()
        self.assertNotEquals(self.sut.scoreboard(), before_scoreboard)

