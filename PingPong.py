import random
from turtle import Screen
import time
from ping import Ping
from pong import Pong
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=1300,height=900)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)
game_is_on = True

score = ScoreBoard()
ping = Ping()
pong = Pong()

screen.listen()
screen.onkey(ping.moveUpPlayerOne,"Up")
screen.onkey(ping.moveUpPlayerTwo,"w")
screen.onkey(ping.moveDownPlayerOne,"Down")
screen.onkey(ping.moveDownPlayerTwo,"s")



sleep = 0.08

while(game_is_on):
    time.sleep(sleep)
    screen.update()
    pong.move()

    # Detect Collision with Wall

    if(pong.ycor() > 430.00 or pong.ycor() < -430.00):
        pong.bounceY()

    # Detect Collision with Ping

    if((pong.distance(ping.playersList[1]) < 80 and pong.xcor() > 570)  or (pong.distance(ping.playersList[0]) < 80 and pong.xcor() < -570)):
        pong.bounceX()
        if(sleep > 0.03):
            sleep -= 0.01

   # Detect if Pong Passes the Ping
    if(pong.xcor() > 645.00):
            sleep = 0.08
            pong.reset_pong()
            score.playerOnePt()

    if(pong.xcor() < -650.00):
            sleep = 0.08
            pong.reset_pong()
            score.playerTwoPt()

    if(score.playerOne == 7 or score.playerTwo == 7):
        if(score.playerOne == 7):
            score.game_over(1)
            game_is_on = False
        else:
            score.game_over(2)
            game_is_on = False
            


screen.exitonclick()