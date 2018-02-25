'''
File: LovesPens.py
Date Started: 02/24/2018
Author: Jason Mizgorski

Description:
This code will be the source that will allow cozmo to monitor a Pens game, report the score, and react to the score.
The idea is to impliment in small chuncks of functionality as I start to get back into the world of programming and
expand my knowledge of robotics and teaching robotics using the Cozmo platform.

Dependancies:
1. Anki Cozmo SDK
2. evansloan082/sports.py (Thank you!)
'''

import sports_py
import cozmo


def getcurrentscore(team1,team2):
    match = sports_py.get_match_score('hockey', team1, team2)
    return match


def cozmo_program(robot: cozmo.robot.Robot):
    robot.say_text("Its a hockey night in Pittsburgh").wait_for_completed()
    robot.say_text("Lets go pens").wait_for_completed()

    currentscore = getcurrentscore('pittsburgh','XXX')
    print('{}-{}'.format(currentscore.home_score, currentscore.away_score))


cozmo.run_program(cozmo_program)




