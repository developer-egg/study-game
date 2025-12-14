from move import Move
from member import Member
from game import Game

# Later make enum for specific types.
basic_attack = Move("Basic Attack", 10, "Normal")
strong_attack = Move("Strong Attack", 30, "Normal")

square_member = Member("Square", [basic_attack, strong_attack], "Normal")
circle_member = Member("Circle", [basic_attack, strong_attack], "Normal")

player_team = [square_member]
opponent_team = [circle_member]

new_game = Game(player_team, opponent_team)

while new_game.isGameActive:
    ## game loop

    ## this requires planning on how the game will actually be played
    pass